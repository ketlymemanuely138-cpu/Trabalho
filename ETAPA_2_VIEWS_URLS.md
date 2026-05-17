# 📝 ETAPA 2 - IMPLEMENTANDO VIEWS E URLS

## ✅ Mudanças Realizadas

### 1. **Atualizado: forms.py**
- ✅ Removido `EmpresaForm` (não usado em cadastros)
- ✅ Simplificado `ClienteForm` - removido campo `ativo`
- ✅ Simplificado `ProdutoForm` - mantém apenas essenciais
- ✅ Removido campo `empresa` dos formulários (segurança)
- ✅ Removido campo `data_cadastro` (automático no modelo)

**Por quê?**
- `empresa` é definida automaticamente via URL
- `data_cadastro` é preenchida automaticamente
- `ativo` não é necessário no cadastro inicial

### 2. **Criado: views.py**

#### `dashboard_loja(request, empresa_id)`
```python
empresa = get_object_or_404(Empresa, id=empresa_id)
produtos = Produto.objects.filter(empresa=empresa)
return render(request, 'loja.html', ...)
```
- Função para **listar produtos** de uma empresa
- Usa `get_object_or_404` - retorna 404 se empresa não existe
- Filtra produtos apenas da empresa específica
- Renderiza template `loja.html`

#### `cadastrar_item(request, empresa_id, tipo)`
```python
if tipo == 'cliente':
    form = ClienteForm(...)
    titulo = "Novo Cliente"
else:
    form = ProdutoForm(...)
    titulo = "Novo Produto"
```
- Função **genérica** para cadastrar cliente OU produto
- Parâmetro `tipo` define qual form usar
- `request.POST or None` - permite GET (mostra form vazio) e POST (valida dados)
- `form.save(commit=False)` - permite modificar antes de salvar
- `item.empresa = empresa` - vincula automaticamente à empresa
- Redireciona para dashboard após salvar

### 3. **Criado: core_loja/urls.py**

```python
path('<int:empresa_id>/', views.dashboard_loja, name='dashboard_loja')
path('<int:empresa_id>/<str:tipo>/', views.cadastrar_item, name='cadastrar_item')
```

**Rotas disponíveis:**
- `/loja/1/` → Dashboard da empresa 1 (lista produtos)
- `/loja/1/cliente/` → Novo cliente para empresa 1
- `/loja/1/produto/` → Novo produto para empresa 1

### 4. **Atualizado: core/urls.py**

```python
path('loja/', include('core_loja.urls')),
```

- Inclui as URLs da app core_loja
- Prefixo `loja/` para todas as rotas da app

## 🔄 Fluxo de Dados

### Cadastrar Novo Cliente:
```
1. GET /loja/1/cliente/
   → cadastrar_item(request, 1, 'cliente')
   → Exibe formulário vazio (form = ClienteForm(None))
   
2. POST /loja/1/cliente/ (com dados preenchidos)
   → cadastrar_item(request, 1, 'cliente')
   → form.is_valid() ✅
   → item.empresa = Empresa.objects.get(id=1)
   → item.save()
   → redirect('/loja/1/')
```

### Cadastrar Novo Produto:
```
1. GET /loja/1/produto/
   → cadastrar_item(request, 1, 'produto')
   → Exibe formulário vazio (form = ProdutoForm(None))
   
2. POST /loja/1/produto/ (com dados preenchidos)
   → cadastrar_item(request, 1, 'produto')
   → form.is_valid() ✅
   → item.empresa = Empresa.objects.get(id=1)
   → item.save()
   → redirect('/loja/1/')
```

## 🎯 Conceitos Django Utilizados

| Conceito | Uso |
|----------|-----|
| `render()` | Renderizar template com contexto |
| `get_object_or_404()` | Buscar objeto ou retornar 404 |
| `redirect()` | Redirecionar para outra URL |
| `request.POST or None` | Form GET/POST dinâmico |
| `form.save(commit=False)` | Salvar sem persistir (modificar antes) |
| `filter()` | Filtrar objetos do banco |
| `include()` | Incluir URLs de outra app |
| `<int:empresa_id>` | Parâmetro de URL inteiro |
| `<str:tipo>` | Parâmetro de URL string |

## 📋 URLs Disponíveis

| Método | URL | Função |
|--------|-----|--------|
| GET | `/loja/1/` | Dashboard empresa 1 |
| POST | `/loja/1/` | Erro (não aceita) |
| GET | `/loja/1/cliente/` | Form novo cliente |
| POST | `/loja/1/cliente/` | Salvar novo cliente |
| GET | `/loja/1/produto/` | Form novo produto |
| POST | `/loja/1/produto/` | Salvar novo produto |

## ✅ Checklist

- [x] forms.py simplificado
- [x] views.py criado com 2 funções
- [x] core_loja/urls.py criado
- [x] core/urls.py atualizado
- [x] Segurança (empresa vinculada automaticamente)
- [x] Validações (form.is_valid())

## 🚀 Próximos Passos

1. ✅ Garantir que templates estão em `core_loja/templates/`
2. Testar as URLs no navegador
3. Criar admin.py para gerenciar dados
4. Adicionar autenticação
5. Adicionar permissões por empresa

## 💡 Observações

1. **Segurança**: `empresa` nunca vem do form (vem da URL)
2. **Validação**: Django valida automaticamente via ModelForm
3. **Genérico**: Uma função `cadastrar_item` serve para cliente e produto
4. **Fluxo**: Após salvar, redireciona para dashboard para feedback visual

---

**Status**: ✅ Pronto para testar
**Próxima**: Criar admin.py e testar as views
