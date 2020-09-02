from django.shortcuts import render

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

import requests

host = '192.168.142.145'

url_base_esb = 'http://'+host+':8004/'


# Create your views here.
class Pedido(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        response = requests.post(url_base_esb+'api/v1/cliente/pedido', json={'cui':request.data['cui']},verify=False)
        print("ESB: El cliente "+str(request.data['cui'])+" solicito el pedido: "+str(response.json()['pedido']))
        return Response({"cui":request.data['cui'],"pedido":response.json()['pedido']}, status=status.HTTP_200_OK)

    def get(self, request):
        params = self.request.query_params
        response = requests.get(url_base_esb+'api/v1/cliente/pedido', params={'cui':params['cui'], 'pedido':params['pedido'],'ubicacion':params['ubicacion']})
        print("El estatus en "+str(params['ubicacion'])+" del pedido "+str(params['pedido'])+ ' es '+str(response.json()['status']))
        return Response({"status":response.json()['status']}, status=status.HTTP_200_OK)