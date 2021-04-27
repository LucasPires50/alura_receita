from django.urls import path

# para selecionar todas as views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:receita_id>/', views.receita, name='receita'),
    path('buscar', views.buscar, name='buscar')
]