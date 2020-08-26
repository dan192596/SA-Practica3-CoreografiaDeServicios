from django.shortcuts import render

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

import requests

from .models import Pedido

url_base_cliente = 'http://localhost:8000'
url_base_repartidor = 'http://localhost:8001'
url_base_restaurante = 'http://localhost:8002'


# Create your views here.
class Pedido(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        cui = request.data['cui']
        pedido = request.data['pedido']
        miPedido = Pedido.objects.get(cui=cui,id=pedido)
        response = requests.post(url_base_restaurante,json={'cui':cui,'id':miPedido.id})
        return Response(status=response.status_code)