from django.urls import path
from . import views

urlpatterns = [
    # Dashboard - Lista produtos de uma empresa
    path('<int:empresa_id>/', views.dashboard_loja, name='dashboard_loja'),
    
    # Cadastro genérico - Cliente ou Produto
    path('<int:empresa_id>/<str:tipo>/', views.cadastrar_item, name='cadastrar_item'),
]
