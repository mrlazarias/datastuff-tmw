# Dia 02 - Variáveis, Input e Estruturas Condicionais

## O que aprendemos hoje

### 1. Variáveis (variaveis.py)
- Como criar e usar variáveis para armazenar dados
- Concatenação de strings com o operador `+`
- Passagem de múltiplas variáveis no `print()`

```python
nome = "Liro"
print("Seja bem vindo, " + nome)

a = 10
b = 20
resultado = a + b
print("A soma de", a, "e", b, "é", resultado)
```

### 2. Entrada de dados do usuário (input.py)
- Função `input()` para receber dados do usuário
- Conversão de tipos com `int()` para trabalhar com números
- Diferença entre concatenação de strings e soma numérica

```python
nome = input("Digite seu nome: ")
print(nome)

a = int(input("Entre com o valor de a:"))
b = int(input("Entre com o valor de b:"))
soma = a + b
print(soma)
```

**Importante**: 
- `"10" + "20"` = `"1020"` (concatenação)
- `10 + 20` = `30` (soma matemática)

### 3. Estrutura condicional IF (if.py)
- Comando `if` para criar condições
- Operadores de comparação (`>=`, `>`, `<`, etc.)
- Indentação é obrigatória em Python!

```python
idade = int(input("Entre com a sua idade: "))

if idade >= 18:
    print("Você é maior de idade! Beba à vontade")
```

### 4. Estrutura IF-ELSE (else.py)
- Comando `else` para executar código quando a condição é falsa
- Criação de fluxos alternativos no programa

```python
if idade >= 18:
    print("Você é maior de idade, Beba à vontade")
else:
    print("Você é muito jovem, go home")
```

### 5. Estrutura IF-ELIF-ELSE (elif.py)
- Comando `elif` para múltiplas condições
- Encadeamento de condições lógicas
- Uso de intervalos com `<=` e `>=`

```python
if idade < 18:
    print("Você é menor de idade, jesus kid, go home")
elif idade > 70:
    print("Você tá muito idoso e calvo.")
else:
    print("Você é maior de idade, wow")

# Condição em intervalo
if 18 <= idade <= 89:
    print("Você é maior de idade, uhu")
```

### 6. Lógica Booleana e Tabela Verdade (tabela_verdade.py)

#### Valores Booleanos:
- `True` (Verdadeiro)
- `False` (Falso)

#### Operadores Lógicos:

**AND (E)** - Ambas condições devem ser verdadeiras:
```python
idade >= 18 and cnh == "sim"
```

**OR (OU)** - Pelo menos uma condição deve ser verdadeira:
```python
# Implementação matemática da tabela verdade
print("True ou True =", bool(1 + 1))  # True
print("False ou True =", bool(0 + 1))  # True
print("True ou False =", bool(1 + 0))  # True
print("False ou False =", bool(0 + 0))  # False
```

#### Tabela Verdade AND:
- True AND True = True
- False AND True = False
- True AND False = False
- False AND False = False

#### Tabela Verdade OR:
- True OR True = True
- False OR True = True
- True OR False = True
- False OR False = False

### 7. Exercícios Práticos

#### Exercícios básicos (ex/):
1. **01.py**: Programa que dá bom dia
2. **02.py**: Programa que cumprimenta pelo nome
3. **03.py**: Sistema de venda de água (com erro de sintaxe para correção)
4. **04.py, 05.py, 06.py**: Exercícios adicionais

#### Exercícios avançados (ex/ex_azul/):
- **01.py**: Sistema de vendas com condicionais mais complexas

## Conceitos importantes aprendidos

1. **Variáveis**: Containers para armazenar dados
2. **Input/Output**: Interação com o usuário
3. **Conversão de tipos**: `int()`, `str()`, `bool()`
4. **Indentação**: Fundamental em Python (4 espaços ou 1 tab)
5. **Operadores de comparação**: `==`, `!=`, `>`, `<`, `>=`, `<=`
6. **Operadores lógicos**: `and`, `or`, `not`
7. **Estruturas condicionais**: `if`, `elif`, `else`
8. **Valores booleanos**: `True`, `False`
9. **Fluxo de controle**: Como o programa toma decisões

## Aplicações em Ciência de Dados

Estes conceitos são fundamentais para:
- **Limpeza de dados**: Condições para filtrar dados inválidos
- **Análise exploratória**: Categorização de dados com condicionais
- **Validação**: Verificação de entrada de dados
- **Pipelines de dados**: Fluxos condicionais de processamento

## Erros comuns identificados

1. **Sintaxe**: Dois pontos (`:`) obrigatórios após `if`, `elif`, `else`
2. **Indentação**: Código dentro do bloco deve estar indentado
3. **Tipos**: Lembrar de converter `input()` para `int()` quando necessário
4. **Comparação**: Usar `==` para comparar, não `=` (que é atribuição)

## Próximos passos
- Estruturas de repetição (for, while)
- Listas e coleções
- Funções definidas pelo usuário