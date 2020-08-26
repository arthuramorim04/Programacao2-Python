class Atividade06():
    def impar_par(self, numero):
        aux = numero % 2
        if aux == 0:
            print("Numero par")
        else:
            print("Numero ímpar")
    def posNeg(self, numero):
        if numero >= 0:
            print("Numero positivo")
        else:
            print("Numero negativo")

validator = Atividade06()
numero = int(input("Digite o númeor que você deseja validar: "))
validator.impar_par(numero)
validator.posNeg(numero)
