#ESTRUTURA CONDICIONAL

media = float(input("informe a media do estudante: "))
presenca = float(input("informe a presenca do aluno: "))

if media >= 7 and presenca >= 70:
    print('Aprovado!')
    print('Parabéns!')
elif media < 7 or presenca <70:
    print('recuperação')
    print('tente novamente')
else:
    print('Reprovado')
    print('Tente novamente')

