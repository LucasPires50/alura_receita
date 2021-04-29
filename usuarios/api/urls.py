from django.urls import path

# para selecionar todas as views
from . import views

urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('cria/receita', views.cria_receita, name='cria_receita'),
    path('edita/<int:receita_id>', views.edita_receita, name='edita_receita'),
    path('deleta/<int:receita_id>', views.deleta_receita, name='deleta_receita'),
]