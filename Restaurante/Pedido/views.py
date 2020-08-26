from django.shortcuts import render

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

import requests

from .models import Pedido

host = '192.168.142.145'

url_base_cliente = 'http://'+host+':8000/'
url_base_repartidor = 'http://'+host+':8001/'
url_base_restarurante = 'http://'+host+':8002/'


# Create your views here.
class PedidoView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        cui = request.data['cui']        
        miPedido = Pedido.objects.create(cui=cui)
        print("El restaurante recibio del cliente "+str(cui)+" el pedido "+str(miPedido.id))
        return Response({"pedido":miPedido.id}, status=status.HTTP_200_OK)

    def get(self, request):
        params = self.request.query_params
        cui = params['cui']
        pedido = params['pedido']
        miPedido = Pedido.objects.get(cui=cui, id=pedido)
        print("Se hizo la consulta del pedido "+str(pedido)+ " y es "+str(miPedido.status))
        return Response({"status":miPedido.status}, status=status.HTTP_200_OK)