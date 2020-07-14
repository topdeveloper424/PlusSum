from django.db import models

# Create your models here.
class IncomeStatement(models.Model):
    SALES = 'S'
    PROFIT = 'P'
    ITEM_CHOICES = (
        (SALES, 'Sales'),
        (PROFIT,'Profit'),
    )
    
    company = models.CharField(max_length=150,null = False, default='')
    item = models.CharField(max_length = 2, choices = ITEM_CHOICES, default = SALES)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=14, decimal_places=4, null=True, default=None)

class BudgetStatement(models.Model):
    ASSET = 'A'
    LOAN = 'L'
    ITEM_CHOICES = (
        (ASSET, 'Asset'),
        (LOAN,'Loan'),
    )
    
    company = models.CharField(max_length=150,null = False, default='')
    item = models.CharField(max_length = 2, choices = ITEM_CHOICES, default = ASSET)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=14, decimal_places=4, null=True, default=None)
    