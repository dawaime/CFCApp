from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect, JsonResponse
from .models import dependent, beneficiary, beneficiary_house, beneficiary_income_expense, supporter_operation, entity, individual, individual_supporter_operation, entity_supporter_operation
from .forms import RegisterForm
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import logging
import os
import json
from openpyxl import Workbook
from openpyxl.styles import *
import decimal

# Set up logging
logger = logging.getLogger(__name__)

# Utility functions =======================================


def convert_to_date(date_str):
    if not date_str:
        return None  # or handle it as needed in your context

    try:
        return datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        print(f"Invalid date format for {date_str}")
        return None  # or raise an exception, depending on your requirement


def is_valid_queryparam(param, type):
    if type == 1:
        return param != '' and param is not None
    elif type == 2:
        return param != "اختار..." and param is not None

# View Handlers ==============================================


def individual2test(request):
    return render(request, 'main/individual2.html')


def individualtest(request):
    return render(request, 'main/individual.html')


def test2(request):
    return render(request, "main/index2.html")


def home(request):
    return render(request, "home.html")


def home_redirect(request):
    return redirect("/home")


def confirmBeneficiaryRequestView(request):
    return render(request, "main/confirmBeneficiaryReq.html")


def sign_up(request):
    if request.method == 'POST':

        form = RegisterForm(request.POST)
        if form.is_valid():
            # consider the case when the user already exists
            # if User.objects.filter(username=form.cleaned_data.username).exists():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    context = {
        "form": form
    }

    return render(request, "registration/sign_up.html", context)


def signin(request):

    if request.method == 'POST':

        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "تم تسجيل الدخول بنجاح")
            return redirect("home")
        else:
            messages.error(request, "كلمة المرور أو اسم المستخدم خطأ!")
            return redirect("login")

    return render(request, "registration/login.html")


@login_required(login_url="/login")
def dashboard(request):
    # insights for the dashboard
    beneficiaries_num = beneficiary.objects.count()
    supporter_operations_num = supporter_operation.objects.count()
    entities_num = entity.objects.count()

    context = {
        "beneficiaries_num": beneficiaries_num,
        "supporter_operations_num": supporter_operations_num,
        "entities_num": entities_num
    }

    return render(request, "dashboard.html", context)


def new_dashboard(request):
    return render(request, "dashboard/dashboard2.html")


@login_required(login_url="/login")
def dashboard_requests(request):
    beneficiary_obj = beneficiary.objects.all()

    context = {
        "beneficiary_obj": beneficiary_obj,
        "beneficiaries_headers": ['رقم الملف', 'الأسم الأول', 'الأسم الأخير', 'التصنيف', 'الحالة الصحية', 'تاريخ الإرسال', 'الحالة الاجتماعية', 'مؤهل؟', 'الاجراءات'],
    }

    return render(request, "requests.html", context)


@login_required(login_url="/login")
def dashboard_reports(request):

    if request.method == "POST":

        # Get beneficiary table data (all)
        beneficiary_arr = beneficiary.objects.all()

        # Retrive form data
        beneficiary_first_name = request.POST.get("beneficiary_first_name")
        beneficiary_last_name = request.POST.get("beneficiary_last_name")
        national_id = request.POST.get("beneficiary_national_id")
        category = request.POST.get("beneficiary_category")
        marital_status = request.POST.get("beneficiary_marital_status")
        is_qualified = request.POST.get("beneficiary_is_qualified")

        # Validate query param
        if is_valid_queryparam(beneficiary_first_name, type=1):
            beneficiary_arr = beneficiary_arr.filter(
                first_name__icontains=beneficiary_first_name)

        if is_valid_queryparam(beneficiary_last_name, type=1):
            beneficiary_arr = beneficiary_arr.filter(
                last_name__icontains=beneficiary_last_name)

        if is_valid_queryparam(national_id, type=1):
            beneficiary_arr = beneficiary_arr.filter(national_id=national_id)

        if is_valid_queryparam(category, type=2):
            beneficiary_arr = beneficiary_arr.filter(category=category)

        if is_valid_queryparam(marital_status, type=2):
            beneficiary_arr = beneficiary_arr.filter(
                marital_status=marital_status)

        # Keep the original value to be sent back in the response
        is_qualified_val = is_qualified

        if is_valid_queryparam(is_qualified, type=2):
            if is_qualified == "مؤهل":
                is_qualified = True
            else:
                is_qualified = False

            beneficiary_arr = beneficiary_arr.filter(is_qualified=is_qualified)

        context = {
            "beneficiaries_headers": [
                "رقم الملف",
                "الأسم الأول",
                "الأسم الأخير",
                "رقم الهوية",
                "التصنيف",
                "الحالة الاجتماعية",
                "مؤهل؟"
            ],
            "beneficiaries": beneficiary_arr,
            "first_name": beneficiary_first_name,
            "last_name": beneficiary_last_name,
            "national_id": national_id,
            "category": category,
            "marital_status": marital_status,
            "is_qualified": is_qualified_val,
        }

        return render(request, "reports.html", context)

    else:
        return render(request, "reports.html")


@login_required(login_url="/login")
def export_excel(request):

    # Get beneficiary table data (all)
    beneficiary_arr = beneficiary.objects.all()

    # Ensure data is in the session (request.session is used to retrieve the data included in the session)
    if 'beneficiary_first_name' in request.session:
        beneficiary_first_name = request.session["beneficiary_first_name"]
    else:
        beneficiary_first_name = None

    if 'beneficiary_last_name' in request.session:
        beneficiary_last_name = request.session["beneficiary_last_name"]
    else:
        beneficiary_last_name = None

    if 'beneficiary_national_id' in request.session:
        beneficiary_national_id = request.session["beneficiary_national_id"]
    else:
        beneficiary_national_id = None

    if 'beneficiary_category' in request.session:
        beneficiary_category = request.session["beneficiary_category"]
    else:
        beneficiary_category = None

    if 'beneficiary_marital_status' in request.session:
        beneficiary_marital_status = request.session["beneficiary_marital_status"]
    else:
        beneficiary_marital_status = None

    if 'beneficiary_is_qualified' in request.session:
        beneficiary_is_qualified = request.session["beneficiary_is_qualified"]
    else:
        beneficiary_is_qualified = None

    # Validate query param
    if is_valid_queryparam(beneficiary_first_name, type=1):
        beneficiary_arr = beneficiary_arr.filter(
            first_name__icontains=beneficiary_first_name)

    if is_valid_queryparam(beneficiary_last_name, type=1):
        beneficiary_arr = beneficiary_arr.filter(
            last_name__icontains=beneficiary_last_name)

    if is_valid_queryparam(beneficiary_national_id, type=1):
        beneficiary_arr = beneficiary_arr.filter(
            national_id=beneficiary_national_id)

    if is_valid_queryparam(beneficiary_category, type=2):
        beneficiary_arr = beneficiary_arr.filter(category=beneficiary_category)

    if is_valid_queryparam(beneficiary_marital_status, type=2):
        beneficiary_arr = beneficiary_arr.filter(
            marital_status=beneficiary_marital_status)

    if is_valid_queryparam(beneficiary_is_qualified, type=2):
        if beneficiary_marital_status == "مؤهل":
            beneficiary_marital_status = True
        else:
            beneficiary_marital_status = False

        beneficiary_arr = beneficiary_arr.filter(
            is_qualified=beneficiary_marital_status)

    if beneficiary_first_name is None or beneficiary_first_name == '':
        beneficiary_first_name = "الكل"
    else:
        beneficiary_first_name = beneficiary_first_name

    if beneficiary_last_name is None or beneficiary_last_name == '':
        beneficiary_last_name = "الكل"
    else:
        beneficiary_last_name = beneficiary_last_name

    if beneficiary_national_id is None or beneficiary_national_id == '':
        beneficiary_national_id = "الكل"
    else:
        beneficiary_national_id = beneficiary_national_id

    if beneficiary_category is None or beneficiary_category == "اختار...":
        beneficiary_category = "الكل"
    else:
        beneficiary_category = beneficiary_category

    if beneficiary_marital_status is None or beneficiary_marital_status == "اختار...":
        beneficiary_marital_status = "الكل"
    else:
        beneficiary_marital_status = beneficiary_marital_status

    if beneficiary_is_qualified is None or beneficiary_is_qualified == "اختار...":
        beneficiary_is_qualified = "الكل"
    else:
        beneficiary_is_qualified = beneficiary_is_qualified

    # Let the browser know what type of file is included in the response
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    # Name the file
    response['Content-Disposition'] = 'attachment; filename="beneficiary' + \
        str(datetime.now()) + '.xlsx"'

    # Workbook object
    workbook = Workbook()

    worksheet = workbook.active

    # Merge the first six rows which indicate the type of data included
    worksheet.merge_cells('A1:H1')
    worksheet.merge_cells('A2:H2')
    worksheet.merge_cells('A3:H3')
    worksheet.merge_cells('A4:H4')
    worksheet.merge_cells('A5:H5')
    worksheet.merge_cells('A6:H6')

    # Style the first row
    first_cell = worksheet['A1']
    first_cell.value = "الأسم الأول: " + " " + beneficiary_first_name
    first_cell.fill = PatternFill("solid", fgColor="246ba1")
    first_cell.font = Font(bold=True, color="F7F6FA")
    first_cell.alignment = Alignment(horizontal="center", vertical="center")

    # Style the second row
    second_cell = worksheet['A2']
    second_cell.value = "الأسم الأخير: " + " " + beneficiary_last_name
    second_cell.font = Font(bold=True, color="246ba1")
    second_cell.alignment = Alignment(horizontal="center", vertical="center")

    # Style the third row
    second_cell = worksheet['A3']
    second_cell.value = "رقم الهوية: " + " " + beneficiary_national_id
    second_cell.font = Font(bold=True, color="246ba1")
    second_cell.alignment = Alignment(horizontal="center", vertical="center")

    # Style the forth row
    second_cell = worksheet['A4']
    second_cell.value = "التصنيف: " + " " + beneficiary_category
    second_cell.font = Font(bold=True, color="246ba1")
    second_cell.alignment = Alignment(horizontal="center", vertical="center")

    # Style the fifth row
    second_cell = worksheet['A5']
    second_cell.value = "الحالة الاجتماعية: " + " " + beneficiary_marital_status
    second_cell.font = Font(bold=True, color="246ba1")
    second_cell.alignment = Alignment(horizontal="center", vertical="center")

    # Style the sixth row
    second_cell = worksheet['A6']
    second_cell.value = "مؤهل أم لا: " + " " + beneficiary_is_qualified
    second_cell.font = Font(bold=True, color="246ba1")
    second_cell.alignment = Alignment(horizontal="center", vertical="center")

    worksheet.title = 'AA'

    # Define the titles for columns
    columns = ['#', 'رقم الملف', 'الأسم الأول',
               'الأسم الأخير', 'رقم الهوية', 'التصنيف', 'الحالة الاجتماعية', 'مؤهل؟']
    row_num = 7

    # Assign the titles for each cell of the header
    for col_num, column_title in enumerate(columns, 1):
        cell = worksheet.cell(row=row_num, column=col_num)
        cell.value = column_title
        cell.fill = PatternFill("solid", fgColor="50C878")
        cell.font = Font(bold=True, color="F7F6FA")
        seventh_cell = worksheet['H7']
        seventh_cell.alignment = Alignment(horizontal="right")

    for beneficiaries in beneficiary_arr:
        row_num += 1

        # Define the data for each cell in the row
        row = [beneficiaries.id, beneficiaries.file_no, beneficiaries.first_name,
               beneficiaries.last_name, beneficiaries.national_id, beneficiaries.category, beneficiaries.marital_status, beneficiaries.is_qualified]

        # Assign the data for each cell of the row
        for col_num, cell_value in enumerate(row, 1):
            cell = worksheet.cell(row=row_num, column=col_num)
            cell.value = cell_value
            # if isinstance(cell_value, decimal.Decimal):
            #     cell.number_format = numbers.FORMAT_NUMBER_COMMA_SEPARATED1

    workbook.save(response)
    return response
# This is for demonstration purposes only. In production, use CSRF protection.


@csrf_exempt
def beneficiary_indiv(request):

    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        # Accessing the data for beneficiary
        first_name = data.get('personalinfo_first_name', None)
        second_name = data.get('personalinfo_second_name', None)
        last_name = data.get('personalinfo_last_name', None)
        date_of_birth_data = data.get('personalinfo_date_of_birth', None)
        date_of_birth = None
        # Check if the date string exists and is not empty
        if date_of_birth_data:
            # Convert the date string to a date object
            date_of_birth = datetime.strptime(
                date_of_birth_data, '%Y-%m-%d').date()
        else:
            print("No valid date found in JSON")
        gender = data.get('personalinfo_gender', None)
        national_id = data.get('personalinfo_national_id', None)
        national_id_exp_date_data = data.get(
            'personalinfo_national_id_exp_date', None)
        national_id_exp_date = convert_to_date(
            national_id_exp_date_data)
        nationality = data.get('personalinfo_nationality', None)
        category = data.get('personalinfo_category', None)
        marital_status = data.get('personalinfo_marital_status', None)
        educational_level = data.get('personalinfo_educational_level', None)
        date_of_death_of_father_or_husband = data.get(
            'personalinfo_date_of_death_of_father_or_husband', None)
        if date_of_death_of_father_or_husband is not None:
            date_of_death_of_father_or_husband = convert_to_date(
                date_of_death_of_father_or_husband)
        washing_place = data.get('personalinfo_washing_place', None)
        health_status = data.get('personalinfo_health_status', None)
        disease_type = data.get('personalinfo_disease_type', None)
        work_status = data.get('personalinfo_work_status', None)
        employer = data.get('personalinfo_employer', None)
        phone_number = data.get('personalinfo_phone_number', None)
        email = data.get('personalinfo_email', None)
        bank_type = data.get('beneficiaryinfo_bank', None)
        bank_iban = data.get('beneficiaryinfo_iban', None)
        family_issues = data.get('familyinfo_family_issues', None)
        family_needs = data.get('familyinfo_needs_type', None)

        beneficiary_obj = beneficiary(
            first_name=first_name,
            second_name=second_name,
            last_name=last_name,
            nationality=nationality,
            gender=gender,
            date_of_birth=date_of_birth,
            phone_number=phone_number,
            email=email,
            national_id=national_id,
            national_id_exp_date=national_id_exp_date,
            category=category,
            marital_status=marital_status,
            educational_level=educational_level,
            death_date_father_husband=date_of_death_of_father_or_husband,
            washing_place=washing_place,
            health_status=health_status,
            disease_type=disease_type,
            work_status=work_status,
            employer=employer,
            bank_type=bank_type,
            bank_iban=bank_iban,
            family_issues=family_issues,
            family_needs=family_needs,
        )
        beneficiary_obj.save(category_seg="CAT", region_seg="SA")

        # Accessing the data for beneficiary_house
        building_number = data.get('houseinfo_building_number', None)
        street_name = data.get('houseinfo_street_name', None)
        neighborhood = data.get('houseinfo_neighborhood', None)
        city = data.get('houseinfo_city', None)
        postal_code = data.get('houseinfo_postal_code', None)
        additional_number = data.get('houseinfo_additional_number', None)
        unit = data.get('houseinfo_unit', None)
        location_url = data.get('houseinfo_location_url', None)
        housing_type = data.get('houseinfo_housing_type', None)
        housing_ownership = data.get('houseinfo_housing_ownership', None)

        beneficiary_house_obj = beneficiary_house(
            building_number=building_number,
            street_name=street_name,
            neighborhood=neighborhood,
            city=city,
            postal_code=postal_code,
            additional_number=additional_number,
            unit=unit,
            location_url=location_url,
            housing_type=housing_type,
            housing_ownership=housing_ownership,
            beneficiary_id=beneficiary_obj,
        )
        beneficiary_house_obj.save()

        # Accessing the data for beneficiary_income_expense
        salary_in = data.get('incomeinfo_salary', None)
        social_insurance_in = data.get('incomeinfo_social_insurance', None)
        charity_in = data.get('incomeinfo_charity', None)
        social_warranty_in = data.get('incomeinfo_social_warranty', None)
        pension_agency_in = data.get('incomeinfo_pension_agency', None)
        citizen_account_in = data.get('incomeinfo_citizen_account', None)
        benefactor_in = data.get('incomeinfo_benefactor', None)
        other_in = data.get('incomeinfo_other', None)
        housing_rent_ex = data.get('expensesinfo_housing_rent', None)
        electricity_bills_ex = data.get('expensesinfo_electricity_bills', None)
        water_bills_ex = data.get('expensesinfo_water_bills', None)
        transportation_ex = data.get('expensesinfo_transportation', None)
        health_supplies_ex = data.get('expensesinfo_health_supplies', None)
        food_supplies_ex = data.get('expensesinfo_food_supplies', None)
        educational_supplies_ex = data.get(
            'expensesinfo_educational_supplies', None)
        proven_debts_ex = data.get('expensesinfo_proven_debts', None)
        other_ex = data.get('expensesinfo_other', None)

        beneficiary_income_expense_obj = beneficiary_income_expense(
            salary_in=salary_in,
            social_insurance_in=social_insurance_in,
            charity_in=charity_in,
            social_warranty_in=social_warranty_in,
            pension_agency_in=pension_agency_in,
            citizen_account_in=citizen_account_in,
            benefactor_in=benefactor_in,
            other_in=other_in,
            housing_rent_ex=housing_rent_ex,
            electricity_bills_ex=electricity_bills_ex,
            water_bills_ex=water_bills_ex,
            transportation_ex=transportation_ex,
            health_supplies_ex=health_supplies_ex,
            food_supplies_ex=food_supplies_ex,
            educational_supplies_ex=educational_supplies_ex,
            proven_debts_ex=proven_debts_ex,
            other_ex=other_ex,
            beneficiary_id=beneficiary_obj,
        )
        beneficiary_income_expense_obj.save()

        # print("Beneficiary: ", first_name, second_name, last_name, date_of_birth, gender, national_id, national_id_exp_date, nationality, category, marital_status,
        #       educational_level, date_of_death_of_father_or_husband, washing_place, health_status, disease_type, work_status, employer, phone_number, email, bank_iban, bank_type, family_issues, family_needs)

        # print("\nBeneficiary House: ", building_number, street_name, neighborhood, city, postal_code,
        #       postal_code, additional_number, unit, location_url, housing_type, housing_ownership)

        # print("\nBeneficiary Income Expenses: ", salary_in, social_insurance_in, charity_in, social_warranty_in, pension_agency_in, citizen_account_in, benefactor_in, other_in,
        #       housing_rent_ex, electricity_bills_ex, water_bills_ex, transportation_ex, health_supplies_ex, food_supplies_ex, educational_supplies_ex, proven_debts_ex, other_ex)

        dependent_table = data.get('dependents-table', None)

        # Parse the JSON string into a Python object
        try:
            dependents_list = json.loads(dependent_table)
        except json.JSONDecodeError:
            print("Error parsing JSON")
            dependents_list = []

        # Now, you can iterate over the list of dependents
        for dep in dependents_list:
            print(dep)  # This will print each dependent as a dictionary
            # Extract the data for each field
            first_name = dep.get('firstName', '')
            second_name = dep.get('secondName', '')
            last_name = dep.get('lastName', '')
            gender = dep.get('gender', '')
            relationship = dep.get('relationship', '')
            educational_status = dep.get('educationalStatus', None)
            marital_status = dep.get('martialStatus', '')
            national_id = dep.get('nationalID', '')
            health_status = dep.get('healthStatus', None)
            income_amount = dep.get('incomeAmount', 0)
            income_source = dep.get('incomeSource', '')
            needs_type = dep.get('needsType', '')
            educational_degree = dep.get('educationalDegree', '')
            date_of_birth = dep.get('dateOfBitrh', None)
            if date_of_birth is not None:
                date_of_birth = convert_to_date(date_of_birth_data)
            national_id_exp_date = dep.get(
                'nationalIDExpDate', None)
            if national_id_exp_date is not None:
                date_of_birth = convert_to_date(national_id_exp_date)
            needs_description = dep.get('needsDescription', '')
            educational_level = dep.get('educationalLevel', None)
            disease_type = dep.get('diseaseType', None)

            # Create a new dependent object and save it to the database
            new_dependent = dependent(
                first_name=first_name,
                second_name=second_name,
                last_name=last_name,
                gender=gender,
                relationship=relationship,
                date_of_birth=date_of_birth,
                national_id=national_id,
                national_id_exp_date=national_id_exp_date,
                marital_status=marital_status,
                educational_level=educational_level,
                educational_status=educational_status,
                health_status=health_status,
                disease_type=disease_type,
                income_amount=income_amount,
                income_source=income_source,
                needs_type=needs_type,
                educational_degree=educational_degree,
                needs_description=needs_description,
                beneficiary_id=beneficiary_obj
            )
            new_dependent.save()

        # In case of successful submission and valid form data
        return JsonResponse({'redirect': '/confirmation', 'file_no': beneficiary_obj.file_no})

    elif request.method == 'GET':
        return render(request, "main/index2.html")

    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)
