from django.urls import path
from loja.views.FavoritosView import favoritos_view, favoritar_produto
urlpatterns = [
    path("favoritos", favoritos_view, name='favoritos'),
    path('favoritar/<int:produto_id>/', favoritar_produto, name='favoritar_produto'),
]