from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.allProducts,name='AllProducts' ),
    path('<int:id>/', views.productLanding ,name='detail')
] 