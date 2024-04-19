notasAlunos = open("notas_estudantes.dat", "r")
tamanho = 0
quantidadeNotas = []
for notaAluno in notasAlunos:
    aluno = notaAluno.split()
    contador = 0
    for i in range(1, len(aluno)):
        contador = contador +1
    if contador >=6:
        print(aluno[0])




