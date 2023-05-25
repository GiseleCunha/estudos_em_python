# > LISTAS

# Antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# Com lista
notas = [7.9, 9.7, 8.2]

# Criando Listas
lista = []
lista = list()
lista = [26, "Gisele", 3,14159, False]
lista_de_listas = [10, [1, 2, 3]]

# Indexação e Slices

lista = [10, 'Walisson', 3,14159, True]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
#print(lista[4])

print(lista[-1])

# Slices

lista = [10, 50, 30, 40, 25, 60, 5]


print(lista[0:3])
print(lista[3:6])
print(lista[3:])
print(lista[2:6:2])



# > Interações com FOR

# 1. Utilizando os próprios elementos da lista

for elemento in lista:
    print(elemento)

# 2. Utilizando os índices

print("Comprimento da lista:", len(lista))

for i in range(len(lista)):
    print(i)

# > Métodos de Listas

lista = [1, 3, 12, 8, 2 ]

#append
 
print("Antes do Append", lista)

lista.append(3)

print('Depois do Append:', lista)

# insert

lista.insert(2, 10)
print("Depois do insert:", lista)

# extend

lista2 = [4, 2, 3]

lista.extend(lista2)

print("Depois do extend: ", lista)

#pop 

lista.pop()

print("lista após o pop:", lista)

lista.pop(0)
print("lista após o pop:", lista)

# remove

lista.remove(3)

print("Depois do remove:", lista)

# count
print('Quantidade de 2  na lista', lista.count(2))

# index

print(' Índice do elemento 12:', lista.index(12))

# sort

lista.sort(reverse=True)
           
print(lista)

# Funções para listas

# len

print(len(lista))

# sum

print(sum(lista))

# max

print("O maior elemento da lista", max(lista))

# min

print("O menor elemento da lista", min(lista))