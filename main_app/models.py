

import django
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings

class Role(models.Model):
    """Роли пользователей"""
    role_name = models.CharField(max_length=20, unique=True, verbose_name='Имя роли')
    description = models.TextField(null=True, blank=True, verbose_name='Описание роли')


class User(AbstractUser):
    """Пользователи"""
    surname = models.CharField(max_length=40, null=True, blank=True, verbose_name='Фамилия')
    avatar = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    phone = PhoneNumberField(null=False, blank=False, verbose_name='Номер телефона')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True, related_name='users')


class ConsultantClient(models.Model):
    """Зависимость консультант-клиент"""
    consultant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='consultants')
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='clients')

class BudjetName(models.Model):
    """Название бюджета и лимиты по нему"""
    name = models.CharField(max_length=40, unique=True, verbose_name='Наименование бюджета')
    plan_costs = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='Планируемый расход')
    plan_incomes = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='Планируемый доход')


class CategoryIncome(models.Model):
    """Категории приходов ДС"""
    name_categoryincome = models.CharField(max_length=30, unique=True, verbose_name='Наименование категории прихода ДС')
    plan = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='Планируемое значение прихода')
    description = models.TextField(null=True, blank=True, verbose_name='Описание категории')

class Currency(models.Model):
    """Валюта"""
    name_currency = models.CharField(max_length=20, unique=True, verbose_name='Наименование валюты')

class BillsCategory(models.Model):
    """Категории счетов"""
    name_billscategory = models.CharField(max_length=20, unique=True, verbose_name='Наименование категории счета')

class Bill(models.Model):
    """Счета клиента"""
    name_bill = models.CharField(max_length=20, unique=True, verbose_name='Наименование счета')
    summ = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='Начальный остаток на счете')
    description = models.TextField(null=True, blank=True, verbose_name='Описание счета')
    date = models.DateField(auto_now=True, verbose_name='Дата изменения')
    bills_category = models.ForeignKey(BillsCategory, on_delete=models.CASCADE, related_name='bills')

class Incomes(models.Model):
    """Поступление в бюджет"""
    creation_date = models.DateField(default=django.utils.timezone.now, verbose_name='Дата создания')
    name = models.CharField(max_length=30, verbose_name='Наименование поступления')
    summ = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='Сумма поступления')
    description = models.TextField(null=True, blank=True, verbose_name='Описание поступления')
    plan = models.BooleanField(default=False, verbose_name='Плановое поступление')
    permanent_income = models.BooleanField(default=False, verbose_name='Постоянный доход')
    category = models.ForeignKey(CategoryIncome, on_delete=models.CASCADE, related_name='incomes')
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='incomes', verbose_name='Валюта')
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='incomes', verbose_name='Счет')

class CategoryCost(models.Model):
    """Категории расхода ДС"""
    name_categorycost = models.CharField(max_length=30, unique=True, verbose_name='Наименование категории расхода ДС')
    plan = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='Планируемое значение расхода')
    description = models.TextField(null=True, blank=True, verbose_name='Описание категории')

class Costs(models.Model):
    """Затраты"""
    creation_date = models.DateField(default=django.utils.timezone.now, verbose_name='Дата создания')
    name = models.CharField(max_length=30, verbose_name='Наименование расхода')
    summ = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='Сумма расхода')
    description = models.TextField(null=True, blank=True, verbose_name='Описание расхода')
    plan = models.BooleanField(default=False, verbose_name='Плановый расход')
    permanent_cost = models.BooleanField(default=False, verbose_name='Постоянный расход')
    bound_cost = models.BooleanField(default=False, verbose_name='Обязательный расход')
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='costs', verbose_name='Валюта')
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='costs', verbose_name='Счет')
    category_cost = models.ForeignKey(CategoryCost, on_delete=models.CASCADE, related_name='costs')

class Budget(models.Model):
    """Бюджет"""
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budjet')
    costs = models.ForeignKey(Costs, on_delete=models.CASCADE, related_name='budjet')
    incomes = models.ForeignKey(Incomes, on_delete=models.CASCADE, related_name='budjet')
    budjetname_id = models.ForeignKey(BudjetName, on_delete=models.CASCADE, related_name='budjet')
