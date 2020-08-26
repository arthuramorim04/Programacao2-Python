class Atividade09():

    def input(self, string, numRep):
        print(string * numRep)

validator = Atividade09()
string = input("Digite a palavra que deseja repetir")
numRep = int(input("Digite a quantidade de repetições que deseja"))
validator.input(string,numRep)
