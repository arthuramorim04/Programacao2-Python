class Atividade03:

    def aplicacao(self):
        val1 = float(input('digite o primeiro valor: '))
        val2 = float(input('digite o segundo valor: '))

        print(Atividade03().soma(val1, val2))
        print(Atividade03().subtracao(val1, val2))
        print(Atividade03().multiplicacao(val1, val2))
        print(Atividade03().divisao(val1, val2))

    def soma(self, val1, val2):
        return val1 + val2

    def subtracao(self, val1, val2):
        return val1 - val2

    def multiplicacao(self, val1, val2):
        return val1 * val2

    def divisao(self, val1, val2):
        return val1 / val2


atividade = Atividade03()
atividade.aplicacao()
