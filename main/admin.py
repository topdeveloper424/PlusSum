from django.contrib import admin
from main.models import IncomeStatement, BudgetStatement

# Register your models here.

admin.site.register(IncomeStatement)
admin.site.register(BudgetStatement)
