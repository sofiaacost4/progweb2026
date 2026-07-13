from django.shortcuts import render, redirect
from loja.models import Categoria

def create_categoria_view(request):
    if request.method == "POST":
        categoria = request.POST.get("Categoria")
        print("postback-create")
        print(categoria)
        try:
            obj_categoria = Categoria()
            obj_categoria.Categoria = categoria
            obj_categoria.criado_em = timezone.now()
            obj_categoria.alterado_em = timezone.now()
            obj_categoria.save()
            print(f"Categoria {categoria} salva com sucesso")
        except Exception as e:
            print(f"Erro inserindo categoria: {e}")
        return redirect("/categoria")
    return render(request, template_name="categoria/categoria-create.html", context={}, status=200)

def list_categoria_view(request, id=None):
    categorias = Categoria.objects.all()
    categoria = request.GET.get("categoria")
    if categoria:
        categorias = categorias.filter(Categoria__contains=categoria)
    if id is not None:
        categorias = categorias.filter(id=id)
    context = {"categorias": categorias}
    return render(request, "categoria/categoria.html", context=context, status=200)

def edit_categoria_view(request, id=None):
    categorias = Categoria.objects.all()
    if id is not None:
        categorias = categorias.filter(id=id)
    categoria = categorias.first()
    context = {"categoria": categoria}
    return render(request, "categoria/categoria-edit.html", context=context, status=200)

def edit_categoria_postback(request):
    if request.method == "POST":
        id = request.POST.get("id")
        nome = request.POST.get("Categoria")
        try:
            obj_categoria = Categoria.objects.filter(id=id).first()
            if obj_categoria:
                obj_categoria.Categoria = nome
                obj_categoria.alterado_em = timezone.now()
                obj_categoria.save()
        except Exception as e:
            print(f"Erro editando categoria: {e}")
    return redirect("/categoria")

def delete_categoria_view(request, id=None):
    categorias = Categoria.objects.all()
    if id is not None:
        categorias = categorias.filter(id=id)
    categoria = categorias.first()
    print(categoria)
    context = {"categoria": categoria}
    return render(request, "categoria/categoria-delete.html", context=context, status=200)

def delete_categoria_postback(request, id=None):
    if request.method == 'POST':
        id = request.POST.get("id")
        print("postback-delete")
        print(id)
        try:
            obj_categoria = Categoria.objects.filter(id=id).first()
            if obj_categoria:
                obj_categoria.delete()
                print(f"Categoria {obj_categoria.Categoria} excluída com sucesso.")
        except Exception as e:
            print("Erro interno excluindo categoria:", e)
        return redirect("/categoria")

def details_categoria_view(request, id=None):
    categorias = Categoria.objects.all()
    if id is not None:
        categorias = categorias.filter(id=id)
    categoria = categorias.first()
    print(categoria)
    context = {"categorias": categorias}
    return render(request, "categoria/categoria-details.html", context=context, status=200)
