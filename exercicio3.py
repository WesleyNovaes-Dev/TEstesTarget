# Exercício 3: Faturamento Diário de uma Distribuidora

import json

# Faturamento diário em formato JSON (aqui como exemplo)
faturamento_json = '''
{
  "dias": [
    {"dia": 1, "faturamento": 1000},
    {"dia": 2, "faturamento": 2000},
    {"dia": 3, "faturamento": 1500},
    {"dia": 4, "faturamento": 500},
    {"dia": 5, "faturamento": 3000}
  ]
}
'''

# Convertendo o JSON para um dicionário Python
faturamento = json.loads(faturamento_json)

# Calculando os valores
valores_faturamento = [dia["faturamento"] for dia in faturamento["dias"]]
media_faturamento = sum(valores_faturamento) / len(valores_faturamento)
menor_faturamento = min(valores_faturamento)
maior_faturamento = max(valores_faturamento)

dias_acima_media = sum(1 for valor in valores_faturamento if valor > media_faturamento)

print(f"Menor faturamento: R${menor_faturamento}")
print(f"Maior faturamento: R${maior_faturamento}")
print(f"Dias acima da média: {dias_acima_media}")
