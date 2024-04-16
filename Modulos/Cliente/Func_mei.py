#FUNÇÃO PARA ADICIONAR
def Adicionar_MEI_Contratante():

    print(f'Adicionando MEI Contratante')

#FUNÇÃO PARA ADICIONAR
def Adicionar_MEI_Parceira():

    print(f'Adicionando MEI Parceira')


#FUNÇÃO PARA EXCLUIR
def excluir_MEI(TreeView):
        # Obtém a seleção da TreeView
        selecao = TreeView.selection()
        # Verifica se há algum item selecionado
        if selecao:
            # Obtém as informações do item selecionado
            valores = TreeView.item(selecao[0])['values']
            # Verifica se há valores associados
            if valores:
                # Obtém o nome do MEI
                id = valores[0]
                nome_MEI = valores[1]
                # Agora você tem o nome do MEI selecionado
                print(f'Excluindo MEI: [id:{id}] {nome_MEI}')
            else:
                print("Nenhum MEI selecionado.")
    #FUNÇÃO PARA EDITAR
def editar_MEI(TreeView):
        # Obtém a seleção da TreeView
        selecao = TreeView.selection()
        # Verifica se há algum item selecionado
        if selecao:
            # Obtém as informações do item selecionado
            valores = TreeView.item(selecao[0])['values']
            # Verifica se há valores associados
            if valores:
                # Obtém o nome do MEI
                id = valores[0]
                nome_MEI = valores[1]
                # Agora você tem o nome do MEI selecionado
                print(f'Editando MEI: [id:{id}] {nome_MEI}')
            else:
                print("Nenhum MEI selecionado.")
    #FUNÇÃO PARA COMENTAR
def comentar_MEI(TreeView):
        # Obtém a seleção da TreeView
        selecao = TreeView.selection()
        # Verifica se há algum item selecionado
        if selecao:
            # Obtém as informações do item selecionado
            valores = TreeView.item(selecao[0])['values']
            # Verifica se há valores associados
            if valores:
                # Obtém o nome do MEI
                id = valores[0]
                nome_MEI = valores[1]
                # Agora você tem o nome do MEI selecionado
                print(f'Comentando MEI: [id:{id}] {nome_MEI}')
            else:
                print("Nenhum MEI selecionado.")
#FUNÇÃO PARA EXCEL

def Exportar_MEIs():

    print(f'Exportando MEIs')