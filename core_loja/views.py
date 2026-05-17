from django.shortcuts import render, get_object_or_404, redirect
from .models import Empresa, Produto, Cliente
from .forms import ClienteForm, ProdutoForm


def dashboard_loja(request, empresa_id):
    """Tela que lista os produtos"""
    empresa = get_object_or_404(Empresa, id=empresa_id)
    produtos = Produto.objects.filter(empresa=empresa)
    return render(request, 'loja.html', {'empresa': empresa, 'produtos': produtos})


def cadastrar_item(request, empresa_id, tipo):
    """Tela de cadastro (Genérica para Cliente e Produto)"""
    empresa = get_object_or_404(Empresa, id=empresa_id)
    
    if tipo == 'cliente':
        form = ClienteForm(request.POST or None)
        titulo = "Novo Cliente"
    else:
        form = ProdutoForm(request.POST or None)
        titulo = "Novo Produto"
    
    if request.method == 'POST' and form.is_valid():
        item = form.save(commit=False)
        item.empresa = empresa  # Vincula à empresa da URL
        item.save()
        return redirect('url_da_loja', empresa_id=empresa.id)
    
    return render(request, 'form_template.html', {'form': form, 'empresa': empresa, 'titulo': titulo})
