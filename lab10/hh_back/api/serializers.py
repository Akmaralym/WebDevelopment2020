from rest_framework import serializers
from .models import Company, Vacancy


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class VacancyShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        exclude = ('company',)


class VacancyFullSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = Vacancy
        fields = '__all__'


class CompanyCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=100)
    address = serializers.CharField(required=False)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.city = validated_data.get('city', instance.city)
        instance.address = validated_data.get('address', instance.address)
        return instance

    def create(self, validated_data):
        company = Company.objects.create(**validated_data)
        return company


