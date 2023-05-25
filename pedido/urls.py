from django.urls import path
from . import views

app_name = 'pedido'

urlpatterns = [
    path('', views.Pagar.as_view(), name='pagar'),
    path('salvarPedido/', views.SalvarPedido.as_view(),
         name='salvarPedido'),
    path('detalhe/', views.Detalhe.as_view(), name='detalhe'),

]
