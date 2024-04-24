Materia = input("Qual a matéria que você está consultando? ")
Nota_a1 = float(input("Qual é a sua nota da A1? "))
Nota_a2 = float(input("Qual é a sua nota da A2? "))

Recuperacao = 0

Media = Nota_a1 + Nota_a2

print("Sua média é de:", Media)

if Media >= 6:
    print(f'Parabéns, você está aprovado na matéria de {Materia}.')
else:
    TrabalhoRec = input("Teve trabalho de recuperação ou fez AF? (Sim/Não) ")
    if TrabalhoRec.lower() == "sim":
        Recuperacao = float(input("Insira a nota do trabalho de recuperação ou AF: "))
        Media += Recuperacao

        print("Sua média é de:", Media)

        if Media >= 6:
            print(f'Parabéns, você está aprovado na matéria de {Materia}.')
        else:
            print("Você não alcançou a média mínima. Estude mais.")
    elif TrabalhoRec.lower() == "não":
        print("Você reprovou. Estude mais.")

    