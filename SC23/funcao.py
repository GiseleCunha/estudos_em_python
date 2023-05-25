#Função
"""print()
input()
len()
max()"""

# 2. Criação de funções

#função inicial

"""def saudacao():
    print('Seja bem - vinda(a)!')
    print("Olá, é um prazer ter você fazendo parte desse curso!")

saudacao()

# Função com parâmetros

def saudacao(nome, curso):
    print(f'Seja bem - vinda(a), {nome}!')
    print(f"Olá, é um prazer ter você fazendo parte desse curso de {curso}!")

saudacao('Gisele', "Python")
saudacao('Aline', "JavaScript")

# Função com parâmetro default

def saudacao(nome, curso = "Python"):
    print(f'Seja bem - vinda(a), {nome}!')
    print(f"Olá, é um prazer ter você fazendo parte desse curso de {curso}!")

saudacao('Gisele', "C++")

# Função com retorno

def soma(num1, num2):
    return num1 + num2

resultado = soma(5, 7)"""

def calculadora(num1,num2,operacao="+"):
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2
    elif operacao == "/":
        return num1 / num2
    else:
        return "Operação Invalida! Por favor, digite (+), (-), (*), (/)"
    
"""o professor demostrou apenas os operadores de adição e subtração
 # os demais foram realizados segundo meus entendimento"""   

resultado = calculadora(10, 20, "l")

print(resultado)