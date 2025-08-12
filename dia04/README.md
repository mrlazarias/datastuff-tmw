# 📊 Dia 04 - Estruturas de Dados Avançadas

> **Explorando Listas, Tuplas, Dicionários e Tratamento de Exceções**

---

## 📚 Conceitos Aprendidos

### **1. Listas Avançadas** 📝
- **Métodos de manipulação**: `append()`, `extend()`, `remove()`
- **Operações avançadas**: concatenação com `+`
- **Listas aninhadas**: estruturas multidimensionais
- **Métodos de string**: `upper()`, `title()`
- **Cópia de listas**: slicing `[:]`

### **2. Tuplas** 🔒
- **Imutabilidade**: estrutura que não pode ser alterada
- **Criação e acesso**: sintaxe com parênteses
- **Slicing em tuplas**: operações de fatiamento

### **3. Dicionários** 🗂️
- **Estrutura chave-valor**: `{"chave": "valor"}`
- **Acesso a elementos**: `dict['chave']`
- **Métodos essenciais**: `.keys()`, `.values()`, `.items()`
- **Dicionários aninhados**: estruturas complexas
- **Aplicação prática**: sistemas de preços e dados

### **4. Tratamento de Exceções** ⚠️
- **Try/Except**: captura de erros
- **ValueError**: tratamento de conversões inválidas
- **Validação de entrada**: loops com tratamento de erro

---

## 🗂️ Arquivos do Dia

### **`listas.py`** 📋
```python
# Conceitos abordados:
- Métodos: append(), extend(), remove()
- Concatenação: lista + [elementos]
- Listas aninhadas: ['nome', ['sublista', ['subsub']]]
- String methods: upper(), title()
- Cópia: lista[:]
- Iteração com for
```

### **`tuplas.py`** 🔒
```python
# Conceitos abordados:
- Criação: nomes = ('murilo', 'isaac', 'manu')
- Imutabilidade: não permite modificações
- Slicing: nomes[::-1] para inversão
```

### **`dicionarios.py`** 🗂️
```python
# Conceitos abordados:
- Estrutura: {"nome": "Murilo", "idade": 27}
- Acesso: dados['nome']
- Métodos: .keys(), .values(), .items()
- Aninhamento: dicionários dentro de listas
- Listas dentro de dicionários
```

---

## 📁 Projetos e Exercícios

### **Pasta `loteria/`** 🎲
- **`loteria_1.py`**: Jogo simples de adivinhação
- **`loteria_2.py`**: Versão avançada com try/except e múltiplas tentativas

### **Exercícios em `ex_azul/`** 💙
- **`03_dict.py`**: Sistema de sorveteria usando dicionários
- **`06_lista.py`**: Verificação de itens em lista
- **`08_for.py`**: Coleta de dados com loop FOR

---

## 🎯 Conceitos Chave

### **Estruturas de Dados - Comparação**
| Tipo | Mutável | Ordenado | Indexado | Sintaxe | Uso Principal |
|------|---------|----------|----------|---------|---------------|
| **Lista** | ✅ Sim | ✅ Sim | ✅ Sim | `[a, b, c]` | Coleções modificáveis |
| **Tupla** | ❌ Não | ✅ Sim | ✅ Sim | `(a, b, c)` | Dados imutáveis |
| **Dicionário** | ✅ Sim | ✅ Sim* | 🔑 Chave | `{"a": 1}` | Mapeamento chave-valor |

### **Métodos de Lista**
| Método | Função | Exemplo | Resultado |
|--------|--------|---------|-----------|
| **`append()`** | Adiciona 1 elemento | `lista.append(5)` | `[1,2,3,5]` |
| **`extend()`** | Adiciona múltiplos | `lista.extend([4,5])` | `[1,2,3,4,5]` |
| **`remove()`** | Remove elemento | `lista.remove(2)` | `[1,3,4,5]` |
| **`+`** | Concatena listas | `[1,2] + [3,4]` | `[1,2,3,4]` |

### **Métodos de Dicionário**
| Método | Retorna | Exemplo |
|--------|---------|---------|
| **`.keys()`** | Todas as chaves | `dict_keys(['nome', 'idade'])` |
| **`.values()`** | Todos os valores | `dict_values(['Murilo', 27])` |
| **`.items()`** | Pares chave-valor | `dict_items([('nome', 'Murilo')])` |

---

## 💡 Exemplos Práticos

### **1. Sistema de Dados Pessoais**
```python
dados = {
    "nome": "Murilo",
    "sobrenome": "Azarias", 
    "idade": 27,
    "ex": ["Nah", "Josefina", "Elaine"],
    "filhos": [
        {"nome": "Maria", "idade": 2}, 
        {"nome": "Murilo", "idade": 27}
    ]
}

# Acessar filho específico
idade_primeiro_filho = dados["filhos"][0]["idade"]  # 2
```

### **2. Sistema de Preços (Sorveteria)**
```python
sorvetes = {
    'casquinha': 1.00,
    'cascão': 2.50,
    'cestinha': 4.00
}

tipo = input("Tipo do sorvete: ")
if tipo in sorvetes:
    preco = sorvetes[tipo]
```

### **3. Validação com Try/Except**
```python
while True:
    try:
        numero = int(input("Digite um número: "))
        break
    except ValueError:
        print("Por favor, digite apenas números!")
```

### **4. Listas Aninhadas**
```python
dados = ['Murilo', 'Azarias', 27, ['Manuela', 'Dorta', ['Isaac']]]
# Acessar elemento aninhado
nome_profundo = dados[3][2][0]  # 'Isaac'
```

---

## 🔍 Aplicações Práticas

1. **🛒 Sistema de Loja**: Verificação de produtos em estoque
2. **🍦 Calculadora de Preços**: Dicionários para tabelas de preços
3. **🎮 Jogos Simples**: Estruturas de dados para game logic
4. **📊 Coleta de Dados**: Listas para armazenar informações
5. **⚠️ Validação Robusta**: Try/except para entrada de usuário

---

## 🚀 Destaques do Aprendizado

### **Manipulação Avançada de Listas**
- **Métodos dinâmicos**: `append()`, `extend()`, `remove()`
- **Estruturas complexas**: listas dentro de listas
- **Cópia segura**: uso de `[:]` para evitar referências

### **Poder dos Dicionários**
- **Flexibilidade**: diferentes tipos de dados como valores
- **Estruturas aninhadas**: dicionários com listas e vice-versa
- **Acesso eficiente**: busca por chave em O(1)

### **Robustez com Try/Except**
- **Prevenção de crashes**: captura de `ValueError`
- **Loops inteligentes**: validação contínua até entrada válida
- **UX melhor**: mensagens de erro personalizadas

---

## 🎓 Próximos Passos

- **Funções**: Organização e reutilização de código
- **Compreensões de Lista**: Sintaxe avançada `[x for x in lista]`
- **Métodos avançados de dicionário**: `get()`, `update()`, `pop()`
- **Módulos**: Importação e organização de código

---

<div align="center">

**📊 Estruturas de Dados • 🗂️ Dicionários • 🔒 Tuplas • ⚠️ Exceções**

*Dia 04 - Dominando as Estruturas de Dados do Python*

</div>