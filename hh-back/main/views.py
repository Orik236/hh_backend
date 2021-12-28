from django.http.response import JsonResponse, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import VacancyForm
from .models import *


def main_page(request):
    return HttpResponsePermanentRedirect("/main/vacancies/")


def authorize(request):
    return render(request, "main/auth.html", {})


def companies_list(request):
    companies = Company.objects.all()
    return render(request, "main/companies_index.html", {'companies': companies})


def company_detail_page(request, comp_id):
    try:
        company = Company.objects.get(id=comp_id)
        vacancies = Vacancy.objects.filter(company__pk=comp_id)
        if request.method == 'POST':
            d = {
                'name': request.POST['name'],
                'description': request.POST['description'],
                'salary': request.POST['salary'],
                'company': company
            }
            vacancy_form = VacancyForm(d)
            if vacancy_form.is_valid():
                vacancy_form.save()
            return redirect(reverse('main:company_detail', args=(comp_id,)))
    except Company.DoesNotExist as e:
        return JsonResponse({'Error': str(e)})
    return render(request, "main/company_detail.html", {'company': company, 'vacancies': vacancies})


def vacancies_list(request):
    vacancies = Vacancy.objects.all()
    return render(request, "main/vacancies_index.html", {'vacancies': vacancies})


def vacancy_detail(request, vac_id):
    try:
        vacancy = Vacancy.objects.get(id=vac_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return render(request, 'main/vacancy_detail.html', {'vacancy': vacancy})


def resumes_list(request):
    resumes = Resumes.objects.all()
    return render(request, "main/resumes_index.html", {'resumes': resumes})


def resume_detail(request, res_id):
    try:
        resume = Resumes.objects.get(id=res_id)
    except Resumes.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return render(request, 'main/resume_detail.html', {'resume': resume})