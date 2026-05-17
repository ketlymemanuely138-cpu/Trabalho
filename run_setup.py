#!/usr/bin/env python
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

# Agora podemos importar os modelos
from core_loja.models import Empresa, Produto, Cliente

# Criar a pasta templates
templates_dir = os.path.join(os.path.dirname(__file__), 'core_loja', 'templates')
os.makedirs(templates_dir, exist_ok=True)

print(f"✓ Pasta templates criada em: {templates_dir}")

# Remover arquivos HTML da raiz de core_loja
root_templates = ['base.html', 'form_template.html', 'loja.html']
core_loja_path = os.path.join(os.path.dirname(__file__), 'core_loja')

for template in root_templates:
    src_path = os.path.join(core_loja_path, template)
    if os.path.exists(src_path):
        os.remove(src_path)
        print(f"✓ Removido arquivo raiz: {template}")

print("\n✓ Setup concluído com sucesso!")
