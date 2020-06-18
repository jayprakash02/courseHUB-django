from django.shortcuts import render
from .models import Allproduct
# Create your views here.
def allProducts(request):
    product_list = Allproduct.objects.all()        
    return render(request,'product.html',{'product_list':product_list})