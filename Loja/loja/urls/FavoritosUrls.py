from django.urls import path
from loja.views.FavoritosView import favoritos_view
urlpatterns = [
    path("favoritos", favoritos_view, name='favoritos')
]