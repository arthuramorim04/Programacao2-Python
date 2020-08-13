class Atividade04:

    def troco(self):
        valRecebido = float(input('digite o valor que sera pago: '))
        valProduto = float(input('digite o valor do produto: '))

        valTroco = valRecebido - valProduto

        if valTroco >= 0:
            return print(valTroco)
        return print("Valor pago é menor que o valor do produto")


atividade = Atividade04()
atividade.troco()
