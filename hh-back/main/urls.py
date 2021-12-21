from .views import *
from django.urls import path


app_name = "main"
urlpatterns = [
    path('', main_page, name="main_page"),
    path('companies/', companies_list, name="companies_page"),
    path('companies/<int:comp_id>/', companies_detail, name="company_page"),
    path('companies/<int:comp_id>/vacancies/', comp_vac, name="company_vacancies"),
    path('vacancies/', vac_list, name="vacancies_page"),
    path('vacancies/<int:vac_id>/', vac_detail, name="vacancy_page"),
    path('vacancies/top/', vacancies_top, name="top_vacancies_page")
]