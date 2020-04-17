from django.urls import path
from api import views


urlpatterns = [
    path('companies/', views.list_of_companies),
    path('companies/<int:id>/', views.get_one_company),
    path('companies/<int:id>/vacancies/', views.vacancies_of_company),
    path('vacancies/', views.list_of_vacancies),
    path('vacancies/<int:id>/', views.get_one_vacancy),
    path('vacancies/top_ten/', views.list_of_top_vacancies),

]