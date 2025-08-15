from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Product
from ..serializers import ProductSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #permissions_classes = []
""" 
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            # Para metodos de criação, atualização ou exclusão
            # O usuário precisa ser um administrador
            permissions_classes = [IsAdminUser]
        else:
            # Para metodos de listagem ('list') ou ver detalhes ('retrieve')
            # O usuário precisa ser somente autenticado
            permissions_classes = [IsAuthenticated]
"""
    
