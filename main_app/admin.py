from django.contrib import admin

from main_app.models import User, Role, BudjetName, CategoryIncome, Currency, BillsCategory, Bill, Incomes


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['id', 'role_name']

@admin.register(BudjetName)
class BudjetNameAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'plan_costs', 'plan_incomes']

@admin.register(CategoryIncome)
class CategoryIncomeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_categoryincome', 'plan']

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_currency']

@admin.register(BillsCategory)
class BillsCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_billscategory']

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_bill', 'summ', 'date', 'bills_category']
    list_filter = ['date', 'bills_category']

@admin.register(Incomes)
class IncomesAdmin(admin.ModelAdmin):
    list_display = ['id', 'creation_date', 'name', 'summ', 'plan', 'permanent_income', 'category', 'currency', 'bill']
    list_filter = ['creation_date', 'plan', 'permanent_income', 'category', 'currency', 'bill']


admin.site.register(User)
