from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from .views import PedidoView

urlpatterns = [
    path('pedido', PedidoView.as_view(), name='notificar_pedido'),
]