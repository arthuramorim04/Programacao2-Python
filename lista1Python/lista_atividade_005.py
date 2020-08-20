class Validator():
    def impar_par(self, numero):
        aux = numero % 2
        if aux == 0:
            print("Este númeor é par!")
        else:
            print("Esse núemro é ímpar!")

validator = Validator()
numero = int(input("Digite o númeor que você deseja validar: "))
validator.impar_par(numero)
