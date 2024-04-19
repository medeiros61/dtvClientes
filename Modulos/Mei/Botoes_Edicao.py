import customtkinter as ctk
import Modulos.Database.Meis as dbm

def criarbotoes(Viewer):
    global entry_Nome,entry_Situao,entry_Identificao,entry_CNPJ,entry_Tributao,entry_Data_abertura_,entry_Prefeitura,entry_Login,entry_Senha,entry_Pendncia_de_Recolhimentos,entry_Entrega_de_DAS_Mensal,entry_E_mail,entry_Pendncias,entry_Observaes,entry_CPF,entry_Cdigo_de_Acesso,entry_Senha_GOV,entry_Nvel_GOV,entry_Endereo,entry_Inscrio_Estadual,entry_Inscrio_Municipal,entry_Certificado_Digital,entry_Modelo_Datavix,entry_Homologado___Sindicato,entry_Vencimento_,entry_Ano,entry_Faturamento

    yes_or_not = [
        "SIM","NÃO"
    ]

    label_Nome = ctk.CTkLabel(Viewer.tab("Empresa"), text="Nome")
    entry_Nome = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_Nome.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
    entry_Nome.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")


    label_Situao = ctk.CTkLabel(Viewer.tab("Empresa"), text="Ativo")
    entry_Situao = ctk.CTkComboBox(Viewer.tab("Empresa"),values=yes_or_not)

    label_Situao.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
    entry_Situao.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")


    label_Identificao = ctk.CTkLabel(Viewer.tab("Empresa"), text="Identificação")
    entry_Identificao = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_Identificao.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")
    entry_Identificao.grid(row=2, column=1, padx=10, pady=5, sticky="nsew")


    label_CNPJ = ctk.CTkLabel(Viewer.tab("Empresa"), text="CNPJ")
    entry_CNPJ = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_CNPJ.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")
    entry_CNPJ.grid(row=3, column=1, padx=10, pady=5, sticky="nsew")


    label_Tributao = ctk.CTkLabel(Viewer.tab("Empresa"), text="Tributação")
    entry_Tributao = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_Tributao.grid(row=4, column=0, padx=10, pady=5, sticky="nsew")
    entry_Tributao.grid(row=4, column=1, padx=10, pady=5, sticky="nsew")


    label_Data_abertura_ = ctk.CTkLabel(Viewer.tab("Empresa"), text="Data abertura (dd/mm/aaaa)")
    entry_Data_abertura_ = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_Data_abertura_.grid(row=5, column=0, padx=10, pady=5, sticky="nsew")
    entry_Data_abertura_.grid(row=5, column=1, padx=10, pady=5, sticky="nsew")


    label_Prefeitura = ctk.CTkLabel(Viewer.tab("Empresa"), text="Prefeitura")
    entry_Prefeitura = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_Prefeitura.grid(row=6, column=0, padx=10, pady=5, sticky="nsew")
    entry_Prefeitura.grid(row=6, column=1, padx=10, pady=5, sticky="nsew")


    label_Login = ctk.CTkLabel(Viewer.tab("Empresa"), text="Login")
    entry_Login = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_Login.grid(row=7, column=0, padx=10, pady=5, sticky="nsew")
    entry_Login.grid(row=7, column=1, padx=10, pady=5, sticky="nsew")


    label_Senha = ctk.CTkLabel(Viewer.tab("Empresa"), text="Senha")
    entry_Senha = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_Senha.grid(row=8, column=0, padx=10, pady=5, sticky="nsew")
    entry_Senha.grid(row=8, column=1, padx=10, pady=5, sticky="nsew")


    label_Pendncia_de_Recolhimentos = ctk.CTkLabel(Viewer.tab("Empresa"), text="Pendência de Recolhimentos")
    entry_Pendncia_de_Recolhimentos = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_Pendncia_de_Recolhimentos.grid(row=9, column=0, padx=10, pady=5, sticky="nsew")
    entry_Pendncia_de_Recolhimentos.grid(row=9, column=1, padx=10, pady=5, sticky="nsew")


    label_Entrega_de_DAS_Mensal = ctk.CTkLabel(Viewer.tab("Empresa"), text="Entrega de DAS Mensal")
    entry_Entrega_de_DAS_Mensal = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_Entrega_de_DAS_Mensal.grid(row=0, column=2, padx=10, pady=5, sticky="nsew")
    entry_Entrega_de_DAS_Mensal.grid(row=0, column=3, padx=10, pady=5, sticky="nsew")


    label_E_mail = ctk.CTkLabel(Viewer.tab("Empresa"), text="E-mail")
    entry_E_mail = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_E_mail.grid(row=1, column=2, padx=10, pady=5, sticky="nsew")
    entry_E_mail.grid(row=1, column=3, padx=10, pady=5, sticky="nsew")


    label_Pendncias = ctk.CTkLabel(Viewer.tab("Empresa"), text="Pendências")
    entry_Pendncias = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_Pendncias.grid(row=2, column=2, padx=10, pady=5, sticky="nsew")
    entry_Pendncias.grid(row=2, column=3, padx=10, pady=5, sticky="nsew")


    label_Observaes = ctk.CTkLabel(Viewer.tab("Empresa"), text="Observações")
    entry_Observaes = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_Observaes.grid(row=3, column=2, padx=10, pady=5, sticky="nsew")
    entry_Observaes.grid(row=3, column=3, padx=10, pady=5, sticky="nsew")


    label_CPF = ctk.CTkLabel(Viewer.tab("Empresa"), text="CPF")
    entry_CPF = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_CPF.grid(row=4, column=2, padx=10, pady=5, sticky="nsew")
    entry_CPF.grid(row=4, column=3, padx=10, pady=5, sticky="nsew")


    label_Cdigo_de_Acesso = ctk.CTkLabel(Viewer.tab("Empresa"), text="Código de Acesso")
    entry_Cdigo_de_Acesso = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_Cdigo_de_Acesso.grid(row=5, column=2, padx=10, pady=5, sticky="nsew")
    entry_Cdigo_de_Acesso.grid(row=5, column=3, padx=10, pady=5, sticky="nsew")


    label_Senha_GOV = ctk.CTkLabel(Viewer.tab("Empresa"), text="Senha GOV")
    entry_Senha_GOV = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_Senha_GOV.grid(row=6, column=2, padx=10, pady=5, sticky="nsew")
    entry_Senha_GOV.grid(row=6, column=3, padx=10, pady=5, sticky="nsew")


    label_Nvel_GOV = ctk.CTkLabel(Viewer.tab("Empresa"), text="Nível GOV")
    entry_Nvel_GOV = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_Nvel_GOV.grid(row=7, column=2, padx=10, pady=5, sticky="nsew")
    entry_Nvel_GOV.grid(row=7, column=3, padx=10, pady=5, sticky="nsew")


    label_Endereo = ctk.CTkLabel(Viewer.tab("Empresa"), text="Endereço")
    entry_Endereo = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_Endereo.grid(row=8, column=2, padx=10, pady=5, sticky="nsew")
    entry_Endereo.grid(row=8, column=3, padx=10, pady=5, sticky="nsew")


    label_Inscrio_Estadual = ctk.CTkLabel(Viewer.tab("Empresa"), text="Inscrição Estadual")
    entry_Inscrio_Estadual = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_Inscrio_Estadual.grid(row=9, column=2, padx=10, pady=5, sticky="nsew")
    entry_Inscrio_Estadual.grid(row=9, column=3, padx=10, pady=5, sticky="nsew")


    label_Inscrio_Municipal = ctk.CTkLabel(Viewer.tab("Empresa"), text="Inscrição Municipal")
    entry_Inscrio_Municipal = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_Inscrio_Municipal.grid(row=10, column=2, padx=10, pady=5, sticky="nsew")
    entry_Inscrio_Municipal.grid(row=10, column=3, padx=10, pady=5, sticky="nsew")


    label_Certificado_Digital = ctk.CTkLabel(Viewer.tab("Empresa"), text="Certificado Digital")
    entry_Certificado_Digital = ctk.CTkComboBox(Viewer.tab("Empresa"),values=yes_or_not)

    label_Certificado_Digital.grid(row=11, column=2, padx=10, pady=5, sticky="nsew")
    entry_Certificado_Digital.grid(row=11, column=3, padx=10, pady=5, sticky="nsew")


    label_Modelo_Datavix = ctk.CTkLabel(Viewer.tab("Contrato de Parceria"), text="Modelo Datavix")
    entry_Modelo_Datavix = ctk.CTkEntry(Viewer.tab("Contrato de Parceria"))

    label_Modelo_Datavix.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
    entry_Modelo_Datavix.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")


    label_Homologado___Sindicato = ctk.CTkLabel(Viewer.tab("Contrato de Parceria"), text="Homologado - Sindicato")
    entry_Homologado___Sindicato = ctk.CTkEntry(Viewer.tab("Contrato de Parceria"))

    label_Homologado___Sindicato.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
    entry_Homologado___Sindicato.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")


    label_Vencimento_ = ctk.CTkLabel(Viewer.tab("Contrato de Parceria"), text="Vencimento (dd/mm/aaaa)")
    entry_Vencimento_ = ctk.CTkEntry(Viewer.tab("Contrato de Parceria"))

    label_Vencimento_.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")
    entry_Vencimento_.grid(row=2, column=1, padx=10, pady=5, sticky="nsew")


    label_Ano_dasn = ctk.CTkLabel(Viewer.tab("DASN"), text="Ano")
    entry_Ano_dasn= ctk.CTkEntry(Viewer.tab("DASN"))

    label_Ano_dasn.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
    entry_Ano_dasn.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")


    label_Faturamento = ctk.CTkLabel(Viewer.tab("DASN"), text="Faturamento")
    entry_Faturamento = ctk.CTkEntry(Viewer.tab("DASN"))

    label_Faturamento.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
    entry_Faturamento.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")


    label_Observaes_dasn = ctk.CTkLabel(Viewer.tab("DASN"), text="Observações")
    entry_Observaes_dasn = ctk.CTkEntry(Viewer.tab("DASN"))

    label_Observaes_dasn.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")
    entry_Observaes_dasn.grid(row=2, column=1, padx=10, pady=5, sticky="nsew")


def Importardados(idcliente):
    Listadedados, identificadores,qr = dbm.getmeidata_toEdit(idcliente)
    

    entry_Nome.delete(0, 'end')
    entry_Nome.insert(0,Listadedados[3]) # Campo nome do banco de dados


    entry_Situao.set(Listadedados[2]) # Campo situacao do banco de dados

    entry_Identificao.delete(0, 'end')
    entry_Identificao.insert(0,Listadedados[4]) # Campo identificacao do banco de dados

    entry_CNPJ.delete(0, 'end')
    entry_CNPJ.insert(0,Listadedados[5]) # Campo cnpj do banco de dados

    entry_Tributao.delete(0, 'end')
    entry_Tributao.insert(0,Listadedados[6]) # Campo tributacao do banco de dados

    entry_Data_abertura_.delete(0, 'end')
    entry_Data_abertura_.insert(0,Listadedados[7]) # Campo data_abertura do banco de dados

    entry_Prefeitura.delete(0, 'end')
    entry_Prefeitura.insert(0,Listadedados[8]) # Campo prefeitura do banco de dados

    entry_Login.delete(0, 'end')
    entry_Login.insert(0,Listadedados[9]) # Campo login do banco de dados

    entry_Senha.delete(0, 'end')
    entry_Senha.insert(0,Listadedados[10]) # Campo senha do banco de dados

    entry_Pendncia_de_Recolhimentos.delete(0, 'end')
    entry_Pendncia_de_Recolhimentos.insert(0,Listadedados[11]) # Campo pendencia_recolhimentos do banco de dados

    entry_Entrega_de_DAS_Mensal.delete(0, 'end')
    entry_Entrega_de_DAS_Mensal.insert(0,Listadedados[12]) # Campo entrega_das_mensal do banco de dados

    entry_E_mail.delete(0, 'end')
    entry_E_mail.insert(0,Listadedados[14]) # Campo email do banco de dados

    entry_Pendncias.delete(0, 'end')
    entry_Pendncias.insert(0,Listadedados[13]) # Campo pendencias do banco de dados

    entry_Observaes.delete(0, 'end')
    entry_Observaes.insert(0,Listadedados[16]) # Campo observacoes do banco de dados

    entry_CPF.delete(0, 'end')
    entry_CPF.insert(0,Listadedados[17]) # Campo cpf do banco de dados

    entry_Cdigo_de_Acesso.delete(0, 'end')
    entry_Cdigo_de_Acesso.insert(0,Listadedados[18]) # Campo codigo_acesso do banco de dados

    entry_Senha_GOV.delete(0, 'end')
    entry_Senha_GOV.insert(0,Listadedados[19]) # Campo senha_gov do banco de dados

    entry_Nvel_GOV.delete(0, 'end')
    entry_Nvel_GOV.insert(0,Listadedados[20]) # Campo nivel_gov do banco de dados

    entry_Endereo.delete(0, 'end')
    entry_Endereo.insert(0,Listadedados[21]) # Campo endereco do banco de dados

    entry_Inscrio_Estadual.delete(0, 'end')
    entry_Inscrio_Estadual.insert(0,Listadedados[22]) # Campo inscricao_estadual do banco de dados

    entry_Inscrio_Municipal.delete(0, 'end')
    entry_Inscrio_Municipal.insert(0,Listadedados[23]) # Campo inscricao_municipal do banco de dados


    entry_Certificado_Digital.set(Listadedados[24]) # Campo certificado_digital do banco de dados

    entry_Modelo_Datavix.delete(0, 'end')
    entry_Modelo_Datavix.insert(0,Listadedados[25]) # Campo modelo_datavix do banco de dados

    entry_Homologado___Sindicato.delete(0, 'end')
    entry_Homologado___Sindicato.insert(0,Listadedados[26]) # Campo homologado_sindicato do banco de dados

    entry_Vencimento_.delete(0, 'end')
    entry_Vencimento_.insert(0,Listadedados[27]) # Campo vencimento do banco de dados

    #entry_Ano_dasn.delete(0, 'end')
    #entry_Ano_dasn.insert(0,Listadedados[28]) # Campo created_at do banco de dados

    #entry_Faturamento.delete(0, 'end')
    #entry_Faturamento.insert(0,Listadedados[29]) # Campo updated_at do banco de dados

    #entry_Observaes_dasn.delete(0, 'end')
    #entry_Observaes_dasn.insert(0,Listadedados[29]) # Campo updated_at do banco de dados