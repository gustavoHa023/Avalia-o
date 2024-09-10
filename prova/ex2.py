alunos = []

def menu():
    print("1: Adicionar Aluno: ")
    print("2: Adicionar Nota: ")
    print('3: Média das notas: ')
    print("9: Sair")


def adicionar_aluno():
    nome = input("Digite o nome do aluno: ")
    for aluno in alunos:
        if aluno['nome'] == nome:
            print(f'O aluno {nome} ja existe')
            return
    alunos.append({'nome': nome, 'nota': []})
    print(f'Aluno {nome} adicionado com sucesso')

def adicionar_nota():
    nome = input("Digite o nome do aluno: ")
    nota = float(input('Digite a nota do aluno: '))
    for aluno in alunos:
        if aluno['nome'] == nome:
            if nota >= 0:
                aluno['nota'].append(nota)
                print(f'Adicionado a nota de {nota} para o aluno {nome}')
            else:
                print('Nota tem que ser maior ou igual a 0')
            return
        print("Aluno não encontrado")
        
def calc_media():
    nome = input('Digite o nome do aluno: ')
    for aluno in alunos:
        if aluno['nome'] == nome:
            if aluno['nota']:
                media = sum(aluno['nota']) /len(aluno['nota'])
                if media < 7:
                    print(f'Aluno reprovado com media {media}')
                else:
                    print("Aprovado")

            else:
                print("Aluno não possui notas")
            return
    print("Aluno não encontrado")



def main():
    while True:
        menu()
        opcao = input('Digite uma opção: ')

        if opcao == '1':
            adicionar_aluno()
        if opcao == '2':
            adicionar_nota()
        if opcao == '3':
            calc_media() 
        elif opcao == '9':
            print("Adeus...")
            break

if __name__ == '__main__':
    main()
