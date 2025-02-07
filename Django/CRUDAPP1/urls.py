from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('home/',homepage),
    path('about/',aboutpage),
    path('services/',servicespage),
    path('contact/',contactpage),
    path('add_product/',Addproduct),
    path('display/',displaypage),
    path('deleteproduct/<int:id>',DeleteButton,name='deleteproduct'),
    path('updateproduct/<int:id>',UpdateButton,name='updateproduct'),
]
