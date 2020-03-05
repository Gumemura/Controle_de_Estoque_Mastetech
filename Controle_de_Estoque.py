'''
O programa, apesar de incompleto, estrutra-se como numa linguagem de programaçõa modular, onde cada
função é uma página.

Consta no arquivo desse scrip um txt de nome 'controle' que contém uma amostra de clientes e produtos

Oque foi implementado no atual estado:
    função que capta informações da txt
    pagina inicial
    cadastro de novos usuários
    exibição de itens a venda

Principais elementos a serem implementados:
    alert caso nao seja encontrado o txt
    gravação de info no txt
    adição de itens no estoque
    adição de inventário individual de cada cliente
    
'''

import os

class estoque():
    def __init__(self):
        '''
        listas que armazenam, respectivamente, os clientes e os produtos disponiveis
        '''
        self.clientes = []
        self.produtos = []
        
        '''
        int que armazena o cliente ativo na sessão
        '''
        self.cliente_ativo = int
        
        self.file = open("controle.txt", "r+")

    def titulo_cena(self, titulo):
        '''
        print do titulo de cada página
        '''
        clear()
        print("_________________________________________")
        print(titulo)
        print("—————————————————————————————————————————\n")    
  
    def print_identificacao(self):
        '''
        print do cabeçalho com a identificação do cliente ativo
        '''
        clear()
        print("_________________________________________")
        print("Usuário: " + self.clientes[self.cliente_ativo][0].replace("_", " "))
        print("ID: " + str(self.clientes[self.cliente_ativo][2]))
        print("—————————————————————————————————————————\n")      

    def verifica_entrada(self, var, num_limite):
        '''
        Essa função verifica os inputs do usuário: ele veta a entrada de qualqeur tipo que não seja
        um inteiro, e, posteriormente, verifica se esse entra dentro do intervalo estipulado
        '''
        while True:
            try:
                int(var)
            except ValueError:
                var = input("Inserir apenas números de 1 a " + str(num_limite) + ": ")
            else:
                if int(var) in range(1 , num_limite):
                    return int(var)
                else:
                    var = input("Inserir apenas números de 1 a " + str(num_limite) + ": ")

    def leitura_txt(self):
        '''
        Essa é a primeira função que é chamada. Ela traduz as informações do txt para as listas
        declaradas no inicializador
        '''
        i_inicial = 0
        cliente = []
        add_estoque = False
        
        for line in self.file:
            if line[0] != "#":
                for i in range(len(line)):
                    if line[i] == " " or line[i] == "\n":
                        try:
                            int(line[i_inicial:i])
                        except ValueError:
                            cliente.append(line[i_inicial:i])
                        else:
                            cliente.append(int(line[i_inicial:i]))
                        i_inicial = i
                
                if add_estoque:
                    self.produtos.append((cliente).copy())
                else:
                    self.clientes.append((cliente).copy())
                cliente.clear()
                i_inicial = 0
            else:
                add_estoque = True
                
        self.pagina_inicial()

    def pagina_inicial(self):
        '''
        a página inicial, onde o usuário se identifica
        '''
        clear()
        print("1 - Novo cliente")
        print("2 - Cliente já cadastrado")
        print("3 - Investidor")
        
        usuario = input("Quem é você? ")
        usuario = self.verifica_entrada(usuario, 4)
        
    
        if usuario == 1:
            self.cadastrar_cliente()
        elif usuario == 2:
            self.identifica_cliente()
        elif usuario == 3:
            print("investidor")
    
    def cadastrar_cliente(self):
        '''
        cadastro de cliente. Cada cliente é inserido da lista global de clientes como uma lista, tendo
        essa três informações: o nome, quantidade de itens comprados, e seu index ocupado na lista global
        '''
        self.titulo_cena("Registro de cliente")
        nome = input("Insira nome completo: ")
        self.cliente_ativo = len(self.clientes)
        self.clientes.append([nome.replace(" ", "_"), 0, len(self.clientes)])
        
        self.menu_inicial_cliente()
    
    def identifica_cliente(self):
        '''
        Identifica o clietne ativo da sessão
        '''
        def verifica_id(var):
            while True:
                try:
                    int(var)
                except ValueError:  
                    var = input("Insira apeans números: ")
                else:
                    return int(var)
            
        self.titulo_cena("Identificação de cliente")
        
        id_cliente = input("Insira seu ID: ")
        id_cliente = verifica_id(id_cliente)

        for i in range(len(self.clientes)):
            if id_cliente == self.clientes[i][2]:
                self.cliente_ativo = i
                self.menu_inicial_cliente()
                break
            else:
                if i == len(self.clientes) - 1:
                    print("Cliente não identificado!")
                    print("Pressione ENTER para retornar ao menu inicial")
                    reset = input()
                    self.pagina_inicial()
                    break

    def menu_inicial_cliente(self):
        '''
        menu inicial do cliente
        '''
        self.print_identificacao()
        print("Olá, " + self.clientes[self.cliente_ativo][0].replace("_", " ") + "! Oque gostaria de fazer?")
        print("1 - Comprar")
        print("2 - Itens adquiridos")
        print("3 - Voltar ao menu inicial")
        
        input_menu_cliente = input("Oque deseja fazer?: ")
        input_menu_cliente = self.verifica_entrada(input_menu_cliente, 4)
        
        if input_menu_cliente == 1:
            self.lista_de_compras()
        elif input_menu_cliente == 2:
            print("hisotiroc")
        elif input_menu_cliente == 3:
            self.pagina_inicial()
    
    def lista_de_compras(self):
        '''
        dispõem ao usuário os itens a venda
        '''
        self.print_identificacao()
        print("Para comprar, insira o código do produto desejado (COD)")
        print("Para voltar ao menu, apenas pressione ENTER\n")
        print("COD\tPRODUTO\t\t\tESTOQUE")
        for i in range(len(self.produtos)):
            print(str(self.produtos[i][2]) + "\t" + self.produtos[i][0].replace("_", " ") + "\t\t\t" + str(self.produtos[i][1]))
        
        item_comprado = input(">:")
        item_comprado = self.verifica_entrada(item_comprado, len(self.produtos))
        
        if item_comprado  == "":
           self.menu_inicial_cliente()
        else:
            self.produtos[item_comprado][1] -= 1
        
        self.clientes[self.cliente_ativo].append([self.produtos[item_comprado][0], 1])
  
'''
função que limpa o CLI a cada chamada de função, ou a cada página
'''
clear = lambda: os.system('cls')

teste = estoque()
teste.leitura_txt()