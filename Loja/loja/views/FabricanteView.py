from django.shortcuts import render, redirect, get_object_or_404
from loja.models import Fabricante
from loja.forms.FabricanteForm import FabricanteForm

def list_fabricante_view(request, id=None):
    fabricantes = Fabricante.objects.all()
    context = {'fabricantes': fabricantes}
    return render(request, template_name='fabricante/fabricante.html', context=context, status=200)

def create_fabricante_view(request):
    if request.method == 'POST':
        form = FabricanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/fabricante/')
    else:
        form = FabricanteForm()
    context = {'form': form}
    return render(request, 'fabricante/fabricante-create.html', context=context, status=200)

def edit_fabricante_view(request, id):
    fabricante = get_object_or_404(Fabricante, id=id)
    if request.method == 'POST':
        form = FabricanteForm(request.POST, instance=fabricante)
        if form.is_valid():
            form.save()
            return redirect('/fabricante/')
    else:
        form = FabricanteForm(instance=fabricante)
    context = {'form': form, 'fabricante': fabricante}
    return render(request, 'fabricante/fabricante-edit.html', context=context, status=200)

def delete_fabricante_view(request, id):
    fabricante = get_object_or_404(Fabricante, id=id)
    if request.method == 'POST':
        fabricante.delete()
        return redirect('/fabricante/')
    context = {'fabricante': fabricante}
    return render(request, 'fabricante/fabricante-delete.html', context=context, status=200)