#class user
from rest_framework.serializers import ModelSerializer
from .models import User
#class TokenRefresh
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.exceptions import InvalidToken

class UserSerializer(ModelSerializer):
    """
    Serializer para o modelo User.
    """
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        read_only_fields = ['id']  # Campos que não podem ser modificados diretamente
        # Se necessário, você pode adicionar outros campos ou métodos de validação aqui
    
class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    def validate (self, attrs):
        #Pega o refresh no cookie da requisição
        refresh_token = self.context['request'].COOKIES.get('refresh_token')
        
        if not refresh_token:
            raise InvalidToken('Nenhum token encontrado no cookie')
        
        attrs['refresh'] = refresh_token
        return super().validate(attrs)