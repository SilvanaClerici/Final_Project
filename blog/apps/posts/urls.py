from django.urls import path
from .views import *

urlpatterns = [
    path('', PaginaPrincipalArticulos.as_view(), name='index')
]
