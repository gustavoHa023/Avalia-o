usuarios = []
def menu():
    print('1: Insira o nome do usuario: ')
    print('2: Insira seu cpf')
    print('3: Somar o cpf')
    

def adicionar_usuario():
    nome = input('Digite o nome do usuario: ')
    for usuario in usuarios:
        if usuario['nome'] == nome:
            print(f'Usuario {nome} ja existe')
            return
    usuarios.append({'nome': nome, 'cpf': []})
    print(f"Usuario {nome} adicionado")
            
def adicionar_cpf():
    nome = input('Digite o nome do usuario: ')
    cpf = input('Digite o cpf no formato 999.999.999.99: ')
    for usuario in usuarios:
        if usuario['nome'] == nome:
            usuario['cpf'].append(cpf)
            print(f'Cpf: {cpf} adicionado com sucesso')
        else:
            print("Nome não encontrado")

def somar_cpf():
    nome = input('Digite o nome do aluno: ')
    for usuario in usuarios:
        if usuario['nome'] == nome:
            if usuario['cpf']:
                soma = sum(usuario['cpf'])
                print(f"A nota final de {nome} é {soma}")
            else:
                print("Usuario não possui cpf")
            return
    print("Usuario não encontrado")

def main():
    while True:
        menu()
        opcao = input('Escolha uma opcao: ')
        
        if opcao == '1':
            adicionar_usuario()
        if opcao == '2':
            adicionar_cpf()
        if opcao == '3':
            somar_cpf()
        if opcao == '9':
            print("Adeus")
            break

if __name__ == "__main__":
    main()




    

