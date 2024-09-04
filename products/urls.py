from django.urls import path
from .views import ProductAPIView

urlpatterns = [
    path('api/products/', ProductAPIView.as_view(), name='product-list-create'), 
    path('api/products/<int:pk>/', ProductAPIView.as_view(), name='product-detail'),  
]
