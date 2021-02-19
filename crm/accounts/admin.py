from django.contrib import admin

#from .models import *
from . models import Customer, Order, Product, Info

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Info)
