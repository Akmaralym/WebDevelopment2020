from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'companies', views.CompanyViewSet)
router.register(r'vacancies', views.VacancyViewSet)

urlpatterns = [
    url(r'^users/', views.users, name='users'),
    url(r'^login/', obtain_jwt_token),
]

urlpatterns += router.urls
