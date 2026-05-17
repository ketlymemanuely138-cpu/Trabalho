#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

# Adicionar ao path do Python
sys.path.insert(0, r'c:\Users\ketly\Downloads\mkdir projeto_saas')

# Criar a pasta templates
templates_dir = r'c:\Users\ketly\Downloads\mkdir projeto_saas\core_loja\templates'

try:
    os.makedirs(templates_dir, exist_ok=True)
    print(f'✓ Pasta criada: {templates_dir}')
except Exception as e:
    print(f'✗ Erro ao criar pasta: {e}')
    sys.exit(1)

# Conteúdo dos arquivos
base_html = '''<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>{{ empresa.nome }} | Painel SaaS</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { 
            display: flex; 
            min-height: 100vh; 
            background-color: #f4f7f6; 
        }
        #sidebar { 
            width: 250px; 
            background: #2c3e50; 
            color: white; 
            padding: 20px; 
        }
        #content { 
            flex: 1; 
            padding: 40px; 
        }
        .nav-link { 
            color: #bdc3c7; 
            margin: 10px 0; 
            text-decoration: none;
            display: block;
            padding: 8px 12px;
            border-radius: 5px;
        }
        .nav-link:hover { 
            color: white; 
            background: #34495e; 
        }
    </style>
</head>
<body>
    <div id="sidebar">
        <h4>{{ empresa.nome }}</h4>
        <p class="small">{{ empresa.ramo }}</p>
        <hr>
        <nav class="nav flex-column">
            <a class="nav-link" href="/loja/{{ empresa.id }}/">Produtos</a>
            <a class="nav-link" href="/loja/{{ empresa.id }}/novocliente/">Novo Cliente</a>
            <a class="nav-link" href="/loja/{{ empresa.id }}/novoproduto/">Novo Produto</a>
        </nav>
    </div>
    <div id="content">
        {% block conteudo %}{% endblock %}
    </div>
</body>
</html>'''

form_template_html = '''{% extends 'base.html' %}
{% block conteudo %}
<h2>{{ titulo }}</h2>
<form method="POST" class="card p-4 shadow-sm">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit" class="btn btn-success">Salvar</button>
</form>
{% endblock %}'''

loja_html = '''{% extends 'base.html' %}
{% block conteudo %}
<h2>Lista de Produtos</h2>
<table class="table">
    <thead>
        <tr>
            <th>Nome</th>
            <th>Preço</th>
        </tr>
    </thead>
    <tbody>
        {% for p in produtos %}
        <tr>
            <td>{{ p.nome }}</td>
            <td>R$ {{ p.preco }}</td>
        </tr>
        {% endfor %}
    </tbody>
</table>
{% endblock %}'''

# Criar os arquivos
files_content = {
    'base.html': base_html,
    'form_template.html': form_template_html,
    'loja.html': loja_html,
}

for filename, content in files_content.items():
    filepath = os.path.join(templates_dir, filename)
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'✓ Criado: {filename}')
    except Exception as e:
        print(f'✗ Erro ao criar {filename}: {e}')

print('✓ Estrutura de templates criada com sucesso!')
