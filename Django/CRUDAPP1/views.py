from django.shortcuts import render,redirect
from .forms import *
from .models import *

def homepage(request):

    return render(request,'home.html')

def aboutpage(request):

    return render(request,'about.html')

def servicespage(request):

    return render(request,'services.html')

def contactpage(request):

    return render(request,'contact.html')

def Addproduct(request):
    context={
        'product_form':product_form()
    }
    
    if request.method == 'POST':
        
       #print(request.POST) stored value to database in terminal print
       product_details = product_form(request.POST)
       
       if product_details.is_valid():
           product_details.save()
    
    return render(request,'add_product.html',context)  #add product class function

def displaypage(request):
    
    context={
        'display_product': product.objects.all()
    }

    return render(request,'display.html',context) #display all data class function

def DeleteButton(request,id):
    
    select_data = product.objects.get(id = id)
    select_data.delete()
    return redirect('/CRUDAPP1/display/')    #delete data class function

def UpdateButton(request,id):
    
    select_data = product.objects.get(id = id)
    
    context={
        'product_form':product_form(instance=select_data)
    }
    
    if request.method == 'POST':
        
       #print(request.POST) stored value to database in terminal print
       product_details = product_form(request.POST,instance=select_data)
       
       if product_details.is_valid():
           product_details.save()
           
           return redirect('/CRUDAPP1/display/')
    
    return render(request,'add_product.html',context)
    
    