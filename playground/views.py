from django import views
from django.shortcuts import render
from django.db.models import Q,F
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from store.models import  Product,Order
from store.models import Collection,OrderItem

# Create your views here.



def say_hello(request):
    
    #Products : inventory < 10 and price < 20
    
    # query_set = Product.objects.filter(inventory=F('unit_price'))
    
    # query_set = Product.objects.all()[:5]

    # query_set = Product.objects.values('id','title','collection__title')
    
    # query_set = Product.objects.filter(id__in= OrderItem.objects.values('product_id').distinct()).order_by('title')
    
    # query_set = Product.objects.only('id','title')
    
    # query_set = Product.objects.defer('description')
    
    # Select Related
    # query_set = Product.objects.select_related('collection').all()
    
    #Prefetech_realted (n)
    # query_set = Product.objects.prefetch_related('promotions').select_related('collection').all()
    
    
    query_set = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    
    
    
    
    return render(request,'hello.html',{'name':'Atharva','orders':list(query_set)})

