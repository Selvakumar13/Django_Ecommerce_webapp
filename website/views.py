from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from .forms import *
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
import json
from django.core import serializers
import openpyxl
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font
from django.http import HttpResponse
import json
import io
import xlsxwriter

@csrf_protect
def home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'website/home.html', context)

def placeOrder(request, i):
    customer = Customer.objects.get(id=i)
    form = createorderform(instance=customer,)
    if request.method == 'POST':
        form = createorderform(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'website/placeOrder.html', context)

def addProduct(request):
    form = createproductform()
    if request.method == 'POST':
        form = createproductform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'website/addProduct.html', context)

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = createuserform()
        customerform = createcustomerform()
        if request.method == 'POST':
            form = createuserform(request.POST)
            customerform = createcustomerform(request.POST)
            if form.is_valid() and customerform.is_valid():
                user = form.save()
                customer = customerform.save(commit=False)
                customer.user = user
                customer.save()
                return redirect('login')
        context = {
            'form': form,
            'customerform': customerform,
        }
        return render(request, 'website/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        context = {}
        return render(request, 'website/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')

def get_products(request):
    products = Product.objects.all()
    product_list = []

    for product in products:
        product_dict = {
            'image_of_product': product.image_of_product.url,
            'product_name': product.product_name,
            'get_product_type_display': product.get_product_type_display(),
            'price': product.price,
            'get_category_display': product.get_category_display(),
            'description': product.description,
            'expiry_date': product.expiry_date,
        }
        product_list.append(product_dict)

    return JsonResponse(product_list, safe=False)

