from django.urls import path
from . import views

app_name = 'produto'  # produto: lista

urlpatterns = [
    path('', views.ListaProduto.as_view(), name='lista'),
    path('<slug>', views.DetalheProduto.as_view(), name='detalhe'),
    path('addcarrinho/', views.AddCarrinho.as_view(), name='addcarrinho'),
    path('removercarrinho/', views.RemoverCarrinho.as_view(),
         name='removercarrinho'),
    path('carrinho/', views.Carrinho.as_view(), name='carrinho'),
    path('resumodacompra/', views.Resumodacompra.as_view(), name='resumodacompra'),
]
