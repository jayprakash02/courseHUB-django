from django.shortcuts import render
from .models import Allproduct
# Create your views here.
def allProducts(request):
    product_list = Allproduct.objects.all()        
    return render(request,'allproduct.html',{'product_list':product_list})

def productLanding(request,id):
    product = Allproduct.objects.all()
    return render(request,'landingpage.html',{'id': id,'product':product })