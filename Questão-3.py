produtos={}

def cadastrarProduto(produtos, produto, preco):

  produtos[produto]=preco

def exibirProdutos(listProdutos):

  for x in listProdutos:

    print("produto: ",x," preco: ",produtos[x])

def removerProduto(produtos, produto):

  del produtos[produto]

  print(produtos)

def exibirBaratoProduto(produtos):

  valid = False

  nome=''

  for x in produtos:

    if valid == False:

      menor = produtos[x]

      nome=x

      valid = True

    if produtos[x]<menor:

      menor=produtos[x]

      nome=x
  return nome

def exibirCaroProduto(produtos):

  maior=0

  for x in produtos:

    if produtos[x]> maior:

      maior=produtos[x]

      nome = x

  return x

def menu():

  cont = 's'

  while (cont == 's'):

    op = int(input("O que deseja?\n1. Adicionar\n2. Exibir produtos\n3. Excluir\n4. Exibir mais caro\n5. Exibir mais barato\n6. Sair.\n"))

    if (op == 1):

      produto = str(input("Digite nome do produto: "))

      preco = float(input("Digite o preco: "))

      cadastrarProduto(produtos,produto, preco)

    elif (op == 2):

      conti = 's'

      listProdutos=[]

      while (conti == 's'):

        prod = str(input("nome do produto "))

        listProdutos.append(prod)

        conti = str(input("Mais? "))

      exibirProdutos(listProdutos)

    elif (op == 3):

      prod = str(input("nome do produto "))

      removerProduto(produtos, produto)

    elif (op == 4):

      print(exibirCaroProduto(produtos))

    elif (op == 5):

      print(exibirBaratoProduto(produtos))

    elif (op == 6):

      cont = "n"

      print("OBRIGADO!")

    else:

      print("OPÇÃO INVÁLIDA!!")


menu()
