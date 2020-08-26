class Atividade():

    def input(selfp):
        listNotas = []
        for i in range(3):
            nota = float(input("entre com a nota "))
            listNotas.append(nota)
        Atividade().calc(listNotas)

    def calc(self, listNotas):
        soma = 0
        aux = 0
        for i in range(3):
            soma = aux + listNotas[i]
            aux = soma
        media = soma / 3

        if media >= 7:
            print("aluno aprovado")
        else:
            print("aluno reprovado")


validator = Atividade()
validator.input()
