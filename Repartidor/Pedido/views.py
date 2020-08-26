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
url_base_restaurante = 'http://'+host+':8002/'


# Create your views here.
class PedidoView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        cui = request.data['cui']
        id = request.data['id']
        Pedido.objects.create(cui=cui,pedido=id)
        print("Se recibio el pedido "+str(id)+" del cliente "+str(cui))
        return Response(status=status.HTTP_200_OK)

    def get(self, request):
        params = self.request.query_params
        cui = params['cui']
        pedido = params['pedido']
        miPedido = Pedido.objects.get(cui=cui, pedido=pedido)
        print("Se consulto el pedido "+str(pedido)+" del cliente "+str(cui))
        return Response({"status":miPedido.status}, status=status.HTTP_200_OK)
    
    def patch(self, request):
        miPedido = Pedido.objects.get(pedido=request.data['pedido'])
        miPedido.status = request.data['status']
        miPedido.save()
        print("Se actualizo el estado del pedido "+str(request.data['pedido'])+" a "+str(request.data['status']))
        return Response({"pedido":miPedido.pedido,"status":miPedido.status}, status=status.HTTP_200_OK)