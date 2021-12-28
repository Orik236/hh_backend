from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

app_name = "main"
urlpatterns = [
    path('', main_page, name="main_page"),
    path('companies/', companies_list, name="companies_page"),
    path('companies/<int:comp_id>/', company_detail_page, name="company_detail"),
    path('vacancies/', vacancies_list, name="vacancies_page"),
    path('vacancies/<int:vac_id>/', vacancy_detail, name="vacancy_detail"),
    path('resumes/', resumes_list, name="resumes_page")
] + static(settings.MEDIA_URL, document_roo=settings.MEDIA_ROOT)
