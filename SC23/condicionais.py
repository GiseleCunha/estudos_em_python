# ESTRUTURAS CONDICINAIS

idade = 18

if idade >= 18:
    print('Você é maior de idade.')
else: 
    print('Voce é menor de idade.')

    """Imagine que você queira imprimir "Aprovada(o), caso o estudante tenha uma média
        superrior ou igual a 7, e "Reprovado", caso a média seja inferior a 7
    """

media = float(input('Informe a média do estudante: '))

if media >= 7:
    print('Você foi Aprovada(o)!')
elif media >= 5:
    print('Recuperação')
else:
    print('Você foi Reprovado.')

media = 10
presenca = 100

if media >= 7 and presenca >= 70:
    print('Aprovada')
    print('Parabéns!')
else:
    print('Reprovado')
    print('Tente novamente')
