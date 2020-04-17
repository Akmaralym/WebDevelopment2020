import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated

from .models import Vacancy, Company
from .serializers import CompanySerializer, VacancyFullSerializer, VacancyShortSerializer, CompanyCreateSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from utils.permissions import CompanyPermission


# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [CompanyPermission]

    def get_serializer_class(self):
        if self.action == 'create':
            return CompanyCreateSerializer
        return self.serializer_class

    @action(methods=['get'], detail=True)
    def vacancies(self, request, *args, **kwargs):
        serializer = VacancyShortSerializer(Vacancy.objects.filter(company=self.get_object()), many=True)
        return Response(serializer.data)


class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyFullSerializer

    @action(methods=['get'], detail=False)
    def top_ten(self, request):
        top_ten = self.get_queryset().order_by('-salary')[:10]
        serializer = VacancyFullSerializer(top_ten, many=True)
        return Response(serializer.data)


def users(request):
    if request.method == 'GET':
        user_list = User.objects.all()
        res = {
            'users': {}
        }
        for user in user_list:
            res['users'][user.username] = {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'username': user.username
            }
        return JsonResponse(res)
