from django.urls import path
from loja.views.CategoriaView import create_categoria_view, list_categoria_view, edit_categoria_view, edit_categoria_postback, delete_categoria_view, delete_categoria_postback, details_categoria_view
urlpatterns = [
    path("", list_categoria_view, name='categoria'),
    path("create", create_categoria_view, name='create_categoria'),
    path("edit/<int:id>", edit_categoria_view, name='edit_categoria'),
    path("edit", edit_categoria_postback, name="edit_categoria_postback"),
    path("delete/<int:id>", delete_categoria_view, name="delete_categoria"),
    path("delete", delete_categoria_postback, name="delete_categoria_postback"),
    path("details/<int:id>", details_categoria_view, name="details_categoria"),
]