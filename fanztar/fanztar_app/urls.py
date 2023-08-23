from django.urls import path
from .views import order_api

urlpatterns = [
    path('orders/', order_api, name='create-order'),
]
