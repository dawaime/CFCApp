from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("todos/", views.todos, name="Todos"),
    path("name/", views.get_name, name="action"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("index/", views.test1, name="index"),
    path("beneficiaries/individuals/new", views.beneficiary_indiv, name="post_beneficiary"),
    path("supporters/entities/new", views.supporter_entity, name="supporter_entity"),
    path("supporters/individuals/new", views.supporter_indiv, name="supporter_indiv"),
    path("dashboard/requests", views.dashboard_requests, name="requests"),
]
