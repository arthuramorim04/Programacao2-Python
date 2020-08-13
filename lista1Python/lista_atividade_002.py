class Atividade02:

    def isNumberinRange(self,num):
        try:
            int(num)
        except ValueError:
            return False
        return True

    def aplication(self):
        num = input('Digte um numero inteiro de 1 até 5:')
        if Atividade02().isNumberinRange(num):
            numInt = int(num)
            if 6 > numInt > 0:
                return numInt
            return 'número inválido'
        return 'número inválido'

atividade = Atividade02()
print(atividade.aplication())