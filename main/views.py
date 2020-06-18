from django.shortcuts import render
from products.models import Allproduct 
# Create your views here.
def index(request):
    product_list = Allproduct.objects.all()
    return render(request,'index.html',{'product_list':product_list})