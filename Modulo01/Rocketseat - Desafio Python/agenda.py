import modules

agenda = []

print("\nSeja bem-vindo a Agenda Pythonesca!")

while True:
    print("\nInforme a opção desejada:")
    print("1. Adicionar um Contato")
    print("2. Editar um Contato")
    print("3. Marcar/Desmarcar um Contato como favorito")
    print("4. Visualizar a lista de contatos")
    print("5. Apagar um contato")
    print("6. Fechar a agenda")
    
    choosedOption = int(input("Digite sua escolha:"))

    if choosedOption == 1:
        nome_contato = input("Digite o nome do contato a ser adicionado:")
        telefone_contato = input("Digite o número do telefone do contato:")
        email_contato = input("Digite o endereço de e-mail do contato:")
        favorito = False
        modules.adiciona_contato_agenda(agenda, nome_contato, telefone_contato, email_contato, favorito)
    elif choosedOption == 2:
        modules.visualiza_lista_contatos_cadastrados(agenda)
        indice_selecionado = input("Digite qual é o numero do contato que você deseja editar:")
        novo_nome = input("Digite o novo nome:")
        novo_telefone = input("Digite o novo telefone:")
        novo_email = input("Digite o novo e-mail:")
        modules.editar_contato(agenda, indice_selecionado, novo_nome, novo_telefone, novo_email)
    elif choosedOption == 3:
        modules.visualiza_lista_contatos_cadastrados(agenda)
        indice_selecionado = input("Digite qual o número do contato que você deseja favoritar/desfavoritar:")
        modules.marcar_desmarcar_contato_favorito(agenda, indice_selecionado)
    elif choosedOption == 4:
        modules.visualiza_lista_contatos_cadastrados(agenda)
    elif choosedOption == 5:
        modules.visualiza_lista_contatos_cadastrados(agenda)
        indice_selecionado = input("Digite qual o número do contato que você deseja apagar:")
        modules.apagar_contato(agenda, indice_selecionado)
        modules.visualiza_lista_contatos_cadastrados(agenda)
    elif choosedOption == 6:
        break
    
print("\n Agenda fechada com sucesso")