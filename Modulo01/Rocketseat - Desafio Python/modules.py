def adiciona_contato_agenda (agenda, nome, telefone, email, favorito):
    
    contato = {
        "nome_contato": nome,
        "telefone_contato": telefone,
        "email_contato": email,
        "favorito": False,
    }
    
    agenda.append(contato)
    print(f"\nContato {nome} adicionado na agenda")
    
    return

def visualiza_lista_contatos_cadastrados (agenda):
    print("\nLista de Contatos")
    for indice, agenda in enumerate (agenda, start=1):
        status = "✓" if agenda["favorito"] else " "
        nome_contato = agenda["nome_contato"]
        print(f"{indice}. [{status}] {nome_contato}")
        
    return

def marcar_desmarcar_contato_favorito (agenda, indice):
    indice_tarefa_ajustado = int(indice) - 1
    if agenda[indice_tarefa_ajustado]["favorito"] == True:
        agenda[indice_tarefa_ajustado]["favorito"] = False
        print(f"Contato {indice} removido dos favoritos")
    else:  
        agenda[indice_tarefa_ajustado]["favorito"] = True
        print(f"Contato {indice} atualizado para favorito")
    
    return

def editar_contato (agenda, indice, novo_nome, novo_telefone, novo_email):
    indice_tarefa_ajustado = int(indice) - 1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado <= len(agenda):
        contato_editado = agenda[indice_tarefa_ajustado]["nome_contato"]
        agenda[indice_tarefa_ajustado]["nome_contato"] = novo_nome
        agenda[indice_tarefa_ajustado]["telefone_contato"] = novo_telefone
        agenda[indice_tarefa_ajustado]["email_contato"] = novo_email
        print(f"O contato {indice}. {contato_editado} foi editado para o novo nome {novo_nome}, novo telefone {novo_telefone} e o novo e-mail {novo_email}")
    else:
        print("O indice informado não é um indice válido")
    return

def apagar_contato (agenda, indice):
    indice_tarefa_ajustado = int(indice) - 1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado <= len(agenda):
        contato_deletado = agenda[indice_tarefa_ajustado]["nome_contato"]
        agenda.remove(agenda[indice_tarefa_ajustado])
    print(f"O contato {contato_deletado} foi removido da sua agenda.")
    return