from django.urls import path, include
from .views import HomeFilmes, Homepage, Detalhesfilme, PesquisaFilme

app_name = 'filme'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('filmes/', HomeFilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', Detalhesfilme.as_view(), name='detalhesfilme'),
    path('pesquisa/', PesquisaFilme.as_view(), name='pesquisafilme')
]