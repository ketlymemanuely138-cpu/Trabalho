import subprocess
import sys

# Executar o script organize_templates.py com python
try:
    result = subprocess.run([sys.executable, r'c:\Users\ketly\Downloads\mkdir projeto_saas\organize_templates.py'], 
                          capture_output=True, text=True, timeout=30)
    print(result.stdout)
    if result.stderr:
        print("ERRO:", result.stderr)
    print(f"Código de retorno: {result.returncode}")
except Exception as e:
    print(f"Erro ao executar: {e}")
