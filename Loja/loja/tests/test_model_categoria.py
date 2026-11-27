from django.test import TestCase
from loja.models import Categoria

class CategoriaModelTestClass(TestCase):
    def setUp(self):
        Categoria.objects.create(Categoria='Monitores')

    def test_categoria_exist(self):
        categoria = Categoria.objects.first()
        self.assertIsNotNone(categoria)