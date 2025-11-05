aluno = input("Digite o Nome do Aluno: ")
nota1 = float(input("Digite a Primeira Nota: "))
nota2 = float(input("Digite a Segunda Nota: "))

media = (nota1+ nota2) / 2

if media>= 7:
    print(f"Aluno: {aluno} Aprovado!\nMédia{media}")
elif media >= 4:
    print(f"Aluno: {aluno} Recuperação!\nMédia{media}")
else:
    print(f'Aluno: {aluno} Reprovado!\nMédia{media}')

