from django import views
from django.shortcuts import render
from django.db.models import Q,F
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from store.models import  Product
from store.models import Collection,OrderItem

# Create your views here.



def say_hello(request):
    
    #Products : inventory < 10 and price < 20
    
    # query_set = Product.objects.filter(inventory=F('unit_price'))
    
    # query_set = Product.objects.all()[:5]

    # query_set = Product.objects.values('id','title','collection__title')
    
    # query_set = Product.objects.filter(id__in= OrderItem.objects.values('product_id').distinct()).order_by('title')
    
    # query_set = Product.objects.only('id','title')
    
    query_set = Product.objects.defer('description')
    
    
    
    return render(request,'hello.html',{'name':'Atharva','products':list(query_set)})

