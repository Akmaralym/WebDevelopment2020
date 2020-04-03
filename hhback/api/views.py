from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from api.models import Company, Vacancy
def list_of_companies(request):
    company_list = Company.objects.all()
    result = [company.to_json() for company in company_list]
    return JsonResponse(result, safe=False)

def get_one_company(request, id):
    company = Company.objects.get(id=id)
    result = company.to_json()
    return JsonResponse(result, safe=False)

def vacancies_of_company(request, id):
    company = Company.objects.get(id=id)
    vacancies = company.vacancy_set.all()
    result = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(result, safe=False)

def list_of_vacancies(request):
    vacancies = Vacancy.objects.all()
    result = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(result, safe=False)

def get_one_vacancy(request, id):
    vacancy = Vacancy.objects.get(id=id)
    result = vacancy.to_json()
    return JsonResponse(result, safe=False)

def list_of_top_vacancies(request):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    result = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(result, safe=False)
