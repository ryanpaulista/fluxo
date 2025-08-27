from rest_framework import viewsets
from ..models import User
from ..serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
        Viewset para atualizar e editar usuários
        - Apenas admins podem listar todos os usuários.
        - Usuários autenticados podem ver/editar seus dados.
    """
    serializer_class = UserSerializer  # Certifique-se de criar um serializer apropriado para o modelo User

    def get_permission(self):
        """ 
            Retorna a lista de permissões que a view requer, baseado na ação (list, create, retrieve, etc.)
        """
        if self.action == 'list':
            #Ação de list (GET /api/user/) requer permissão de admin
            permissions_classes = [isAdminUser]
        else:
            #Para todas as outras ações é exido apenas estar autenticado
            permissions_classes = [IsAuthenticated]
        
        return [permission() for permission in permissions_classes]

    def get_queryset(self):
        """
            Filtra o queryset para que usuários normais vejam e editem apenas a si mesmos. Admin veem todos.
        """
        if user.is_staff:
            return User.objects.all()
        return User.objects.filter(pk=user.pk)
