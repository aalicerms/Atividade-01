qtd_turmas = int(input("Insira a quantidade de turmas: "))
alunos_total = 0


for i in range(qtd_turmas):
    alunos_turma = int(input(f"Insira a quantidade de alunos na turma {i}: "))
    if alunos_turma > 40:
        print("Número maior que 40.")
    else:
        alunos_total += alunos_turma
        media = alunos_total / qtd_turmas
        print(f"A média de alunos por turma é {media}")

