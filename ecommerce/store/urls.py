from django.urls import path 
from . import views # . means from this directory 


urlpatterns = [
    path('',views.store,  name='store'), #dynamic name
    path('cart/',views.cart,  name='cart'),
    path('checkout/',views.checkout,  name='checkout'),
    
    
]
