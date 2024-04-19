import customtkinter as ctk

def criarbotoes(Viewer):


    label_Nome = ctk.CTkLabel(Viewer.tab("Empresa"), text="Nome")
    entry_Nome = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_Nome.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
    entry_Nome.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")


    label_Situao = ctk.CTkLabel(Viewer.tab("Empresa"), text="Situação")
    entry_Situao = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_Situao.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
    entry_Situao.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")


    label_Identificao = ctk.CTkLabel(Viewer.tab("Empresa"), text="Identificação")
    entry_Identificao = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_Identificao.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")
    entry_Identificao.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")


    label_CNPJ = ctk.CTkLabel(Viewer.tab("Empresa"), text="CNPJ")
    entry_CNPJ = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_CNPJ.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")
    entry_CNPJ.grid(row=4, column=0, padx=10, pady=5, sticky="nsew")


    label_Tributao = ctk.CTkLabel(Viewer.tab("Empresa"), text="Tributação")
    entry_Tributao = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_Tributao.grid(row=4, column=0, padx=10, pady=5, sticky="nsew")
    entry_Tributao.grid(row=5, column=0, padx=10, pady=5, sticky="nsew")


    label_Data_abertura_ = ctk.CTkLabel(Viewer.tab("Empresa"), text="Data abertura (dd/mm/aaaa)")
    entry_Data_abertura_ = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_Data_abertura_.grid(row=5, column=0, padx=10, pady=5, sticky="nsew")
    entry_Data_abertura_.grid(row=6, column=0, padx=10, pady=5, sticky="nsew")


    label_Prefeitura = ctk.CTkLabel(Viewer.tab("Empresa"), text="Prefeitura")
    entry_Prefeitura = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_Prefeitura.grid(row=6, column=0, padx=10, pady=5, sticky="nsew")
    entry_Prefeitura.grid(row=7, column=0, padx=10, pady=5, sticky="nsew")


    label_Login = ctk.CTkLabel(Viewer.tab("Empresa"), text="Login")
    entry_Login = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_Login.grid(row=7, column=0, padx=10, pady=5, sticky="nsew")
    entry_Login.grid(row=8, column=0, padx=10, pady=5, sticky="nsew")


    label_Senha = ctk.CTkLabel(Viewer.tab("Empresa"), text="Senha")
    entry_Senha = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_Senha.grid(row=8, column=0, padx=10, pady=5, sticky="nsew")
    entry_Senha.grid(row=9, column=0, padx=10, pady=5, sticky="nsew")


    label_Pendncia_de_Recolhimentos = ctk.CTkLabel(Viewer.tab("Empresa"), text="Pendência de Recolhimentos")
    entry_Pendncia_de_Recolhimentos = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_Pendncia_de_Recolhimentos.grid(row=9, column=0, padx=10, pady=5, sticky="nsew")
    entry_Pendncia_de_Recolhimentos.grid(row=10, column=0, padx=10, pady=5, sticky="nsew")


    label_Entrega_de_DAS_Mensal = ctk.CTkLabel(Viewer.tab("Empresa"), text="Entrega de DAS Mensal")
    entry_Entrega_de_DAS_Mensal = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_Entrega_de_DAS_Mensal.grid(row=0, column=2, padx=10, pady=5, sticky="nsew")
    entry_Entrega_de_DAS_Mensal.grid(row=1, column=2, padx=10, pady=5, sticky="nsew")


    label_E_mail = ctk.CTkLabel(Viewer.tab("Empresa"), text="E-mail")
    entry_E_mail = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_E_mail.grid(row=1, column=2, padx=10, pady=5, sticky="nsew")
    entry_E_mail.grid(row=2, column=2, padx=10, pady=5, sticky="nsew")


    label_Pendncias = ctk.CTkLabel(Viewer.tab("Empresa"), text="Pendências")
    entry_Pendncias = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_Pendncias.grid(row=2, column=2, padx=10, pady=5, sticky="nsew")
    entry_Pendncias.grid(row=3, column=2, padx=10, pady=5, sticky="nsew")


    label_Observaes = ctk.CTkLabel(Viewer.tab("Empresa"), text="Observações")
    entry_Observaes = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_Observaes.grid(row=3, column=2, padx=10, pady=5, sticky="nsew")
    entry_Observaes.grid(row=4, column=2, padx=10, pady=5, sticky="nsew")


    label_CPF = ctk.CTkLabel(Viewer.tab("Empresa"), text="CPF")
    entry_CPF = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_CPF.grid(row=4, column=2, padx=10, pady=5, sticky="nsew")
    entry_CPF.grid(row=5, column=2, padx=10, pady=5, sticky="nsew")


    label_Cdigo_de_Acesso = ctk.CTkLabel(Viewer.tab("Empresa"), text="Código de Acesso")
    entry_Cdigo_de_Acesso = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_Cdigo_de_Acesso.grid(row=5, column=2, padx=10, pady=5, sticky="nsew")
    entry_Cdigo_de_Acesso.grid(row=6, column=2, padx=10, pady=5, sticky="nsew")


    label_Senha_GOV = ctk.CTkLabel(Viewer.tab("Empresa"), text="Senha GOV")
    entry_Senha_GOV = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_Senha_GOV.grid(row=6, column=2, padx=10, pady=5, sticky="nsew")
    entry_Senha_GOV.grid(row=7, column=2, padx=10, pady=5, sticky="nsew")


    label_Nvel_GOV = ctk.CTkLabel(Viewer.tab("Empresa"), text="Nível GOV")
    entry_Nvel_GOV = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_Nvel_GOV.grid(row=7, column=2, padx=10, pady=5, sticky="nsew")
    entry_Nvel_GOV.grid(row=8, column=2, padx=10, pady=5, sticky="nsew")


    label_Endereo = ctk.CTkLabel(Viewer.tab("Empresa"), text="Endereço")
    entry_Endereo = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_Endereo.grid(row=8, column=2, padx=10, pady=5, sticky="nsew")
    entry_Endereo.grid(row=9, column=2, padx=10, pady=5, sticky="nsew")


    label_Inscrio_Estadual = ctk.CTkLabel(Viewer.tab("Empresa"), text="Inscrição Estadual")
    entry_Inscrio_Estadual = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_Inscrio_Estadual.grid(row=9, column=2, padx=10, pady=5, sticky="nsew")
    entry_Inscrio_Estadual.grid(row=10, column=2, padx=10, pady=5, sticky="nsew")


    label_Inscrio_Municipal = ctk.CTkLabel(Viewer.tab("Empresa"), text="Inscrição Municipal")
    entry_Inscrio_Municipal = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_Inscrio_Municipal.grid(row=10, column=2, padx=10, pady=5, sticky="nsew")
    entry_Inscrio_Municipal.grid(row=11, column=2, padx=10, pady=5, sticky="nsew")


    label_Certificado_Digital = ctk.CTkLabel(Viewer.tab("Empresa"), text="Certificado Digital")
    entry_Certificado_Digital = ctk.CTkEntry(Viewer.tab("Empresa"))

    label_Certificado_Digital.grid(row=11, column=2, padx=10, pady=5, sticky="nsew")
    entry_Certificado_Digital.grid(row=12, column=2, padx=10, pady=5, sticky="nsew")


    label_Modelo_Datavix = ctk.CTkLabel(Viewer.tab("Contrato de Parceria"), text="Modelo Datavix")
    entry_Modelo_Datavix = ctk.CTkEntry(Viewer.tab("Contrato de Parceria"))

    label_Modelo_Datavix.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
    entry_Modelo_Datavix.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")


    label_Homologado___Sindicato = ctk.CTkLabel(Viewer.tab("Contrato de Parceria"), text="Homologado - Sindicato")
    entry_Homologado___Sindicato = ctk.CTkEntry(Viewer.tab("Contrato de Parceria"))

    label_Homologado___Sindicato.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
    entry_Homologado___Sindicato.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")


    label_Vencimento_ = ctk.CTkLabel(Viewer.tab("Contrato de Parceria"), text="Vencimento (dd/mm/aaaa)")
    entry_Vencimento_ = ctk.CTkEntry(Viewer.tab("Contrato de Parceria"))

    label_Vencimento_.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")
    entry_Vencimento_.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")


    label_Ano = ctk.CTkLabel(Viewer.tab("DASN"), text="Ano")
    entry_Ano = ctk.CTkEntry(Viewer.tab("DASN"))

    label_Ano.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
    entry_Ano.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")


    label_Faturamento = ctk.CTkLabel(Viewer.tab("DASN"), text="Faturamento")
    entry_Faturamento = ctk.CTkEntry(Viewer.tab("DASN"))

    label_Faturamento.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
    entry_Faturamento.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")


    label_Observaes = ctk.CTkLabel(Viewer.tab("DASN"), text="Observações")
    entry_Observaes = ctk.CTkEntry(Viewer.tab("DASN"))

    label_Observaes.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")
    entry_Observaes.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")

