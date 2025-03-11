# Exercício 2: Verificação de um Número na Sequência de Fibonacci

def verificar_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num

# Número informado
numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

if verificar_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
