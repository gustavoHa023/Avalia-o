livros = []

def menu():
    print('1: Adicionar um livro: ')
    print('2: Listar os livros: ')
    print('3: Buscar por titulo: ')

def adicionar_livro():
    nome = input('Digite o nome do livro: ')
    autor = input('Digite o autor do livro: ')
    for livro in livros:
        if livro['nome'] == nome:
            print(f'Livro {nome} ja existe')
            return
    livros.append({'nome': nome, 'livro': autor})
    print(f"Livro {nome} autor:{autor} adicionado com sucesso! ")

def listar_livros():
    if livros:
        print("Os livros na bibilhoteca são: ")
        for livro in livros:
            print(livro['nome'])
        return
    print("Não há livros adicionados: ")

def buscar_livro_por_titulo():
    nome = input("Digite o nome do livro: ")
    for livro in livros:
        if livro['nome'] == nome:
            print(f'Livro: {nome} autor')
            return
    print("Livro não encontrado")

def main():
    while True:
        menu()
        opcao = input('Escolha uma opcao: ')
        
        if opcao == '1':
            adicionar_livro()
        if opcao == '2':
            listar_livros()
        if opcao == '3':
            buscar_livro_por_titulo()
        if opcao == '9':
            print("Adeus")
            break

if __name__ == "__main__":
    main()
