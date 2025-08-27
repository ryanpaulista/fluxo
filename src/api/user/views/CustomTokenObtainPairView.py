from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200: #SUCESSO
            refresh_token = response.data.get('refresh')

            if refresh_token:
                response.set_cookie(
                    key='refresh_token',
                    value=refresh_token,
                    httponly=True, #Impede o acesso via javascript
                    samesite='Lax',
                    #secure=True, #Usar True em produção - Requer HTTPS
                )
                #Opcional deletar os token do corpo da resposta

            #remove o refresh do corpo da resposta
            if 'refresh' in response.data:
                del response.data['refresh']

            # O access token permanece no corpo da resposta para o frontend usar
        return response
