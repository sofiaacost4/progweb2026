from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from loja.models import Produto, Usuario, Favorito

@login_required
def favoritos_view(request):
    usuario = Usuario.objects.filter(user=request.user).first()
    favoritos = Favorito.objects.filter(usuario=usuario).select_related('produto')
    produtos = [favorito.produto for favorito in favoritos]
    context = {
        'produtos': produtos
    }
    return render(request, 'produto/produtos-favoritos.html', context)

@login_required
def favoritar_produto(request, produto_id):
    usuario = Usuario.objects.get(user=request.user)
    produto = get_object_or_404(Produto, id=produto_id)
    Favorito.objects.get_or_create(
        usuario=usuario,
        produto=produto
    )
    return redirect('favoritos')