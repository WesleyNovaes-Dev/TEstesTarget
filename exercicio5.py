# Exercício 5: Inverter os Caracteres de uma String

def inverter_string(s):
    resultado = ''
    for i in range(len(s) - 1, -1, -1):
        resultado += s[i]
    return resultado

# Entrada do usuário
entrada = input("Informe uma string para inverter: ")

# Resultado
print(f"A string invertida é: {inverter_string(entrada)}")
