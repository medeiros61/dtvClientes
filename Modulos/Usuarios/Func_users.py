from tkinter import *
import Modulos.Cliente.Botoes_Edicao as btedit
#FUNÇÃO PARA ADICIONAR
def Adicionar_cliente():

    print(f'Adicionando cliente')



#FUNÇÃO PARA EXCLUIR
def excluir_cliente(TreeView):
        # Obtém a seleção da TreeView
        selecao = TreeView.selection()
        # Verifica se há algum item selecionado
        if selecao:
            # Obtém as informações do item selecionado
            valores = TreeView.item(selecao[0])['values']
            # Verifica se há valores associados
            if valores:
                # Obtém o nome do cliente
                id = valores[0]
                nome_cliente = valores[1]
                # Agora você tem o nome do cliente selecionado
                print(f'Excluindo cliente: [id:{id}] {nome_cliente}')
            else:
                print("Nenhum cliente selecionado.")


#FUNÇÃO PARA EDITAR
def editar_cliente(TreeView,Dadosparateladeedição):
        # Obtém a seleção da TreeView
        selecao = TreeView.selection()
        # Verifica se há algum item selecionado
        if selecao:
            # Obtém as informações do item selecionado
            valores = TreeView.item(selecao[0])['values']
            # Verifica se há valores associados
            if valores:
                # Obtém o nome do cliente
                id = valores[0]
                nome_cliente = valores[1]
                frame_edição_dados = Dadosparateladeedição[0]
                Frame_atual = Dadosparateladeedição[1]
                Frame_atual.pack_forget()
                frame_edição_dados.pack(side=RIGHT, fill = BOTH,expand=True)
                #btedit.Importardados(id)
                # Agora você tem o nome do cliente selecionado
                print(f'Editando cliente: [id:{id}] {nome_cliente}')
            else:
                print("Nenhum cliente selecionado.")


#FUNÇÃO PARA COMENTAR
def comentar_cliente(TreeView):
        # Obtém a seleção da TreeView
        selecao = TreeView.selection()
        # Verifica se há algum item selecionado
        if selecao:
            # Obtém as informações do item selecionado
            valores = TreeView.item(selecao[0])['values']
            # Verifica se há valores associados
            if valores:
                # Obtém o nome do cliente
                id = valores[0]
                nome_cliente = valores[1]
                # Agora você tem o nome do cliente selecionado
                print(f'Comentando cliente: [id:{id}] {nome_cliente}')
            else:
                print("Nenhum cliente selecionado.")
#FUNÇÃO PARA EXCEL

def Exportar_clientes():

    print(f'Exportando clientes')