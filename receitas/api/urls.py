from django.urls import path

# para selecionar todas as views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('receita/', views.receita, name='receita')
]