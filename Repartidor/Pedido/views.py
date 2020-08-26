from django.shortcuts import render

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

import requests

from .models import Pedido

url_base_cliente = 'http://localhost:8000'
url_base_repartidor = 'http://localhost:8001'
url_base_restarurante = 'http://localhost:8002'


# Create your views here.
class Pedido(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        cui = request.data['cui']
        id = request.data['id']
        Pedido.objects.create(cui=cui,pedido=id)
        return Response(status=status.HTTP_200_OK)

    def get(self, request):
        params = self.request.query_params
        cui = params['cui']
        pedido = params['pedido']
        miPedido = Pedido.objects.get(cui=cui, pedido=pedido)
        return Response({"status":miPedido.status}, status=status.HTTP_200_OK)
    
    def patch(self, request, pk):
        miPedido = Pedido.objects.get(pedido=request.data['pedido'])
        miPedido.status = request.data['status']
        miPedido.save()
        return Response({"pedido":miPedido.pedido,"status":miPedido.status}, status=status.HTTP_200_OK)