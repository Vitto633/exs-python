notasAlunos = open("notas_estudantes.dat")
for notaAluno in notasAlunos:
    aluno = notaAluno.split()
    menorValor = aluno[1]
    maiorValor = aluno[1]
    for i in range(1, len(aluno)):
        if int(aluno[i]) > int(maiorValor):
            maiorValor = int(aluno[i])
        if int(aluno[i]) < int(menorValor):
            menorValor = int(aluno[i])
    print(aluno[0], menorValor, maiorValor)
