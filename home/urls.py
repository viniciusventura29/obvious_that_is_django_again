from unicodedata import name
from . import views
from django.urls import path


urlpatterns = [
    path('',views.home_index,name='homeindex'),
    path('cadastro/',views.usuario_cadastro,name='usuario_cadastro'),
    path('login/',views.usuario_login,name='usuario_login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('sair',views.sair,name='sair'),
]
