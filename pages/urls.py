from django.urls import path
from .views      import *

urlpatterns = [
    path('', home),
    path('product', product),
    path('login',loginSystem),
]
