from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from .models import IncomeStatement, BudgetStatement
from django.db.models import Sum
import pandas as pd
import random
import json

def home(request):
    statements_obj = IncomeStatement.objects 
    company_choices = statements_obj.order_by().values('company').distinct()
    year_choices = statements_obj.order_by().values('year').distinct()
    # qs = statements_obj.all().values()
    # data = pd.DataFrame(qs)
    # print(data)
    context = {
        'company_choices':company_choices,
        'year_choices':year_choices
    }
    return render(request,'home.html',context)

''' calculate by company and year'''
def calc_fuc(company, year):
    income_obj = IncomeStatement.objects.all().values()
    budget_obj = BudgetStatement.objects.all().values()
    incom_df = pd.DataFrame(income_obj)
    budget_df = pd.DataFrame(budget_obj)
    
    profit = incom_df.where(incom_df['company']==company).where(incom_df['year']==year).where(incom_df['item']=='P').dropna()['price'].sum()
    sales = incom_df.where(incom_df['company']==company).where(incom_df['year']==year).where(incom_df['item']=='S').dropna()['price'].sum()
    asset = budget_df.where(budget_df['company']==company).where(budget_df['year']==year).where(budget_df['item']=='A').dropna()['price'].sum()
    loan = budget_df.where(budget_df['company']==company).where(budget_df['year']==year).where(budget_df['item']=='L').dropna()['price'].sum()

    ##### PS = Profit / Sales ##########
    ps = None
    if sales != 0 and sales != None:
        ps = round(profit/sales,2)
    print(ps)

    ##### LA = Loan / Asset ##########
    la = None
    if asset != 0 and asset != None:
        la = round(loan/asset, 2)
    print(la)

    ##### PL = Profit / Loan  ##########
    pl = None
    if loan != 0 and loan != None:
        pl = round(profit/loan, 2)
    print(pl)

    ##### SA = Sales / Asset  ##########
    sa = None
    if asset != 0 and asset != None:
        sa = round(sales/asset, 2)
    print(sa)
    
    return [ps, la, pl, sa]
    
''' calculate by year'''
def calc_years_fuc(company):
    income_obj = IncomeStatement.objects.all().values()
    budget_obj = BudgetStatement.objects.all().values()
    incom_df = pd.DataFrame(income_obj)
    budget_df = pd.DataFrame(budget_obj)
    calc_array = []
    year_choices = IncomeStatement.objects.order_by().values('year').distinct()
    for year_choice in year_choices:
        profit = incom_df.where(incom_df['company']==company).where(incom_df['year']==year_choice['year']).where(incom_df['item']=='P').dropna()['price'].sum()
        sales = incom_df.where(incom_df['company']==company).where(incom_df['year']==year_choice['year']).where(incom_df['item']=='S').dropna()['price'].sum()
        asset = budget_df.where(budget_df['company']==company).where(budget_df['year']==year_choice['year']).where(budget_df['item']=='A').dropna()['price'].sum()
        loan = budget_df.where(budget_df['company']==company).where(budget_df['year']==year_choice['year']).where(budget_df['item']=='L').dropna()['price'].sum()
        ##### PS = Profit / Sales ##########
        ps = None
        if sales != 0 and sales != None:
            ps = round(profit/sales,2)
        print(ps)

        ##### LA = Loan / Asset ##########
        la = None
        if asset != 0 and asset != None:
            la = round(loan/asset, 2)
        print(la)

        ##### PL = Profit / Loan  ##########
        pl = None
        if loan != 0 and loan != None:
            pl = round(profit/loan, 2)
        print(pl)

        ##### SA = Sales / Asset  ##########
        sa = None
        if asset != 0 and asset != None:
            sa = round(sales/asset, 2)
        print(sa)
        
        calc_array.append({'year':year_choice['year'],'calc':[ps, la, pl, sa]})
        
    return calc_array

''' calculate by company'''
def calc_company_fuc(year):
    income_obj = IncomeStatement.objects.all().values()
    budget_obj = BudgetStatement.objects.all().values()
    incom_df = pd.DataFrame(income_obj)
    budget_df = pd.DataFrame(budget_obj)
    calc_array = []
    company_choices = IncomeStatement.objects.order_by().values('company').distinct()
    for company_choice in company_choices:
        profit = incom_df.where(incom_df['company']==company_choice['company']).where(incom_df['year']==year).where(incom_df['item']=='P').dropna()['price'].sum()
        sales = incom_df.where(incom_df['company']==company_choice['company']).where(incom_df['year']==year).where(incom_df['item']=='S').dropna()['price'].sum()
        asset = budget_df.where(budget_df['company']==company_choice['company']).where(budget_df['year']==year).where(budget_df['item']=='A').dropna()['price'].sum()
        loan = budget_df.where(budget_df['company']==company_choice['company']).where(budget_df['year']==year).where(budget_df['item']=='L').dropna()['price'].sum()
        ##### PS = Profit / Sales ##########
        ps = None
        if sales != 0 and sales != None:
            ps = round(profit/sales,2)
        print(ps)

        ##### LA = Loan / Asset ##########
        la = None
        if asset != 0 and asset != None:
            la = round(loan/asset, 2)
        print(la)

        ##### PL = Profit / Loan  ##########
        pl = None
        if loan != 0 and loan != None:
            pl = round(profit/loan, 2)
        print(pl)

        ##### SA = Sales / Asset  ##########
        sa = None
        if asset != 0 and asset != None:
            sa = round(sales/asset, 2)
        print(sa)
        
        calc_array.append({'company':company_choice['company'],'calc':[ps, la, pl, sa]})
        
    return calc_array
''' getting data for displaying graphs'''
def get_graph_data(request):
    company = request.GET['company']
    year = int(request.GET['year'])
    spyder_calc_list = calc_fuc(company, year)
    year_calc_list = calc_years_fuc(company)
    company_calc_list = calc_company_fuc(year)
    
    return JsonResponse({'spyder':spyder_calc_list, 'yearly':year_calc_list, 'company':company_calc_list}, safe=False)
    

''' generating fake data into 2 tables'''
def generate_fake(request):
    IncomeStatement.objects.all().delete()
    BudgetStatement.objects.all().delete()
    years = [2017, 2018, 2019, 2020]
    items1 = ['S','P']
    companies = ['A','B','C','D','E','F']
    prices = [None, -9, -8, -7, -6, -5, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25,30, 35, 40, 45, 50, 60]
    for company in companies:
        for year in years:
            for item in items1:
                price = random.choice(prices)
                income = IncomeStatement(company=company, item=item, year= year, price=price)
                income.save()
    items2 = ['A','L']
    for company in companies:
        for year in years:
            for item in items2:
                price = random.choice(prices)
                budget = BudgetStatement(company=company, item=item, year= year, price=price)
                budget.save()

    response = {}
    response['status'] = 'success'
                
    return HttpResponse(json.dumps(response),content_type="application/json")
    
                
    