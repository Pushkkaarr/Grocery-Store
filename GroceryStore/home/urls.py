
from django.urls import path,include
from .views import *

urlpatterns = [
   path('',home,name="home"),
   path('cart/',cart,name="cart"),
   path('checkout/',checkout,name="checkout"),
   path('store/',store,name="store"),
]