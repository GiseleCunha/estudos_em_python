# DICIONÁRIOS

# Crindo dicionários

dicionario = {}
dicionario = dict()

dicionario = {"nome": "Gisele","idade": 28,"altura": 1.77}

print(dicionario)
print(dicionario["idade"])

# Adicionando elementos em um dicionário

dicionario["programdor"] = True

print(dicionario)

dicionario["altura"] = 2
print(dicionario)

# Iterando sobre um dicionário

for chave in dicionario:
    print(chave, dicionario[chave])

# Testando a existência  de uma chave

print("peso" in dicionario)
print("altura" in dicionario)
