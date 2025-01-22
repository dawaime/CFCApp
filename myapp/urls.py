from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path(
        "403/",
        views.forbidden,
        name="403",
    ),
    path(
        "",
        views.home_redirect,
        name="index"
    ),
    path(
        "home/",
        views.home,
        name="home"
    ),
    path(
        "beneficiaries/<int:user_id>/new",
        views.beneficiary_indiv,
        name="beneficiary_new"
    ),
    path(
        "beneficiaries/<int:user_id>/edit/validate_national_id/",
        views.validate_national_id_edit_user,
        name="validate_national_id_edit_user"
    ),
    path(
        "beneficiaries/<int:user_id>/new/validate_phonenumber_beneficiary/",
        views.validate_phonenumber_new_beneficiary,
        name="validate_phonenumber_new_beneficiary"
    ),
    path(
        "beneficiary_details/<int:beneficiary_id>",
        views.beneficiary_details,
        name="beneficiary_details"
    ),
    path(
        "confirmation",
        views.confirmBeneficiaryRequestView,
        name="beneficiary_confirmation"
    ),
    path(
        "supporters/new",
        views.supporter_indiv,
        name="supporter_indiv"
    ),
    path(
        "supporters/new_request/",
        views.supporter_indiv_post,
        name="supporter_indiv_post"
    ),
    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),
    path(
        "dashboard/users/",
        views.dashboard_users,
        name="dashboard_users"
    ),
    path(
        "dashboard/users/<int:user_id>",
        views.dashboard_user_profile,
        name="dashboard_user_profile"
    ),
    path(
        "dashboard/users/<int:user_id>/delete/",
        views.dashboard_user_delete,
        name="dashboard_user_delete"
    ),
    path(
        "dashboard/users/<int:user_id>/edit/",
        views.dashboard_user_edit_basic_info,
        name="dashboard_user_edit_basic_info"
    ),
    path(
        "dashboard/users/<int:user_id>/edit_email/",
        views.dashboard_user_edit_email,
        name="dashboard_user_edit_email"
    ),
    path(
        "beneficiaries/users/<int:user_id>/edit/",
        views.beneficiary_profile_edit,
        name="beneficiary_profile_edit"
    ),
    path(
        "dashboard/users/validate_username/",
        views.dashboard_user_validate_username,
        name="dashboard_user_validate_username"
    ),
    path(
        "dashboard/users/validate_national_id/",
        views.dashboard_user_validate_national_id,
        name="dashboard_user_validate_national_id"
    ),
    path(
        "dashboard/users/validate_email/",
        views.dashboard_user_validate_email,
        name="dashboard_user_validate_email"
    ),
    path(
        "dashboard/users/<int:user_id>/edit_role/",
        views.dashboard_user_edit_role,
        name="dashboard_user_edit_role"
    ),
    path(
        "dashboard/support_operations/",
        views.dashboard_support_operations,
        name="dashboard_support_operations"
    ),
    path(
        "dashboard/support_operations/new/",
        views.dashboard_add_support_operation,
        name="dashboard_add_support_operation"
    ),
    path(
        "dashboard/field_visits/",
        views.dashboard_field_visits,
        name="dashboard_field_visits"
    ),
    path(
        "dashboard/field_visits/new/",
        views.dashboard_add_field_visit,
        name="dashboard_add_field_visit"
    ),
    path(
        "dashboard/beneficiaries/requests/",
        views.dashboard_beneficiaries_requests,
        name="dashboard_beneficiaries_requests"
    ),
    path(
        "dashboard/supporters/requests/",
        views.dashboard_supporters_requests,
        name="dashboard_supporters_requests"
    ),
    path(
        "dashboard/supporters/<int:supporter_id>/requests/<int:s_request_id>/",
        views.supporter_request_details,
        name="supporter_request_details"
    ),
    path(
        "dashboard/supporters/<int:supporter_id>/requests/<int:s_request_id>/confirm",
        views.supporter_request_confirm,
        name="supporter_request_confirm"
    ),
    path(
        "dashboard/supporters/<int:supporter_id>/requests/<int:s_request_id>/update",
        views.supporter_request_update,
        name="supporter_request_update"
    ),
    path(
        "dashboard/reports/",
        views.dashboard_reports,
        name="dashboard_generate_reports"
    ),
    path(
        "dashboard/reports/new",
        views.dashboard_reports_post,
        name="dashboard_generate_reports_post"
    ),
    path(
        'export_excel',
        views.export_excel,
        name="dashboard_generate_reports_export_excel"
    ),
    path(
        "dashboard/sponsorships/",
        views.supporter_beneficiary_sponsorship,
        name="supporter_beneficiary_sponsorship"
    ),
    path(
        "dashboard/sponsorships/new",
        views.add_sponsorship,
        name="add_sponsorship"
    ),
    path(
        "dashboard/beneficiaries/",
        views.dashboard_beneficiaries_list,
        name="beneficiaries_list"
    ),
    path(
        "dashboard/beneficiaries/<int:b_id>/",
        views.dashboard_beneficiary_details,
        name="beneficiary_details"
    ),
    path(
        "dashboard/supporters/<int:s_id>/",
        views.dashboard_supporter_details,
        name="supporter_details"
    ),
    path(
        "dashboard/supporters/",
        views.dashboard_supporters_list,
        name="supporters_list"
    ),
    path(
        'beneficiaries/<int:user_id>/',
        views.beneficiary_profile,
        name="beneficiary_profile"
    ),
    path(
        'beneficiaries/<int:user_id>/requests/',
        views.beneficiary_requests,
        name="beneficiary_requests"
    ),
    path(
        "dashboard/beneficiaries/<int:beneficiary_id>/requests/<int:b_request_id>/",
        views.dashboard_beneficiary_request_details,
        name="dashboard_beneficiary_request_details"
    ),
    path(
        "dashboard/beneficiaries/<int:beneficiary_id>/requests/<int:b_request_id>/update/",
        views.dashboard_beneficiary_request_update,
        name="dashboard_beneficiary_request_update"
    ),
    path(
        'beneficiaries/<int:user_id>/details/',
        views.beneficiary_request_details,
        name="beneficiary_request_details"
    ),
    path(
        'beneficiaries/<int:user_id>/update/',
        views.beneficiary_request_update,
        name="beneficiary_request_update"
    ),
    path(
        'beneficiaries/<int:user_id>/update/validate_national_id_dependent/',
        views.validate_national_id_dependent,
        name="validate_national_id_dependent"
    ),
    path(
        'beneficiaries/<int:user_id>/update/validate_national_id_edit_dependent/',
        views.validate_national_id_edit_dependent,
        name="validate_national_id_edit_dependent"
    ),
    path(
        'beneficiaries/<int:user_id>/update/confirm/',
        views.beneficiary_request_update_confirm,
        name="beneficiary_request_update_confirm"
    ),
    path(
        'beneficiaries/requests/confirm_message/',
        views.confirm_beneficiary_request_update,
        name="beneficiary_request_update_confirm_message"
    ),
    path(
        "sign-up/",
        views.sign_up,
        name="sign-up"
    ),
    path(
        "sign-up/new/validate_national_id/",
        views.validate_national_id_new_user,
        name="validate_national_id_new_user"
    ),
    path(
        "login/",
        views.signin,
        name="login"
    ),
    path(
        "login/by-phone-number/",
        views.phone_login_page,
        name="phone_login_page"
    ),
    path(
        "login/by-phone-number/send-otp-sms",
        views.send_otp_phone_login,
        name="send_otp_phone_login"
    ),
    path(
        "verify-otp-login/",
        views.verify_otp_login,
        name="verify_otp_login"
    ),
    path(
        "send-otp-sms/",
        views.send_otp_via_sms,
        name="send_otp_sms"
    ),
    path(
        "logout/",
        views.logout_user,
        name="logout"
    ),
    path(
        "sign-up/validate_email/",
        views.validate_email,
        name="validate_email"
    ),
    path(
        "sign-up/validate_username/",
        views.validate_username,
        name="validate_username"
    ),
    path(
        "sign-up/validate_phonenumber/",
        views.validate_phonenumber,
        name="validate_phonenumber"
    ),
    # path(
    #     "activate/<uidb64>/<token>/",
    #     views.activate,
    #     name="activate"
    # ),
    path(
        'verify-activation-otp/',
        views.verify_activation_otp_view,
        name='verify_activation_otp'
    ),
    # path(
    #     'resend-activation/',
    #     views.resend_activation_email,
    #     name='resend_activation_email'
    # ),
    path(
        'resend-activation-email/',
        views.resend_activation_email_view,
        name="resend_activation_email_view"
    ),
    path(
        'otp_sign_up_view/',
        views.otp_sign_up_view,
        name="otp_sign_up_view"
    ),
    path(
        'password_reset/',
        views.password_reset_request,
        name="password_reset"
    ),
    path(
        'password_reset/done/',
        views.password_reset_done,
        name="password_reset_done"
    ),
    path(
        'password_reset_confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name="auth/password_reset_confirm.html"),
        name="password_reset_confirm"
    ),
    path(
        'password_reset/complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name="auth/password_reset_complete.html"),
        name="password_reset_complete"
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
