from django.shortcuts import render

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

import requests

from Pedido.models import Pedido

host = '192.168.142.145'

url_base_esb = 'http://'+host+':8004/'


# Create your views here.
class PedidoView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        miPedido = Pedido.objects.get(cui=request.data['cui'],id=request.data['pedido'])
        response = requests.post(url_base_esb+'api/v1/repartidor/pedido',json={'cui':request.data['cui'],'id':miPedido.id})
        if response.status_code==200:
            miPedido.status = 1
            miPedido.save()
            print("El restaurante notifico al repartidor del pedido "+str(miPedido.id))
        return Response(status=response.status_code)