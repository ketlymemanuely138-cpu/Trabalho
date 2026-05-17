# 🧪 GUIA DE TESTE - ETAPA 2

## Pré-requisitos

✅ Templates organizados em `core_loja/templates/`
✅ forms.py e views.py atualizados
✅ urls.py configurado
✅ Banco de dados migrado

## 1. Preparar o Ambiente

```bash
# Navegar até a pasta do projeto
cd c:\Users\ketly\Downloads\mkdir projeto_saas

# Ativar ambiente virtual (se necessário)
# venv\Scripts\activate  (Windows)
# source venv/bin/activate  (Linux/Mac)

# Executar migrações (se não feito)
python manage.py migrate

# Criar superuser (para admin)
python manage.py createsuperuser

# Iniciar servidor
python manage.py runserver
```

## 2. Criar Dados de Teste

### Via Admin Django

1. Acesse: http://localhost:8000/admin/
2. Login com superuser
3. Crie uma Empresa:
   - Nome: "Loja Teste"
   - Ramo: "Petshop"
   - ID: 1 (será gerado automaticamente)

## 3. Testar as Views

### ✅ TESTE 1: Dashboard (Listar Produtos)

**URL**: `http://localhost:8000/loja/1/`

**Esperado**:
- [ ] Página renderiza sem erro
- [ ] Mostra "Lista de Produtos"
- [ ] Mostra nome da empresa na sidebar
- [ ] Navegação funciona
- [ ] Se não houver produtos, tabela vazia ✅

**Passos**:
1. Abrir navegador
2. Ir para: `http://localhost:8000/loja/1/`
3. Verificar conteúdo

**Debug** (se erro):
```python
# No views.py adicione:
print(f"Empresa: {empresa}")
print(f"Produtos: {produtos}")
```

---

### ✅ TESTE 2: Novo Cliente (GET)

**URL**: `http://localhost:8000/loja/1/cliente/`

**Esperado**:
- [ ] Página renderiza
- [ ] Mostra titulo "Novo Cliente"
- [ ] Form com campos: nome, cpf, email, telefone, data_nascimento, endereco, cidade, cep
- [ ] Botão "Salvar" presente
- [ ] Bootstrap styling aplicado

**Passos**:
1. Abrir navegador
2. Ir para: `http://localhost:8000/loja/1/cliente/`
3. Verificar campos do form

---

### ✅ TESTE 3: Novo Cliente (POST - Preenchimento)

**URL**: `http://localhost:8000/loja/1/cliente/`

**Dados para Testar**:
```
Nome: João Silva
CPF: 123.456.789-00
Email: joao@email.com
Telefone: (37) 98765-4321
Data Nascimento: 1990-05-15
Endereço: Rua A, 123
Cidade: Nova Porteirinha
CEP: 39.530-000
```

**Esperado Após Salvar**:
- [ ] Redirect para: `http://localhost:8000/loja/1/` (dashboard)
- [ ] Novo cliente aparece na query do banco
- [ ] Sem mensagens de erro

**Passos**:
1. Preencher todos os campos
2. Clicar em "Salvar"
3. Verificar se redirecionou
4. Verificar em Admin se cliente foi criado

**Debug**:
```bash
# No terminal Django shell:
python manage.py shell
>>> from core_loja.models import Cliente
>>> Cliente.objects.all()
>>> Cliente.objects.filter(empresa_id=1)
```

---

### ✅ TESTE 4: Novo Cliente (POST - Validação)

**Teste com dados inválidos**:

**Dados**:
```
Nome: (vazio)
CPF: (vazio)
Email: email_invalido
Telefone: (vazio)
Data Nascimento: (vazio)
Endereço: (vazio)
Cidade: (vazio)
CEP: (vazio)
```

**Esperado**:
- [ ] Form renderiza novamente
- [ ] Mensagens de erro aparecem
- [ ] Cliente NÃO foi salvo no banco
- [ ] Dados permanecem no form (erro em fields)

**Passos**:
1. Deixar campos vazios
2. Clicar em "Salvar"
3. Verificar mensagens de erro

---

### ✅ TESTE 5: Novo Produto (GET)

**URL**: `http://localhost:8000/loja/1/produto/`

**Esperado**:
- [ ] Página renderiza
- [ ] Titulo "Novo Produto"
- [ ] Form com campos: nome, preco
- [ ] Bootstrap styling

**Passos**:
1. Ir para: `http://localhost:8000/loja/1/produto/`
2. Verificar campos

---

### ✅ TESTE 6: Novo Produto (POST - Preenchimento)

**Dados**:
```
Nome: Ração Premium
Preço: 45.50
```

**Esperado**:
- [ ] Redirect para: `http://localhost:8000/loja/1/`
- [ ] Produto aparece na tabela
- [ ] Preço formatado corretamente (R$ 45.50)

**Passos**:
1. Preencher campos
2. Clicar "Salvar"
3. Verificar se aparece na lista

---

### ✅ TESTE 7: Empresa Não Existe (404)

**URL**: `http://localhost:8000/loja/999/`

**Esperado**:
- [ ] Erro 404 Page Not Found
- [ ] Mensagem Django padrão

**Passos**:
1. Ir para URL com ID inválido
2. Verificar erro

---

## 4. Verificar Segurança

### ✅ Teste: Campo Empresa via URL

**Objetivo**: Garantir que `empresa` sempre vem da URL

```bash
# Terminal Django Shell:
python manage.py shell

>>> from core_loja.models import Empresa, Cliente
>>> emp1 = Empresa.objects.get(id=1)
>>> emp2 = Empresa.objects.create(nome="Empresa 2", ramo="Loja")
>>> 
>>> # Tentar criar cliente para empresa 2 via URL de empresa 1
>>> # GET /loja/1/cliente/ → formulário para empresa 1
>>> # Salvar dados → cliente sempre será de empresa 1
>>>
>>> # Verificar:
>>> Cliente.objects.filter(empresa=emp1)
>>> Cliente.objects.filter(empresa=emp2)
```

---

## 5. Checklist de Testes

- [ ] Dashboard renderiza (empresas com e sem produtos)
- [ ] Novo Cliente - GET (form vazio)
- [ ] Novo Cliente - POST (dados válidos)
- [ ] Novo Cliente - POST (dados inválidos)
- [ ] Novo Produto - GET (form vazio)
- [ ] Novo Produto - POST (dados válidos)
- [ ] Novo Produto - POST (dados inválidos)
- [ ] 404 para empresa inválida
- [ ] Cliente vinculado à empresa correta
- [ ] Produto vinculado à empresa correta
- [ ] Redirect funciona após salvar
- [ ] Bootstrap styling aplicado

---

## 6. Possíveis Problemas

### ❌ "Module not found: forms" ou "Module not found: views"

**Solução**: Verificar imports em `core_loja/urls.py`

```python
from . import views  # Correto
# OU
from .views import dashboard_loja, cadastrar_item  # Alternativa
```

### ❌ "Reverse for 'dashboard_loja' not found"

**Solução**: Verificar `name='dashboard_loja'` em `urls.py`

```python
path('<int:empresa_id>/', views.dashboard_loja, name='dashboard_loja')
```

### ❌ "Template does not exist: loja.html"

**Solução**: Verificar se templates estão em `core_loja/templates/`

```bash
# Listar:
ls core_loja/templates/

# Deve mostrar:
# base.html
# form_template.html
# loja.html
```

### ❌ "FieldError: Unknown field(s) (empresa)"

**Solução**: Remover campo `empresa` do form

```python
# Correto:
fields = ['nome', 'preco']

# Errado:
fields = ['empresa', 'nome', 'preco']
```

---

## 7. Logs Úteis

**Para ver informações de debug**, adicione em `views.py`:

```python
def dashboard_loja(request, empresa_id):
    empresa = get_object_or_404(Empresa, id=empresa_id)
    produtos = Produto.objects.filter(empresa=empresa)
    
    # DEBUG
    print(f"[DEBUG] Empresa: {empresa}")
    print(f"[DEBUG] Produtos: {list(produtos)}")
    print(f"[DEBUG] Total: {produtos.count()}")
    
    return render(...)
```

---

**Status**: 🟢 Pronto para testar
**Próximo**: Criar admin.py e registrar modelos
