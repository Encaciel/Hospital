class Usuario:
    dic={}  #Define biblioteca global

    def __init__(self, nome, dtNas, filhos):    #Características do Usuário
        self.nome = nome
        self.dtNas = dtNas
        self.filhos = filhos

    def apresentar(self):   #Comportamentos do Usuário
        print(f"Olá, meu nome é {self.nome}. Nasci em {self.dtNas}.")

    def CadastrarUsuario(self): #Comportamento do Usuário
        dic[self.nome] = {"dataNas":self.dtNas, "qntFilhos":self.filhos}

    def ListarUsuario(nome):    #Comportamento do Usuário
        try:
            nomeEncontrado = dic[nome]
        except (KeyError):
            print("Nome não existente!")
        else:
            return nomeEncontrado
        finally:
            print("Operação concluída!")