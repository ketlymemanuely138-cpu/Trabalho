import os

# Setup manual de criação de templates
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
templates_dir = os.path.join(project_root, 'core_loja', 'templates')

# Criar diretório
os.makedirs(templates_dir, exist_ok=True)

# Conteúdo do base.html
base_content = '''<!DOCTYPE html>
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

# Conteúdo form_template.html
form_content = '''{% extends 'base.html' %}
{% block conteudo %}
<h2>{{ titulo }}</h2>
<form method="POST" class="card p-4 shadow-sm">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit" class="btn btn-success">Salvar</button>
</form>
{% endblock %}'''

# Conteúdo loja.html  
loja_content = '''{% extends 'base.html' %}
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

# Escrever arquivos
files_to_create = {
    'base.html': base_content,
    'form_template.html': form_content,
    'loja.html': loja_content,
}

for filename, content in files_to_create.items():
    filepath = os.path.join(templates_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Criado: {filepath}")

print(f"\nTemplates criados em: {templates_dir}")

# Remover arquivos da raiz
for filename in files_to_create:
    filepath = os.path.join(project_root, 'core_loja', filename)
    if os.path.exists(filepath):
        os.remove(filepath)
        print(f"Removido: {filepath}")
