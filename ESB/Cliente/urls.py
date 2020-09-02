from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from .views import Pedido

urlpatterns = [
    path('pedido', Pedido.as_view(), name='pedido'),    
]