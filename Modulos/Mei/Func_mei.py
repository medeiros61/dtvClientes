from tkinter import *
import Modulos.Mei.Botoes_Edicao as btedit
import Modulos.Database.Logs as log
import Modulos.Mei.Mei_V_E as M_Tela_Edit

Evento_Contratante = f'Entrou na tela de cadastro de MEI Contratante'
obs_Contratante = ""

Evento_Parceira= f'Entrou na tela de cadastro de MEI Parceira'
obs_Parceira = ""

Evento_exportar= f'Exportando Listagem MEIS'
obs_exportar = ""

#FUNÇÃO PARA ADICIONAR
def Adicionar_MEI_Contratante(Dadosparateladeedição):

            
    frame_edição_dados = Dadosparateladeedição[0]
    Frame_atual = Dadosparateladeedição[1]
    M_Tela_Edit.definiçãotipodeentrada('Criação_Contratante')
    
    btedit.limparbotões()
    Frame_atual.pack_forget()
    frame_edição_dados.pack(side=RIGHT, fill = BOTH,expand=True) 

    btedit.preencher_tipo('Criar_Contratante',"")
    log.RegistrarEventosdeLOG(Evento_Contratante,obs_Contratante) 

#FUNÇÃO PARA ADICIONAR
def Adicionar_MEI_Parceira(Dadosparateladeedição,TreeView):
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
            nome_cliente = valores[1]
            btedit.id_empresa_Contratante(id)
            btedit.preencher_tipo('Criar_Parceira',nome_cliente)

    frame_edição_dados = Dadosparateladeedição[0]
    Frame_atual = Dadosparateladeedição[1]
    M_Tela_Edit.definiçãotipodeentrada('Criação_Parceira')
    btedit.limparbotões()
    Frame_atual.pack_forget()
    frame_edição_dados.pack(side=RIGHT, fill = BOTH,expand=True) 

    
    log.RegistrarEventosdeLOG(Evento_Parceira,obs_Parceira) 




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
                Evento= f'Excluindo MEI: [id:{id}] {nome_MEI}'
                obs = ""
                log.RegistrarEventosdeLOG(Evento,obs) 

            else:
                print("Nenhum MEI selecionado.")


#FUNÇÃO PARA EDITAR
def editar_MEI(TreeView,Dadosparateladeedição):
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
                btedit.Importardados(id,Dadosparateladeedição)
                Evento= f'Editando Cliente Planilha MEI: [id:{id}] {nome_cliente}'
                obs = ""
                log.RegistrarEventosdeLOG(Evento,obs) 
                M_Tela_Edit.definiçãotipodeentrada('Edição')
            else:
                print("Nenhum cliente selecionado.")

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
                Evento= f'Comentando Cliente Planilha MEI: [id:{id}] {nome_MEI}'
                obs = ""
                log.RegistrarEventosdeLOG(Evento,obs) 
            else:
                print("Nenhum MEI selecionado.")
#FUNÇÃO PARA EXCEL

def Exportar_MEIs():


    log.RegistrarEventosdeLOG(Evento_exportar,obs_exportar) 
         
