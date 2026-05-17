#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
EXECUTAR ESTE ARQUIVO PARA ORGANIZAR OS TEMPLATES
Duplo clique ou: python execute_setup.py
"""

import os
import sys
import subprocess

def run_script():
    """Executa o script de organização"""
    script_path = os.path.join(os.path.dirname(__file__), 'organize_django_templates.py')
    
    try:
        # Executar com Python
        result = subprocess.run(
            [sys.executable, script_path],
            capture_output=False,
            text=True
        )
        return result.returncode == 0
    except Exception as e:
        print(f"Erro: {e}")
        return False

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 INICIANDO ORGANIZAÇÃO DE TEMPLATES DJANGO")
    print("="*60 + "\n")
    
    if run_script():
        print("\n" + "="*60)
        print("✅ SUCESSO! Templates organizados com sucesso!")
        print("="*60)
        print("\nPróximos passos:")
        print("1. Abra o arquivo RESUMO_ETAPA1.md para documentação")
        print("2. Crie as views.py")
        print("3. Configure urls.py")
        print("4. Teste os templates")
    else:
        print("\n❌ Erro ao executar setup!")
        sys.exit(1)
