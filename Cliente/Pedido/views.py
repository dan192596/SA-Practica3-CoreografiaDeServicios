from django.shortcuts import render

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

import requests

url_base_repartidor = 'http://localhost:8001'
url_base_restarurante = 'http://localhost:8002'


# Create your views here.
class Pedido(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        cui = request.data['cui']
        id = request.data['id']
        return Response({"cui":cui,"id":id}, status=status.HTTP_200_OK)

    def get(self, request):
        params = self.request.query_params
        status = 0
        if params['ubicacion'] =='restaurante':
            response = requests.get(url_base_restarurante)
            status = response.json()['status']
        elif params['ubicacion'] =='repartidor':
            response = requests.get(url_base_repartidor)
            status = response.json()['status']
        return Response({"status":status}, status=status.HTTP_200_OK)