from django.shortcuts import render

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

import requests


host = '192.168.142.145'

url_base_repartidor = 'http://'+host+':8001/'

# Create your views here.
class PedidoView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        response = requests.post(url_base_repartidor+'api/v1/pedido',json={'cui':request.data['cui'],'id':request.data['id']})
        print("ESB: El restaurante notifico al repartidor del pedido "+str(request.data['id']))
        return Response(status=response.status_code)