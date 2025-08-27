from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        try:
            response = Response(status=status.HTTP_200_OK)
            # remove os cookies
            response.delete_cookie('access_token')
            response.delete_cookie('refresh_token')
            response.data = {'message': 'Logout bem-sucedido.'}
            return response
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            