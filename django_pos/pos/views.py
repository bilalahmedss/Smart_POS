import json
from datetime import date
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, FloatField, F
from django.db.models.functions import Coalesce
from django.shortcuts import render, redirect
from products.models import Product, Category
from sales.models import Sale
from django.http import HttpResponse


@login_required(login_url="/accounts/login/")
def index(request):
    return redirect("/sales/")

@login_required(login_url="/accounts/login/")
def dashboard(request):
    return HttpResponse("<h1>Dashboard is under process</h1>")
