from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Product.
    """
    class Meta:
        model = Product
        #Atributos que serão exibidos no serializer
        fields = ['id', 'name', 'description', 'price', 'stock']
        read_only_fields = ['id']
        #exclude = ['created_at', 'updated_at']  # Exemplo de como excluir campos, se necessário
        #fields = '__all__'  # Se quiser incluir todos os campos do modelo