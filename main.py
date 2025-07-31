# 6. Eliminação de Duplicatas
# Objetivo: Dada uma lista de emails, remover todos os duplicados.
emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]

emails_unicos = list(set(emails))
print(emails_unicos)

# 7. Filtragem de Dados
# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

idades = [22, 15, 30, 17, 18]

idades_validas = [idade for idade in idades if idade >= 18]

print(idades_validas)

# 8. Ordenação Personalizada
# Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

pessoas = [
    {"nome": "carol", "idade": 30},
    {"nome": "Bob", "idade": 25},
    {"nome": "Alice", "idade": 20}
]
print(pessoas)
# Ordenação crescente (sem modificar a lista original)
pessoas_ordem_crescente = sorted(pessoas, key=lambda pessoa: pessoa["nome"])

# Ordenação decrescente (sem modificar a lista original)
pessoas_ordem_decrescente = sorted(pessoas, key=lambda pessoa: pessoa["nome"], reverse=True)

print(pessoas_ordem_crescente)
print(pessoas_ordem_decrescente)

# 9. Agregação de Dados
# Objetivo: Dado um conjunto de números, calcular a média.

numeros = [10,20,30]

media = sum(numeros)/len(numeros)

print(media)

# 10. Divisão de Dados em Grupos
# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = [valor for valor in valores if valor % 2 == 0]

impares = [valor for valor in valores if valor % 2 != 0]

print(f"valores pares {pares}")
print(f"valores impares {impares}")

# 12. Fusão de Dicionários
# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.

dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"c": 3, "d": 4}

dicionario_fundido = {**dicionario1, **dicionario2}

print(dicionario_fundido)

# 13. Filtragem de Dados em Dicionário
# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

estoque_positivo = {produto : quantidade for produto, quantidade in estoque.items() if quantidade > 0}

print(estoque_positivo)

# 14. Extração de Chaves e Valores
# Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.

dicionario = {"a": 1, "b": 2, "c": 3}

chaves = list(dicionario.keys())

valores = list(dicionario.values())

print(chaves)
print(valores)


# 15. Contagem de Frequência de Itens
# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.

texto = "engenharia de dados"
frequencia = {}
texto_s_espaco = texto.replace(" ", "")
print(texto_s_espaco)

for caractere in texto_s_espaco :
    try:
        if caractere in frequencia:
            frequencia[caractere] += 1
        else:
            frequencia[caractere] = 1
    except ValueError as e:
        print(e)

print(frequencia)