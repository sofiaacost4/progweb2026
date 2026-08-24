from loja.models import Produto, Fabricante, Categoria
from datetime import timedelta, datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

@login_required
def edit_produto_view(request, id=None):
    produtos = Produto.objects.all()
    Fabricantes = Fabricante.objects.all()
    Categorias = Categoria.objects.all()
    if id is not None:
        produtos = produtos.filter(id=id)
    produto = produtos.first()
    print(produto)
    context = { 'produto': produto, 'fabricantes' : Fabricantes, 'categorias' : Categorias}
    return render(request, template_name='produto/produto-edit.html', context=context, status=200)

def edit_produto_postback(request, id=None):
    if request.method == 'POST':
        id = request.POST.get("id")
        produto = request.POST.get("Produto")
        destaque = request.POST.get("destaque")
        promocao = request.POST.get("promocao")
        msgPromocao = request.POST.get("msgPromocao")
        categoria = request.POST.get("CategoriaFk")
        fabricante = request.POST.get("FabricanteFk")
        image = request.FILES.get("image")
        print("postback")
        print(id)
        print(produto)
        print(destaque)
        print(promocao)
        print(msgPromocao)
        print(categoria)
        print(fabricante)
        print(image)
        try:
            obj_produto = Produto.objects.filter(id=id).first()
            obj_produto.Produto = produto
            obj_produto.destaque = (destaque is not None)
            obj_produto.promocao = (promocao is not None)
            obj_produto.fabricante = Fabricante.objects.filter(id=fabricante).first()
            obj_produto.categoria = Categoria.objects.filter(id=categoria).first()
            if image:
                if obj_produto.image:
                    obj_produto.image.delete(save=False)
                obj_produto.image = image
            if msgPromocao is not None:
                obj_produto.msgPromocao = msgPromocao
            obj_produto.save()
            print("Produto %s salvo com sucesso" % produto)
        except Exception as e:
            print("Erro salvando edição de produto: %s" % e)
    return redirect("/produto")

def list_produto_view(request, id=None):
    produto = request.GET.get("produto")
    destaque = request.GET.get("destaque")
    promocao = request.GET.get("promocao")
    categoria = request.GET.get("categoria")
    fabricante = request.GET.get("fabricante")
    dias = request.GET.get("dias")
    produtos = Produto.objects.all()

    if dias is not None:
        now = timezone.now()
        now = now - timedelta(days = int(dias))
        produtos = produtos.filter(criado_em__gte=now)
    if produto is not None:
        produtos = produtos.filter(Produto__contains=produto )
    if promocao is not None:
        produtos = produtos.filter(promocao=promocao)
    if destaque is not None:
        produtos = produtos.filter(destaque=destaque)
    if categoria is not None:
        produtos = produtos.filter(categoria__Categoria=categoria)
    if fabricante is not None:
        produtos = produtos.filter(fabricante__Fabricante=fabricante)
    if id is not None:
        produtos = produtos.filter(id=id)
    print(produtos)
    context = {'produtos': produtos}
    return render(request, template_name='produto/produto.html', context=context, status=200)

def details_produto_view(request, id=None):
    produtos = Produto.objects.all()
    categorias = Categoria.objects.all()
    fabricantes = Fabricante.objects.all()
    if id is not None:
        produtos = produtos.filter(id=id)
    produto = produtos.first()
    print(produto)
    context = {'produto': produto, 'fabricantes': fabricantes, 'categorias': categorias}
    return render(request, template_name='produto/produto-details.html', context=context, status=200)

def delete_produto_view(request, id=None):
    produtos = Produto.objects.all()
    categorias = Categoria.objects.all()
    fabricantes = Fabricante.objects.all()
    if id is not None:
        produtos = produtos.filter(id=id)
    produto = produtos.first()
    print(produto)
    context = {'produto': produto, 'categorias': categorias, 'fabricantes': fabricantes}
    return render(request, template_name='produto/produto-delete.html', context=context, status=200)

def delete_produto_postback(request, id=None):
    if request.method == 'POST':
        id = request.POST.get("id")
        print("postback-delete")
        print(id)
        try:
            obj_produto = Produto.objects.filter(id=id).first()
            if obj_produto:
                if obj_produto.image:
                    obj_produto.image.delete(save=False)
                obj_produto.delete()
                print(f"Produto {obj_produto.Produto} excluído com sucesso")
        except Exception as e:
            print("Erro excluindo produto:", e)
    return redirect("/produto")

def create_produto_view(request, id=None):
    categorias = Categoria.objects.all()
    fabricantes = Fabricante.objects.all()
    if request.method == 'POST':
        produto = request.POST.get("Produto")
        destaque = request.POST.get("destaque")
        promocao = request.POST.get("promocao")
        msgPromocao = request.POST.get("msgPromocao")
        categoria = request.POST.get("CategoriaFk")
        fabricante = request.POST.get("FabricanteFk")
        preco = request.POST.get("preco")
        image = request.FILES.get("image")
        print("postback-create")
        print(produto)
        print(destaque)
        print(promocao)
        print(msgPromocao)
        print(preco)
        print(categoria)
        print(fabricante)
        print(image)
        try:
            obj_produto = Produto()
            obj_produto.Produto = produto
            obj_produto.destaque = (destaque is not None)
            obj_produto.promocao = (promocao is not None)
            if msgPromocao is not None:
                obj_produto.msgPromocao = msgPromocao
            obj_produto.preco = 0
            if (preco is not None) and ( preco != ""):
                obj_produto.preco = preco
            obj_produto.criado_em = timezone.now()
            obj_produto.alterado_em = obj_produto.criado_em
            if categoria and categoria != "-1":
                obj_produto.categoria = Categoria.objects.filter(id=int(categoria)).first()
            else:
                obj_produto.categoria = None
            if fabricante and fabricante != "-1":
                obj_produto.fabricante = Fabricante.objects.filter(id=int(fabricante)).first()
            else:
                obj_produto.fabricante = None
            # Se for anexado arquivo, salva na pasta e guarda nome no objeto
            if request.FILES is not None:
                num_files = len(request.FILES.getlist('image'))
                if num_files > 0:
                    imagefile = request.FILES['image']
                    print(imagefile)
                    if image:
                        obj_produto.image = image
            obj_produto.save()
            print("Produto %s salvo com sucesso" % produto)
        except Exception as e:
            print("Erro inserindo produto: %s" % e)
        return redirect("/produto")
    context = {'categorias': categorias, 'fabricantes': fabricantes}
    return render(request, template_name='produto/produto-create.html', context=context, status=200)

#cd loja
#Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
#winget install Python.Python.3.11
#py -3.11 -m venv venv
#venv\Scripts\activate
#pip install django Django==4.2.7
#pip install pillow
#python manage.py runserver 127.0.0.1:8080