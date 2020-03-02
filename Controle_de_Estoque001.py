def controle_de_estoque():
    clientes = []
    produtos = []
    cliente_ativo = int
    
    def pagina_inicial():   
        print("__________________________________________")
        print("Quem é você?\n")
        print("1 - Novo usuário")
        print("2 - Usuário já cadastrado")
        print("3 - Investidor")
        
        tipo_de_usuario = int(input('Input:'))
        
        while tipo_de_usuario not in range(1 ,4):
            tipo_de_usuario = int(input("Input errado. Responder de 1 a 3: "))
            
        if tipo_de_usuario == 1:
            cadastrar_cliente()
        elif tipo_de_usuario == 2:
            identificacao_cliente()
        elif tipo_de_usuario == 3:
            print("adm")
      
    def cadastrar_cliente():
        print("\n\n__________________________________________\n\n")
        print("CADASTRO DE NOVO CLIENTE")
        nome = input("Digite seu nome: ")
        cliente_ativo = len(clientes)
        clientes.append([nome, 0])
        
        menu_cliente_existente()
    
    def cadastrar_item(item, quantidade):
        print("\n\n__________________________________________\n\n")
        print("CADASTRO DE PRODUTO")
        produto = input("Nome do produto: ")
        quantidade = input("Quantidade: ")
        produtos.append([produto, quantidade])
    
    def identificacao_cliente():
        print("\n\n__________________________________________\n\n")
        cliente = input("Digite seu nome: ")
        
        for i in range(len(clientes)):
            if cliente.lower() == clientes[i][0]:
                cliente_ativo = i
                print("é  cliente")
        
    def menu_cliente_existente():
        print("\n\n__________________________________________\n\n")
        print("Oque deseja fazer?")
        print("1 - Comprar")
        print("2 - Ver quantidade de itens comprados")
        
    def display_itens():
        print("v")
    
    pagina_inicial()

if __name__ == '__main__':
    controle_de_estoque()