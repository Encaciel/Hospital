import Usuario as us

nome = input("Informe o nome do usuário: ")

dataNas = input("Informe a data de nascimento: ").strip()
dd = dataNas[0:2]
mm = dataNas[3:5]
aaaa = dataNas[6:]
dataNasf = "/".join([dd, mm, aaaa])

qntFilhos = int(input("Informe a quantidade de filhos: "))
if (qntFilhos <0):
    raise Exception("Quantidade de filhos inválido!")

user01 = us.Usuario(nome, dataNasf, qntFilhos)

user01.CadastrarUsuario
user01.Apresentar