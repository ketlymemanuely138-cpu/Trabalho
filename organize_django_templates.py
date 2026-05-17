#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script para organizar templates Django
Uso: python organize_django_templates.py
"""

import os
import shutil

def main():
    # Definir caminhos
    base_dir = os.path.dirname(os.path.abspath(__file__))
    core_loja_dir = os.path.join(base_dir, 'core_loja')
    templates_dir = os.path.join(core_loja_dir, 'templates')
    
    print("=" * 60)
    print("🚀 Organizando Templates Django")
    print("=" * 60)
    
    # 1. Criar pasta templates
    try:
        os.makedirs(templates_dir, exist_ok=True)
        print(f"✅ Pasta criada/verificada: {templates_dir}")
    except Exception as e:
        print(f"❌ Erro ao criar pasta: {e}")
        return False
    
    # 2. Mover arquivos HTML para templates
    html_files = ['base.html', 'form_template.html', 'loja.html']
    
    for html_file in html_files:
        src_path = os.path.join(core_loja_dir, html_file)
        dst_path = os.path.join(templates_dir, html_file)
        
        if os.path.exists(src_path):
            try:
                # Se o arquivo já existe em templates, remover versão antiga
                if os.path.exists(dst_path):
                    os.remove(dst_path)
                
                # Copiar arquivo
                shutil.copy2(src_path, dst_path)
                print(f"✅ Copiado: {html_file} → templates/")
                
                # Remover arquivo original
                os.remove(src_path)
                print(f"   Removido arquivo original")
                
            except Exception as e:
                print(f"❌ Erro ao mover {html_file}: {e}")
                return False
        else:
            print(f"⚠️  Arquivo não encontrado: {html_file}")
    
    # 3. Remover script de setup se existir
    setup_script = os.path.join(core_loja_dir, 'setup_django_templates.py')
    if os.path.exists(setup_script):
        try:
            os.remove(setup_script)
            print(f"✅ Script de setup removido")
        except:
            pass
    
    print("\n" + "=" * 60)
    print("✨ Templates organizados com sucesso!")
    print("=" * 60)
    print(f"\n📁 Estrutura criada:")
    print(f"   core_loja/templates/")
    print(f"   ├── base.html")
    print(f"   ├── form_template.html")
    print(f"   └── loja.html")
    print(f"\n📝 Próximo passo: Criar views.py e urls.py")
    
    return True

if __name__ == '__main__':
    success = main()
    exit(0 if success else 1)
