turmas = {}


def adicionarTurma():

  nome = str(input("Nome da turma: "))

  alunos = {}

  turmas[nome] = alunos
  
def adicionarAlunoNotas():

  nomeTurma= str(input("Nome da turma:"))

  matricula=str(input("Matricula: "))

  notas=[]

  mais = 'Sim'

  while (mais =='Sim'):

    nota = float(input("Digite a nota: "))

    notas.append(nota)

    mais = str(input("Deseja inserir mais notas? "))

    turmas[nomeTurma][matricula] = notas



def calcularMedia(notas):

  soma = 0

  for x in notas:

    soma += x

  return soma/len(notas)


def calcularMediaTurma():

  soma = 0

  quantidadeDeTurmas = 0

  nomeTurma = str(input("Nome da turma: "))

  for x in turmas[nomeTurma]:

    soma += calcularMedia(turmas[nomeTurma][x])

    quantidadeDeTurmas += 1

  return soma/quantidadeDeTurmas


def consulta():

  op = int(input("1. Turmas;\n2. Alunos;\n3. Aluno;\n"))

  if(op == 1):

    print(turmas)

  elif(op == 2):

    nomeTurma= str(input("Nome da turma: "))

    print(turmas[nomeTurma])

  elif(op == 3):

    nomeTurma= str(input("Nome da turma: "))

    matr = str(input("Matricula do aluno: "))

    print(turmas[nomeTurma][matr])




def Menu():

  continuar = 'Sim'

  while (continuar == 'Sim'):

    opcao = int(input("O que deseja fazer?\n 1: Adicionar turma;\n 2: Adicionar aluno e notas;\n 3: Calcular média de um aluno;\n 4: Calcular média de um aluno;\n 5: Consutar os dados inseridos;\n 6: Sair.\n"))

    if (opcao ==  1):

      adicionarTurma()

    elif (opcao == 2):

      adicionarAlunoNotas()

    elif (opcao == 3):

      turma = str(input("Turma: "))

      matricula = str(input("Matricula: "))

      print(calcularMedia(turmas[turma][matricula]))

    elif (opcao == 4):

      print(calcularMediaTurma())

    elif (opcao == 5):
      consulta()
    
    elif (opcao == 6):
      continuar = 'Não'

    else:

      print("Opção inválida! Tente Novamente.\n")


Menu()