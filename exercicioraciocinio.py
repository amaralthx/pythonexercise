estudantes = []
opcao = 0

def menu_principal():
  print("\n\n----- MENU PRINCIPAL -----\n")
  opcao = int(input ("1. Gerenciar estudantes.\n2. Gerenciar professores.\n3. Gerenciar disciplinas.\n4. Gerenciar turmas.\n5. Gerenciar matrículas.\n9. Sair.\n\nDigite uma opção e aperte Enter: "))
  return opcao

def menu_estudantes():
  print(f"\n***** [ESTUDANTES] MENU DE OPERAÇÕES *****\n")
  opcao = int(input ("\n1. Incluir\n2. Listar\n3. Atualizar\n4. Excluir\n9. Voltar ao menu principal.\n\nDigite uma opção e aperte Enter: "))
  #Oção para incluir estudante
  if opcao == 1:
    nome = input('Digite o nome do aluno: ')
    estudantes.append(nome)
  #Opção para listar estudantes utilizando FOR
  elif opcao == 2:
    if len(estudantes) == 0:
      print('Não há estudantes cadastrados !')
    else:
      for estudante in estudantes:
        print(estudante)
  #Opção de Atualizar estudante
  elif opcao == 3:
    print('Em desenvolvimento')
  #Opçaõ de Exlcuir estudante
  elif opcao == 4:
    print('Em desenvolvimento')
  elif opcao == 9:
    opcao = 0
    


def menu_professores():
  print(f"\n***** [PROFESSORES] MENU DE OPERAÇÕES *****\n")
  opcao = int(input ("\n1. Incluir\n2. Listar\n3. Atualizar\n4. Excluir\n9. Voltar ao menu principal.\n\nDigite uma opção e aperte Enter: "))
  if opcao == 1:
    print('Em desenvolvimento')
  elif opcao == 2:
    print('Em desenvolvimento')
  elif opcao == 3:
    print('Em desenvolvimento')
  elif opcao == 4:
    print('Em desenvolvimento')
  elif opcao == 9:
    opcao = 0

def menu_disciplinas():
  print(f"\n***** [DISCIPLINAS] MENU DE OPERAÇÕES *****\n")
  opcao = int(input ("\n1. Incluir\n2. Listar\n3. Atualizar\n4. Excluir\n9. Voltar ao menu principal.\n\nDigite uma opção e aperte Enter: "))
  if opcao == 1:
    print('Em desenvolvimento')
  elif opcao == 2:
    print('Em desenvolvimento')
  elif opcao == 3:
    print('Em desenvolvimento')
  elif opcao == 4:
    print('Em desenvolvimento')
  elif opcao == 9:
    opcao = 0

def menu_turmas():
  print(f"\n***** [TURMAS] MENU DE OPERAÇÕES *****\n")
  opcao = int(input ("\n1. Incluir\n2. Listar\n3. Atualizar\n4. Excluir\n9. Voltar ao menu principal.\n\nDigite uma opção e aperte Enter: "))
  if opcao == 1:
    print('Em desenvolvimento')
  elif opcao == 2:
    print('Em desenvolvimento')
  elif opcao == 3:
    print('Em desenvolvimento')
  elif opcao == 4:
    print('Em desenvolvimento')
  elif opcao == 9:
    opcao = 0

def menu_matriculas():
  print(f"\n***** [MATRICULAS] MENU DE OPERAÇÕES *****\n")
  opcao = int(input ("\n1. Incluir\n2. Listar\n3. Atualizar\n4. Excluir\n9. Voltar ao menu principal.\n\nDigite uma opção e aperte Enter: "))
  if opcao == 1:
    print('Em desenvolvimento')
  elif opcao == 2:
    print('Em desenvolvimento')
  elif opcao == 3:
    print('Em desenvolvimento')
  elif opcao == 4:
    print('Em desenvolvimento')
  elif opcao == 9:
    opcao = 0
    

#Início
while opcao != 9:
  opcao = menu_principal()
  if opcao == 1:
    menu_estudantes()
  elif opcao == 2:
    menu_professores()
  elif opcao == 3:
    menu_disciplinas()
  elif opcao == 4:
    menu_turmas()
  elif opcao == 5:
    menu_disciplinas()