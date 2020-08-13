class Atividade01:

    def checkAdulthood(self, age):
        if age >= 18:
            return 'maior'
        return 'menor'

    def aplication(self):
        idade = int(input('digite a idade: '))
        if idade != None:
            return Atividade01().checkAdulthood(idade)
        return 0


atividade = Atividade01()
print(atividade.aplication())