from django.urls import path
from .views import *
from django.urls import path
from . import views as core_views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('inicio/', inicio, name='inicio'),
    path('perfil/<str:nome>/', perfil, name='perfil'),
    path('pub/<int:public_id>/', core_views.pubs_detail, name = 'detalhe'),
    path('comentario', comentario, name='comentario'),
    path('publicar/', PublicacaoView.as_view(), name='publicar'),

]