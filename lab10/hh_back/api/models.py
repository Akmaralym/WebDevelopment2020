from django.db import models


# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    city = models.CharField(max_length=100, verbose_name='Город')
    address = models.TextField(verbose_name='Адрес', blank=True, null=True)

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Vacancy(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    salary = models.FloatField(verbose_name='Зарплата')
    company = models.ForeignKey(Company, related_name='vacancies', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
