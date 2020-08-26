from django.shortcuts import render

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

import requests

from Pedido.models import Pedido

host = '192.168.142.145'

url_base_cliente = 'http://'+host+':8000/'
url_base_repartidor = 'http://'+host+':8001/'
url_base_restarurante = 'http://'+host+':8002/'


# Create your views here.
class PedidoView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        cui = request.data['cui']
        pedido = request.data['pedido']
        miPedido = Pedido.objects.get(cui=cui,id=pedido)
        response = requests.post(url_base_repartidor+'api/v1/pedido',json={'cui':cui,'id':miPedido.id})
        if response.status_code==200:
            miPedido.status = 1
            miPedido.save()
        return Response(status=response.status_code)