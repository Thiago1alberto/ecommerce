from django.urls import path
from . import views

app_name = 'pedido'

urlpatterns = [
    path('', views.Pagar.as_view(), name='pagar'),
    path('fecharPedido/', views.FecharPedido.as_view(),
         name='fecharPedido'),
    path('detalhe/', views.Detalhe.as_view(), name='detalhe'),

]
