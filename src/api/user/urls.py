from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'user'

router = DefaultRouter()
router.register(prefix='' ,viewset=views.UserViewSet, basename='user')

urlpatterns = [
    
]

urlpatterns += router.urls