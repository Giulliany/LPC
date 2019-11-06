from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('inicio/', inicio, name='inicio'),
    path('publicar/', PublicacaoView.as_view(), name='publicar'),
    path('perfil/<str:nome>/', perfil, name='publicar'),
    path('seguir/<int:id_pessoa>', seguir, name='seguir'),
    path('comentario', comentario, name='comentario'),
]