import numpy as np








class estoque():
    def __init__(self):
        self.clientes = []
        self.itens = []
        
    def pagina_inicial(self):   
        print("__________________________________________")
        print("Quem é você?\n")
        print("1 - Novo usuário")
        print("2 - Usuário já cadastrado")
        print("3 - Investidor")
        
        tipo_de_usuario = int(input('Input:'))
        
        while tipo_de_usuario not in range(1 ,4):
            tipo_de_usuario = int(input("Input errado. Responder de 1 a 3: "))
            
        if tipo_de_usuario == 1:
            self.cadastrar_cliente()
        elif tipo_de_usuario == 2:
            print("antigo")
        elif tipo_de_usuario == 3:
            print("adm")
      
    def cadastrar_cliente(self, nome):
        self.clientes.append([nome, 0])
    
    def cadastrar_item(self, item, quantidade):
        self.itens.append([item, quantidade])
        
    def display_itens(self):
        print()

def main():
    a = estoque()
    
main()