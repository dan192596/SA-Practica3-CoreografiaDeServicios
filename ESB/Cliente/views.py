from django.shortcuts import render

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

import requests

host = '192.168.142.145'

url_base_repartidor = 'http://'+host+':8001/'
url_base_restarurante = 'http://'+host+':8002/'

# Create your views here.
class Pedido(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        response = requests.post(url_base_restarurante+'api/v1/pedido', json={'cui':request.data['cui']},verify=False)
        print("El cliente "+str(request.data['cui'])+" solicito el pedido: "+str(response.json()['pedido']))
        return Response({"cui":request.data['cui'],"pedido":response.json()['pedido']}, status=status.HTTP_200_OK)

    def get(self, request):
        params = self.request.query_params
        miStatus = 0
        if params['ubicacion'] =='restaurante':
            response = requests.get(url_base_restarurante+'api/v1/pedido', params={'cui':params['cui'], 'pedido':params['pedido']})
            miStatus = response.json()['status']
        elif params['ubicacion'] =='repartidor':
            response = requests.get(url_base_repartidor+'api/v1/pedido', params={'cui':params['cui'], 'pedido':params['pedido']})
            miStatus = response.json()['status']
        print("El estatus en "+str(params['ubicacion'])+" del pedido "+str(params['pedido'])+ ' es '+str(miStatus))
        return Response({"status":miStatus}, status=status.HTTP_200_OK)