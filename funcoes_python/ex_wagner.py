lista_usuarios = []

lista_produtos = []




def menu():
    opcao = ""
    while opcao != "4":
        print("1 - Adicionar usuário no sistema")
        print("2 - Entrar no sistema")
        print("3 - Registrar alimentos")
        print("4 - sair")
        
        opcao = input("opcao: ")
        match(opcao):
            case "1":
                adicionar_usuario()
                
            case "2":
                criando_cadastro()
                
            case "3": 
                registro_alimentos()
                



def criando_cadastro():
    criacao_login = input("Digite login: ")
    criacao_senha = input("Digite sua senha: ")
    login = ""
    senha = ""


    while login != criacao_login or senha != criacao_senha:
        print("Digite o login e a senha novamente para acessar o painel de admin")
        login = input("Digite seu login: ")
        senha = input("Digite sua senha: ")








def registro_alimentos():
    dicionario_produtos = {}


    print("O titulo do produto deve possuir no mínimo 2 caracteres e a descrição no mínimo 5")

    titulo = input("Digite o titulo do produto: ")


    while len(titulo) < 2:
        print("O titulo do produto deve possuir no mínimo 2 caracteres")
        titulo = input("Digite o titulo do produto novamente: ")


    preco = float(input("Digite o preço do produto: ")) 
    descricao = input("Digite a descricao do produto: ")


    while len(descricao) < 5: 
        print("A descricao do produto deve possuir no mínimo 5 caracteres: ")
        descricao = input("Digite a descricao do produto: ")


    dicionario_produtos['titulo'] = titulo
    dicionario_produtos['preço'] = preco
    dicionario_produtos['descricao'] = descricao 

    lista_produtos.append(dicionario_produtos)

    print(lista_produtos)
    




def adicionar_usuario():
    dicionario_usuarios = {

    }

    
    email = input("Digite seu email: ")
    senha = input("Digite sua senha")

    dicionario_usuarios['email'] = email
    dicionario_usuarios['senha'] = senha

    lista_usuarios.append(dicionario_usuarios)
    print(lista_usuarios)
   

menu()