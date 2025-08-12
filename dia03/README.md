# 🔄 Dia 03 - Estruturas de Repetição e Listas (2025)

> **Explorando loops e estruturas de dados sequenciais em Python**

---

## 📚 Conceitos Aprendidos

### **1. Listas (Lists)** 📝
- **Criação de listas vazias e com dados**
- **Indexação e acesso a elementos**
- **Slicing (fatiamento) de listas**
- **Índices negativos**

### **2. Loop FOR** 🔁
- **Iteração sobre strings**
- **Uso de `range()` para sequências numéricas**
- **Controle de fluxo com `continue`**
- **Filtragem com condicionais dentro de loops**

### **3. Loop WHILE** ♾️
- **Loops condicionais**
- **Controle de fluxo com `break` e `continue`**
- **Loops infinitos controlados**
- **Contadores e incrementos**

---

## 🗂️ Arquivos do Dia

### **`listas.py`** 📋
```python
# Conceitos abordados:
- Criação de lista vazia: []
- Lista mista: ["murilo", "azarias", 27, 1.82]
- Indexação: minha_lista[0], minha_lista[3]
- Índices negativos: minha_lista[-2]
- Slicing: minha_lista[0:2], minha_lista[::-1]
- Step em slicing: minha_lista[::2]
```

### **`for.py`** 🔁
```python
# Conceitos abordados:
- Iteração sobre string: for i in "Murilo Azarias"
- Uso de continue para pular iterações
- range() para sequências: range(0, 10)
- Filtros com condicionais: if i % 2 == 0
```

### **`while.py`** ♾️
```python
# Conceitos abordados:
- Loop controlado por contador
- input() dentro de loops
- Loop infinito com break
- continue para pular iterações
- Validação de entrada do usuário
```

---

## 🎯 Conceitos Chave

### **Listas - Operações Fundamentais**
| Operação | Sintaxe | Exemplo | Resultado |
|----------|---------|---------|-----------|
| **Criar lista** | `[]` | `lista = [1, 2, 3]` | `[1, 2, 3]` |
| **Acessar elemento** | `lista[índice]` | `lista[0]` | `1` |
| **Último elemento** | `lista[-1]` | `lista[-1]` | `3` |
| **Slice** | `lista[start:stop]` | `lista[0:2]` | `[1, 2]` |
| **Reverso** | `lista[::-1]` | `lista[::-1]` | `[3, 2, 1]` |

### **Loops - Estruturas de Repetição**
| Tipo | Uso Principal | Exemplo |
|------|---------------|---------|
| **FOR** | Iteração sobre sequências | `for i in range(10):` |
| **WHILE** | Repetição condicional | `while contador <= 10:` |

### **Controle de Fluxo**
| Comando | Função | Contexto |
|---------|---------|----------|
| **`break`** | Sai do loop | Termina o loop imediatamente |
| **`continue`** | Pula iteração | Vai para próxima iteração |

---

## 💡 Exemplos Práticos

### **1. Lista com Diferentes Tipos**
```python
dados_pessoais = ["murilo", "azarias", 27, 1.82]
nome = dados_pessoais[0]      # "murilo"
sobrenome = dados_pessoais[1] # "azarias"
idade = dados_pessoais[2]     # 27
altura = dados_pessoais[3]    # 1.82
```

### **2. FOR com Filtro**
```python
# Imprimir apenas números pares de 1 a 15
for numero in range(1, 16):
    if numero % 2 == 0:
        print(numero)  # 2, 4, 6, 8, 10, 12, 14
```

### **3. WHILE com Validação**
```python
while True:
    senha = input("Digite a senha: ")
    if senha == "correct":
        break  # Sai do loop
    print("Senha incorreta, tente novamente")
```

---

## 🔍 Aplicações Aprendidas

1. **📊 Processamento de Dados**: Iteração sobre listas de informações
2. **🔢 Cálculos Repetitivos**: Loops para operações matemáticas
3. **✅ Validação de Entrada**: WHILE para garantir dados corretos
4. **🎯 Filtragem**: FOR com condicionais para selecionar dados

---

## 🎓 Próximos Passos

- **Métodos de Lista**: `append()`, `remove()`, `sort()`
- **List Comprehension**: Sintaxe avançada para criação de listas
- **Nested Loops**: Loops aninhados
- **Funções**: Organização de código reutilizável

---

<div align="center">

**🔄 Estruturas de Repetição • 📝 Listas • 🎯 Controle de Fluxo**

*Dia 03 - Fundamentos de Loops e Estruturas de Dados*

</div>