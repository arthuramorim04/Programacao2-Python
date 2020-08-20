listaAlunos = []

class Aluno:
    def __init__(self, name, notas):
        self.name = name
        self.notas = notas

class Atividade01:

    def alunos(self, nomeAluno, notasAluno):
        self.name = nomeAluno
        self.notas = notasAluno

    def calcula(self):
        for x in range(2):
            alunos = listaAlunos[x]
            aux = 0
            total = 0

            for i in range(3):
                total = aux + alunos.notas[i]
                aux = total

            media = total / 3
            if media >= 7:
                print("\n ", alunos.name," está aprovado")
            else:
                print("\n ", alunos.name," foi reprovado")


    def input_alunos(self):
        instance = Atividade01()
        for x in range(2):
            notas = []
            name= input("Digite o nome do aluno: ")
            for i in range(3):
                nota = int(input("Digite a nota: "))
                notas.append(nota)

            aluno = Aluno(name, notas)
            listaAlunos.append(aluno)

        instance.calcula()


    def aplication(self):
        idade = int(input('digite a idade: '))
        if idade != None:
            return Atividade01().checkAdulthood(idade)
        return 0



atividade = Atividade01()
atividade.input_alunos()
