notasAlunos = open("notas_estudantes.dat")

for notaAluno in notasAlunos:
    aluno = notaAluno.split()
    soma = 0
    media = 0
    for i in range(1, len(aluno)):
        soma = soma + int(aluno[i])
    media = soma/len(aluno)
    print(aluno[1], media)