from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from .views import PedidoView

urlpatterns = [
    path('', PedidoView.as_view(), name='pedido'),    
]