dias = {}

def adicionarDia(posicao):
    if(posicao >= 1 and posicao <= 7):
        dia = str(input("Digite o dia da semana para ser adicionado: "))
        dias[posicao] = dia
        print(dias)
    else:
        print("A semana tem apenas 7 dias!")
    
    return dias

def exibirDias(dias):
    for d in dias:
        print("Dia: ", d,"\n")


def main(Args=None):
    cont = "s"
    while (cont == 's'):
        op = int(input("O que deseja?\n1. Adicionar dia � semana.\n2. Exibir dias da semana.\n3. Sair.\n"))
        if (op == 1):
            posicao = int(input("Digite um n�mero para a posi��o: "))

            adicionarDia(posicao)
        elif (op == 2):
            exibirDias(dias)
        elif (op == 3):
            cont = "n"
            print("OBRIGADO!")
        else:
            print("OP��O INV�LIDA!!")
            
if(__name__ == __name__):
  main()