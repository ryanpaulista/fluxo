from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'catalog'

router = DefaultRouter()
router.register(prefix='products', viewset=views.ProductViewSet, basename='products')

urlpatterns = [
    
]

urlpatterns += router.urls
