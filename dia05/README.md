# Dia 05 - Aprendizado Python (2025)

## Conceitos Aprendidos

### 1. Importação de Bibliotecas (`bibliotecas.py`)
- **Import básico**: `import math`
- **Import específico**: `from math import pi, e`
- **Import com wildcard**: `from math import *`
- **Import com alias**: `import math as mt`
- Uso das funções matemáticas como `sqrt()`, constantes `pi` e `e`

### 2. Definição e Uso de Funções (`funcoes.py`)
- **Definição básica de função**: `def funcao(x):`
- **Funções com parâmetros**: `def soma(a=0, b=0):`
- **Valores padrão**: Parâmetros opcionais com valores default
- **Argumentos nomeados**: `soma(a=10, b=20)`
- **Retorno de valores**: Uso da palavra-chave `return`

### 3. Funções Avançadas (`funcoes_2.py`)
- **`*args`**: Função que aceita número variável de argumentos
- **Unpacking**: Desempacotamento de listas usando `*`
- **Operações condicionais**: Diferentes operações baseadas em parâmetros
- **Troca de variáveis**: Técnicas para swap de valores
- **Tuplas**: Criação e manipulação de tuplas

### 4. Manipulação de Arquivos (`lendo_arquivos.py`)
- **Escrita em arquivo**: `open('arquivo.txt', 'a')` e `write()`
- **Leitura de arquivo**: `open('arquivo.txt', 'r')` e `read()`
- **Leitura de linhas**: `readlines()` para ler todas as linhas
- **Context manager**: Uso de `with open()` para gerenciamento automático de arquivos
- **Modos de abertura**: 'r' (read), 'w' (write), 'a' (append)

### 5. APIs e Manipulação de Dados (`api.py`)
- **Requisições HTTP**: Uso da biblioteca `requests`
- **Consumo de API REST**: Requisições para a API do OpenDota
- **Manipulação de JSON**: Conversão de resposta para formato Python
- **DataFrame do Pandas**: Conversão de dados JSON para DataFrame
- **Exportação para CSV**: Salvamento de dados em formato CSV
- **Status codes**: Verificação de status de requisições HTTP

## Arquivos Gerados
- `arquivo.txt` - Arquivo de texto para testes de escrita/leitura
- `heroes_dota.csv` - Dados dos heróis do Dota 2 da API
- `partidas_dota.csv` - Dados de partidas profissionais do Dota 2

## Bibliotecas Utilizadas
- **math**: Funções matemáticas e constantes
- **requests**: Para fazer requisições HTTP
- **pandas**: Para manipulação e análise de dados

## Principais Conceitos
1. **Modularização**: Importação e uso de bibliotecas externas
2. **Funções**: Criação de código reutilizável
3. **Manipulação de arquivos**: Leitura e escrita de dados
4. **APIs**: Consumo de serviços web externos
5. **Estruturas de dados**: Listas, tuplas e DataFrames