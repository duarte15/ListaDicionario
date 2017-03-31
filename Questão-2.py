funcionarios = {}


def adicionarFuncionario(matricula, nome):

  funcionarios[matricula]=nome
 
def buscarFuncionario(matricula):

  print(funcionarios[matricula])

def exibirFuncionarios(funcionarios):

  print(funcionarios)



def main(Args=None):

    cont = "s"

    while (cont == 's'):

        op = int(input("O que deseja?\n1. Adicionar funcionario;\n2. Exibir funcionario;\n3. Exibir funcionarios;\n4. Sair.\n"))

        if (op == 1):

            matricula = int(input("Digite um número para matricula: "))

            nome = str(input("Digite o nome: "))

            adicionarFuncionario(matricula, nome)

        elif (op == 2):

            matricula = int(input("Digite matricula: "))

            buscarFuncionario(matricula)

        elif (op == 3):

            exibirFuncionarios(funcionarios)

        elif (op == 3):

            cont = "n"

        else:

            print("OPÇÃO INVÁLIDA!!")

if (__name__ == __name__):

  main()