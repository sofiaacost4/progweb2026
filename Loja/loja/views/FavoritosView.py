from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from loja.models import Produto, Usuario, Favorito

@login_required
def favoritos_view(request):
    usuario = Usuario.objects.filter(user=request.user).first()
    favoritos = Favorito.objects.filter(usuario=usuario).select_related('produto')
    produtos = [favorito.produto for favorito in favoritos]
    context = {
        'produtos': produtos
    }
    return render(
        request,
        'produto/favoritos.html',
        context
    )