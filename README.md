# Exercícios de Programação

Este repositório contém a solução para 5 exercícios de programação. O objetivo é implementar soluções para problemas comuns em programação, utilizando conceitos de loops, sequências, vetores e manipulação de dados. Abaixo, você encontrará as descrições dos problemas, os objetivos e as soluções.

---

## Exercício 1: Soma de Números Inteiros até um Índice

### Descrição:
Dado um valor de `INDICE`, o programa deve calcular a soma de todos os números inteiros de 1 até o valor do `INDICE`.

### Objetivo:
- Criar uma lógica que some os números inteiros de 1 até `INDICE`.
- Utilizar um loop para somar os valores progressivamente.

### Solução:
Neste código, iniciamos `SOMA` e `K` com 0. Utilizamos um loop `Enquanto` para iterar até que `K` seja igual a `INDICE`, e em cada iteração, somamos `K` à variável `SOMA`.

**Resultado Esperado:**
Se `INDICE = 13`, a soma será 91.

---

## Exercício 2: Verificação de um Número na Sequência de Fibonacci

### Descrição:
Dado um número informado, o programa deve verificar se ele pertence à sequência de Fibonacci. A sequência de Fibonacci começa com 0 e 1, e cada número subsequente é a soma dos dois anteriores.

### Objetivo:
- Gerar a sequência de Fibonacci até que o número informado seja alcançado ou ultrapassado.
- Verificar se o número está na sequência.

### Solução:
O código gera a sequência de Fibonacci até o número informado e verifica se esse número pertence à sequência.

**Resultado Esperado:**
O programa retorna uma mensagem dizendo se o número informado está ou não na sequência de Fibonacci.

---

## Exercício 3: Faturamento Diário de uma Distribuidora

### Descrição:
Dado o faturamento diário de uma distribuidora durante o mês, o programa deve calcular:
- O menor valor de faturamento ocorrido em um dia do mês.
- O maior valor de faturamento ocorrido.
- O número de dias em que o faturamento foi superior à média mensal.

### Objetivo:
- Processar os valores de faturamento de uma distribuidora.
- Calcular o menor e o maior faturamento, além de determinar quantos dias tiveram faturamento acima da média.

### Solução:
O programa utiliza dados de faturamento em formato JSON e realiza os cálculos necessários.

**Resultado Esperado:**
O programa retorna o menor e maior valor de faturamento, além do número de dias com faturamento acima da média.

---

## Exercício 4: Percentual de Representação de Cada Estado no Faturamento Total

### Descrição:
Dado o faturamento de uma distribuidora em diferentes estados, o programa deve calcular o percentual de faturamento de cada estado em relação ao faturamento total.

### Objetivo:
- Calcular a porcentagem que cada estado representa no faturamento total da distribuidora.

### Solução:
O programa recebe os valores de faturamento por estado, calcula o total e, em seguida, calcula o percentual de cada estado.

**Resultado Esperado:**
O programa retorna o percentual de faturamento de cada estado.

---

## Exercício 5: Inverter os Caracteres de uma String

### Descrição:
O programa deve inverter os caracteres de uma string fornecida. O objetivo é criar um algoritmo que realize a inversão de forma manual, sem utilizar funções prontas.

### Objetivo:
- Inverter uma string sem usar funções prontas como `reverse()`.

### Solução:
O código percorre a string de trás para frente e vai construindo uma nova string com os caracteres invertidos.

**Resultado Esperado:**
O programa retorna a string fornecida com os caracteres invertidos.

---

## Como Rodar os Exercícios

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/WesleyNovaes-Dev/TEstesTarget
