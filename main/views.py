from django.shortcuts import render
from products.models import Allproduct 
# Create your views here.
def index(request):
    recent_product_list = Allproduct.objects.order_by('-pub_date')
    recomended_list = Allproduct.objects.order_by('rating')
    return render(request,'index.html',{'recent_product_list': recent_product_list,'recomended_list':recomended_list})