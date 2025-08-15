from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'catalog'

router = DefaultRouter()
router.register(prefix='', viewset=views.ProductViewSet, basename='product')

urlpatterns = [
    
]

urlpatterns += router.urls
