class Atividade04:

    def troco(self):
        valDesconto = float(input('digite o valor do desconto: '))
        valProduto = float(input('digite o valor do produto: '))

        valFinal = valProduto - valDesconto

        if valFinal >= 0:
            return print("O valor final do produto é: ", valFinal)
        return print("Valor de desconto é maior que o valor do produto")


atividade = Atividade04()
atividade.troco()
