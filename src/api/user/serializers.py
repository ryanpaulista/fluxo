from rest_framework.serializers import ModelSerializer
from .models import User

class UserSerializer(ModelSerializer):
    """
    Serializer para o modelo User.
    """
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        read_only_fields = ['id']  # Campos que não podem ser modificados diretamente
        # Se necessário, você pode adicionar outros campos ou métodos de validação aqui