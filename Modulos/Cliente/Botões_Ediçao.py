import customtkinter as ctk
import tkinter
from tkinter import *

def criarbotoes(Viewer):

#------------------------------cliente
    label_Nome_empresa = ctk.CTkLabel(Viewer.tab("Cliente"), text="Nome empresa")
    entry_Nome_empresa = ctk.CTkEntry(Viewer.tab("Cliente"), width=200)

    label_Nome_empresa.grid(row=0, column=0,columnspan=2, padx=10, pady=1, sticky="w")
    entry_Nome_empresa.grid(row=1, column=0,columnspan=2, padx=10, pady=15, sticky="nsew")

    
    label_CNPJ = ctk.CTkLabel(Viewer.tab("Cliente"), text="CNPJ")
    entry_CNPJ = ctk.CTkEntry(Viewer.tab("Cliente"), width=200)

    label_CNPJ.grid(row=0, column=2, padx=10, pady=1, sticky="w")
    entry_CNPJ.grid(row=1, column=2, padx=10, pady=15, sticky="nsew")


    label_Estado = ctk.CTkLabel(Viewer.tab("Cliente"), text="Estado")
    entry_Estado = ctk.CTkComboBox(Viewer.tab("Cliente"))

    label_Estado.grid(row=2, column=0, padx=10, pady=1, sticky="w")
    entry_Estado.grid(row=3, column=0, padx=10, pady=15, sticky="nsew")
    #entry_Estado.grid(row=2, column=1, padx=10, pady=(5, 5), sticky="nsew")

    label_Municpio = ctk.CTkLabel(Viewer.tab("Cliente"), text="Município")
    entry_Municpio = ctk.CTkEntry(Viewer.tab("Cliente"))

    label_Municpio.grid(row=2, column=1, padx=10, pady=1, sticky="w")
    entry_Municpio.grid(row=3, column=1, padx=10, pady=15, sticky="nsew")


    label_Atividade = ctk.CTkLabel(Viewer.tab("Cliente"), text="Atividade")
    entry_Atividade = ctk.CTkEntry(Viewer.tab("Cliente"))

    label_Atividade.grid(row=2, column=2, padx=10, pady=1, sticky="w")
    entry_Atividade.grid(row=3, column=2, padx=10, pady=15, sticky="nsew")


    label_Data_abertura_ = ctk.CTkLabel(Viewer.tab("Cliente"), text="Data abertura (dd/mm/aaaa)")
    entry_Data_abertura_ = ctk.CTkEntry(Viewer.tab("Cliente"))

    label_Data_abertura_.grid(row=4, column=1, padx=10, pady=1, sticky="w")
    entry_Data_abertura_.grid(row=5, column=1, padx=10, pady=15, sticky="nsew")


    label_Ativo = ctk.CTkLabel(Viewer.tab("Cliente"), text="Ativo")
    entry_Ativo = ctk.CTkComboBox(Viewer.tab("Cliente"))

    label_Ativo.grid(row=4, column=2, padx=10, pady=1, sticky="w")
    entry_Ativo.grid(row=5, column=2, padx=10, pady=15, sticky="nsew")


    label_Link_WhatsApp = ctk.CTkLabel(Viewer.tab("Cliente"), text="Link WhatsApp")
    entry_Link_WhatsApp = ctk.CTkEntry(Viewer.tab("Cliente"))

    label_Link_WhatsApp.grid(row=4, column=0, padx=10, pady=1, sticky="w")
    entry_Link_WhatsApp.grid(row=5, column=0, padx=10, pady=15, sticky="nsew")

#------------------------------Gerais

    label_Formas_de_tributao = ctk.CTkLabel(Viewer.tab("Gerais"), text="Formas de tributação")
    entry_Formas_de_tributao = ctk.CTkComboBox(Viewer.tab("Gerais"), width=50)

    label_Formas_de_tributao.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
    entry_Formas_de_tributao.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")


    label_Anexo_simples_nacional = ctk.CTkLabel(Viewer.tab("Gerais"), text="Anexo simples nacional")
    entry_Anexo_simples_nacional = ctk.CTkEntry(Viewer.tab("Gerais"), width=50)

    label_Anexo_simples_nacional.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
    entry_Anexo_simples_nacional.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")


    label_Folha_de_pagamento = ctk.CTkLabel(Viewer.tab("Gerais"), text="Folha de pagamento")
    entry_Folha_de_pagamento = ctk.CTkComboBox(Viewer.tab("Gerais"), width=50)

    label_Folha_de_pagamento.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")
    entry_Folha_de_pagamento.grid(row=2, column=1, padx=10, pady=5, sticky="nsew")


    label_Responsvel_contabil = ctk.CTkLabel(Viewer.tab("Gerais"), text="Responsável contabil")
    entry_Responsvel_contabil = ctk.CTkEntry(Viewer.tab("Gerais"), width=50)

    label_Responsvel_contabil.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")
    entry_Responsvel_contabil.grid(row=3, column=1, padx=10, pady=5, sticky="nsew")


    label_Responsvel_fiscal = ctk.CTkLabel(Viewer.tab("Gerais"), text="Responsável fiscal")
    entry_Responsvel_fiscal = ctk.CTkEntry(Viewer.tab("Gerais"), width=50)

    label_Responsvel_fiscal.grid(row=4, column=0, padx=10, pady=5, sticky="nsew")
    entry_Responsvel_fiscal.grid(row=4, column=1, padx=10, pady=5, sticky="nsew")


    label_Responsvel_societrio = ctk.CTkLabel(Viewer.tab("Gerais"), text="Responsável societário")
    entry_Responsvel_societrio = ctk.CTkEntry(Viewer.tab("Gerais"), width=50)

    label_Responsvel_societrio.grid(row=5, column=0, padx=10, pady=5, sticky="nsew")
    entry_Responsvel_societrio.grid(row=5, column=1, padx=10, pady=5, sticky="nsew")


    label_Responsvel_DP = ctk.CTkLabel(Viewer.tab("Gerais"), text="Responsável DP")
    entry_Responsvel_DP = ctk.CTkEntry(Viewer.tab("Gerais"), width=50)

    label_Responsvel_DP.grid(row=6, column=0, padx=10, pady=5, sticky="nsew")
    entry_Responsvel_DP.grid(row=6, column=1, padx=10, pady=5, sticky="nsew")


    label_Domiclio_eletrnico = ctk.CTkLabel(Viewer.tab("Gerais"), text="Domicílio eletrônico")
    entry_Domiclio_eletrnico = ctk.CTkComboBox(Viewer.tab("Gerais"), width=50)

    label_Domiclio_eletrnico.grid(row=7, column=0, padx=10, pady=5, sticky="nsew")
    entry_Domiclio_eletrnico.grid(row=7, column=1, padx=10, pady=5, sticky="nsew")


    label_Email = ctk.CTkLabel(Viewer.tab("Gerais"), text="Email")
    entry_Email = ctk.CTkEntry(Viewer.tab("Gerais"), width=50)

    label_Email.grid(row=8, column=0, padx=10, pady=5, sticky="nsew")
    entry_Email.grid(row=8, column=1, padx=10, pady=5, sticky="nsew")


    label_Nome_representante = ctk.CTkLabel(Viewer.tab("Gerais"), text="Nome representante")
    entry_Nome_representante = ctk.CTkEntry(Viewer.tab("Gerais"), width=50)

    label_Nome_representante.grid(row=9, column=0, padx=10, pady=5, sticky="nsew")
    entry_Nome_representante.grid(row=9, column=1, padx=10, pady=5, sticky="nsew")


    label_CPF_representante_legal = ctk.CTkLabel(Viewer.tab("Gerais"), text="CPF representante legal")
    entry_CPF_representante_legal = ctk.CTkEntry(Viewer.tab("Gerais"), width=50)

    label_CPF_representante_legal.grid(row=0, column=2, padx=10, pady=5, sticky="nsew")
    entry_CPF_representante_legal.grid(row=0, column=3, padx=10, pady=5, sticky="nsew")


    label_Data_de_nascimento_ = ctk.CTkLabel(Viewer.tab("Gerais"), text="Data de nascimento (dd/mm/aaaa)")
    entry_Data_de_nascimento_ = ctk.CTkEntry(Viewer.tab("Gerais"), width=50)

    label_Data_de_nascimento_.grid(row=1, column=2, padx=10, pady=5, sticky="nsew")
    entry_Data_de_nascimento_.grid(row=1, column=3, padx=10, pady=5, sticky="nsew")


    label_Contabilidade_finalizada_ = ctk.CTkLabel(Viewer.tab("Gerais"), text="Contabilidade finalizada (dd/mm/aaaa)")
    entry_Contabilidade_finalizada_ = ctk.CTkEntry(Viewer.tab("Gerais"), width=50)

    label_Contabilidade_finalizada_.grid(row=2, column=2, padx=10, pady=5, sticky="nsew")
    entry_Contabilidade_finalizada_.grid(row=2, column=3, padx=10, pady=5, sticky="nsew")


    label_Certificado_digital = ctk.CTkLabel(Viewer.tab("Gerais"), text="Certificado digital")
    entry_Certificado_digital = ctk.CTkComboBox(Viewer.tab("Gerais"), width=50)

    label_Certificado_digital.grid(row=3, column=2, padx=10, pady=5, sticky="nsew")
    entry_Certificado_digital.grid(row=3, column=3, padx=10, pady=5, sticky="nsew")


    label_Senha_certificado = ctk.CTkLabel(Viewer.tab("Gerais"), text="Senha certificado")
    entry_Senha_certificado = ctk.CTkEntry(Viewer.tab("Gerais"), width=50)

    label_Senha_certificado.grid(row=4, column=2, padx=10, pady=5, sticky="nsew")
    entry_Senha_certificado.grid(row=4, column=3, padx=10, pady=5, sticky="nsew")


    label_Data_de_vencimento_ = ctk.CTkLabel(Viewer.tab("Gerais"), text="Data de vencimento (dd/mm/aaaa)")
    entry_Data_de_vencimento_ = ctk.CTkEntry(Viewer.tab("Gerais"), width=50)

    label_Data_de_vencimento_.grid(row=5, column=2, padx=10, pady=5, sticky="nsew")
    entry_Data_de_vencimento_.grid(row=5, column=3, padx=10, pady=5, sticky="nsew")

#------------------------------Federais

    label_Cdigo_e_cac = ctk.CTkLabel(Viewer.tab("Federais"), text="Código e-cac")
    entry_Cdigo_e_cac = ctk.CTkEntry(Viewer.tab("Federais"), width=200)

    label_Cdigo_e_cac.grid(row=0, column=0, padx=10, pady=15, sticky="nsew")
    entry_Cdigo_e_cac.grid(row=0, column=1, padx=10, pady=15, sticky="nsew")


    label_Senha_EAC = ctk.CTkLabel(Viewer.tab("Federais"), text="Senha EAC")
    entry_Senha_EAC = ctk.CTkEntry(Viewer.tab("Federais"), width=50)

    label_Senha_EAC.grid(row=1, column=0, padx=10, pady=15, sticky="nsew")
    entry_Senha_EAC.grid(row=1, column=1, padx=10, pady=15, sticky="nsew")


    label_Cdigo_Simples = ctk.CTkLabel(Viewer.tab("Federais"), text="Código Simples")
    entry_Cdigo_Simples = ctk.CTkEntry(Viewer.tab("Federais"), width=50)

    label_Cdigo_Simples.grid(row=2, column=0, padx=10, pady=15, sticky="nsew")
    entry_Cdigo_Simples.grid(row=2, column=1, padx=10, pady=15, sticky="nsew")


    label_Nmero_de_livros_ECD = ctk.CTkLabel(Viewer.tab("Federais"), text="Número de livros ECD")
    entry_Nmero_de_livros_ECD = ctk.CTkEntry(Viewer.tab("Federais"), width=50)

    label_Nmero_de_livros_ECD.grid(row=3, column=0, padx=10, pady=15, sticky="nsew")
    entry_Nmero_de_livros_ECD.grid(row=3, column=1, padx=10, pady=15, sticky="nsew")


    label_Ano_Nmero_de_livros_ECD = ctk.CTkLabel(Viewer.tab("Federais"), text="Ano Número de livros ECD")
    entry_Ano_Nmero_de_livros_ECD = ctk.CTkEntry(Viewer.tab("Federais"), width=50)

    label_Ano_Nmero_de_livros_ECD.grid(row=4, column=0, padx=10, pady=15, sticky="nsew")
    entry_Ano_Nmero_de_livros_ECD.grid(row=4, column=1, padx=10, pady=15, sticky="nsew")


    label_Nmero_de_livros_ECF = ctk.CTkLabel(Viewer.tab("Federais"), text="Número de livros ECF")
    entry_Nmero_de_livros_ECF = ctk.CTkEntry(Viewer.tab("Federais"), width=50)

    label_Nmero_de_livros_ECF.grid(row=5, column=0, padx=10, pady=15, sticky="nsew")
    entry_Nmero_de_livros_ECF.grid(row=5, column=1, padx=10, pady=15, sticky="nsew")


    label_Ano_Nmero_de_livros_ECF = ctk.CTkLabel(Viewer.tab("Federais"), text="Ano Número de livros ECF")
    entry_Ano_Nmero_de_livros_ECF = ctk.CTkEntry(Viewer.tab("Federais"), width=50)

    label_Ano_Nmero_de_livros_ECF.grid(row=6, column=0, padx=10, pady=15, sticky="nsew")
    entry_Ano_Nmero_de_livros_ECF.grid(row=6, column=1, padx=10, pady=15, sticky="nsew")

#------------------------------Estaduais

    label_Estado = ctk.CTkLabel(Viewer.tab("Estaduais"), text="Estado")
    entry_Estado = ctk.CTkComboBox(Viewer.tab("Estaduais"), width=200)

    label_Estado.grid(row=0, column=0, padx=10, pady=15, sticky="nsew")
    entry_Estado.grid(row=0, column=1, padx=10, pady=15, sticky="nsew")


    label_UF = ctk.CTkLabel(Viewer.tab("Estaduais"), text="UF")
    entry_UF = ctk.CTkEntry(Viewer.tab("Estaduais"), width=50)

    label_UF.grid(row=1, column=0, padx=10, pady=15, sticky="nsew")
    entry_UF.grid(row=1, column=1, padx=10, pady=15, sticky="nsew")


    label_Inscrio_estadual = ctk.CTkLabel(Viewer.tab("Estaduais"), text="Inscrição estadual")
    entry_Inscrio_estadual = ctk.CTkEntry(Viewer.tab("Estaduais"), width=50)

    label_Inscrio_estadual.grid(row=2, column=0, padx=10, pady=15, sticky="nsew")
    entry_Inscrio_estadual.grid(row=2, column=1, padx=10, pady=15, sticky="nsew")


    label_Credenciamento_NFE = ctk.CTkLabel(Viewer.tab("Estaduais"), text="Credenciamento NFE")
    entry_Credenciamento_NFE = ctk.CTkComboBox(Viewer.tab("Estaduais"), width=50)

    label_Credenciamento_NFE.grid(row=3, column=0, padx=10, pady=15, sticky="nsew")
    entry_Credenciamento_NFE.grid(row=3, column=1, padx=10, pady=15, sticky="nsew")


    label_Nmero_CSC = ctk.CTkLabel(Viewer.tab("Estaduais"), text="Número CSC")
    entry_Nmero_CSC = ctk.CTkEntry(Viewer.tab("Estaduais"), width=50)

    label_Nmero_CSC.grid(row=4, column=0, padx=10, pady=15, sticky="nsew")
    entry_Nmero_CSC.grid(row=4, column=1, padx=10, pady=15, sticky="nsew")


    label_Site_caixa_postal = ctk.CTkLabel(Viewer.tab("Estaduais"), text="Site caixa postal")
    entry_Site_caixa_postal = ctk.CTkEntry(Viewer.tab("Estaduais"), width=50)

    label_Site_caixa_postal.grid(row=5, column=0, padx=10, pady=15, sticky="nsew")
    entry_Site_caixa_postal.grid(row=5, column=1, padx=10, pady=15, sticky="nsew")


    label_Livros_Fiscais_Entrada_Ano_Nmero = ctk.CTkLabel(Viewer.tab("Estaduais"), text="Livros Fiscais Entrada Ano Número")
    entry_Livros_Fiscais_Entrada_Ano_Nmero = ctk.CTkEntry(Viewer.tab("Estaduais"), width=50)

    label_Livros_Fiscais_Entrada_Ano_Nmero.grid(row=6, column=0, padx=10, pady=15, sticky="nsew")
    entry_Livros_Fiscais_Entrada_Ano_Nmero.grid(row=6, column=1, padx=10, pady=15, sticky="nsew")


    label_Livros_Fiscais_Inventrio_Ano_Nmero = ctk.CTkLabel(Viewer.tab("Estaduais"), text="Livros Fiscais Inventário Ano Número")
    entry_Livros_Fiscais_Inventrio_Ano_Nmero = ctk.CTkEntry(Viewer.tab("Estaduais"), width=50)

    label_Livros_Fiscais_Inventrio_Ano_Nmero.grid(row=7, column=0, padx=10, pady=15, sticky="nsew")
    entry_Livros_Fiscais_Inventrio_Ano_Nmero.grid(row=7, column=1, padx=10, pady=15, sticky="nsew")

#------------------------------Municipais

    label_Inscrio_municipal = ctk.CTkLabel(Viewer.tab("Municipais"), text="Inscrição municipal")
    entry_Inscrio_municipal = ctk.CTkEntry(Viewer.tab("Municipais"), width=200)

    label_Inscrio_municipal.grid(row=0, column=0, padx=10, pady=15, sticky="nsew")
    entry_Inscrio_municipal.grid(row=0, column=1, padx=10, pady=15, sticky="nsew")


    label_Site = ctk.CTkLabel(Viewer.tab("Municipais"), text="Site")
    entry_Site = ctk.CTkEntry(Viewer.tab("Municipais"), width=50)

    label_Site.grid(row=1, column=0, padx=10, pady=15, sticky="nsew")
    entry_Site.grid(row=1, column=1, padx=10, pady=15, sticky="nsew")


    label_Login = ctk.CTkLabel(Viewer.tab("Municipais"), text="Login")
    entry_Login = ctk.CTkEntry(Viewer.tab("Municipais"), width=50)

    label_Login.grid(row=2, column=0, padx=10, pady=15, sticky="nsew")
    entry_Login.grid(row=2, column=1, padx=10, pady=15, sticky="nsew")


    label_Senha = ctk.CTkLabel(Viewer.tab("Municipais"), text="Senha")
    entry_Senha = ctk.CTkEntry(Viewer.tab("Municipais"), width=50)

    label_Senha.grid(row=3, column=0, padx=10, pady=15, sticky="nsew")
    entry_Senha.grid(row=3, column=1, padx=10, pady=15, sticky="nsew")


    label_Demais_senhas = ctk.CTkLabel(Viewer.tab("Municipais"), text="Demais senhas")
    entry_Demais_senhas = ctk.CTkEntry(Viewer.tab("Municipais"), width=50)

    label_Demais_senhas.grid(row=4, column=0, padx=10, pady=15, sticky="nsew")
    entry_Demais_senhas.grid(row=4, column=1, padx=10, pady=15, sticky="nsew")


    label_Senha_Abertura_Processos = ctk.CTkLabel(Viewer.tab("Municipais"), text="Senha Abertura Processos")
    entry_Senha_Abertura_Processos = ctk.CTkEntry(Viewer.tab("Municipais"), width=50)

    label_Senha_Abertura_Processos.grid(row=5, column=0, padx=10, pady=15, sticky="nsew")
    entry_Senha_Abertura_Processos.grid(row=5, column=1, padx=10, pady=15, sticky="nsew")


    label_Observaes = ctk.CTkLabel(Viewer.tab("Municipais"), text="Observações")
    entry_Observaes = ctk.CTkEntry(Viewer.tab("Municipais"), width=50)

    label_Observaes.grid(row=6, column=0, padx=10, pady=15, sticky="nsew")
    entry_Observaes.grid(row=6, column=1, padx=10, pady=15, sticky="nsew")

#------------------------------Societario

    label_Alvara_de_funcionamento = ctk.CTkLabel(Viewer.tab("Societário"), text="Alvara de funcionamento")
    entry_Alvara_de_funcionamento = ctk.CTkComboBox(Viewer.tab("Societário"), width=50)

    label_Alvara_de_funcionamento.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
    entry_Alvara_de_funcionamento.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")


    label_Data_vencimento_ = ctk.CTkLabel(Viewer.tab("Societário"), text="Data vencimento (dd/mm/aaaa)")
    entry_Data_vencimento_ = ctk.CTkEntry(Viewer.tab("Societário"), width=50)

    label_Data_vencimento_.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
    entry_Data_vencimento_.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")


    label_Alvara_sanitrio = ctk.CTkLabel(Viewer.tab("Societário"), text="Alvara sanitário")
    entry_Alvara_sanitrio = ctk.CTkComboBox(Viewer.tab("Societário"), width=50)

    label_Alvara_sanitrio.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")
    entry_Alvara_sanitrio.grid(row=2, column=1, padx=10, pady=5, sticky="nsew")


    label_Data_vencimento_ = ctk.CTkLabel(Viewer.tab("Societário"), text="Data vencimento (dd/mm/aaaa)")
    entry_Data_vencimento_ = ctk.CTkEntry(Viewer.tab("Societário"), width=50)

    label_Data_vencimento_.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")
    entry_Data_vencimento_.grid(row=3, column=1, padx=10, pady=5, sticky="nsew")


    label_Licenca_ambiental = ctk.CTkLabel(Viewer.tab("Societário"), text="Licença ambiental")
    entry_Licenca_ambiental = ctk.CTkComboBox(Viewer.tab("Societário"), width=50)

    label_Licenca_ambiental.grid(row=4, column=0, padx=10, pady=5, sticky="nsew")
    entry_Licenca_ambiental.grid(row=4, column=1, padx=10, pady=5, sticky="nsew")


    label_Data_vencimento_ = ctk.CTkLabel(Viewer.tab("Societário"), text="Data vencimento (dd/mm/aaaa)")
    entry_Data_vencimento_ = ctk.CTkEntry(Viewer.tab("Societário"), width=50)

    label_Data_vencimento_.grid(row=5, column=0, padx=10, pady=5, sticky="nsew")
    entry_Data_vencimento_.grid(row=5, column=1, padx=10, pady=5, sticky="nsew")


    label_Bombeiros = ctk.CTkLabel(Viewer.tab("Societário"), text="Bombeiros")
    entry_Bombeiros = ctk.CTkComboBox(Viewer.tab("Societário"), width=50)

    label_Bombeiros.grid(row=6, column=0, padx=10, pady=5, sticky="nsew")
    entry_Bombeiros.grid(row=6, column=1, padx=10, pady=5, sticky="nsew")


    label_Data_vencimento_ = ctk.CTkLabel(Viewer.tab("Societário"), text="Data vencimento (dd/mm/aaaa)")
    entry_Data_vencimento_ = ctk.CTkEntry(Viewer.tab("Societário"), width=50)

    label_Data_vencimento_.grid(row=7, column=0, padx=10, pady=5, sticky="nsew")
    entry_Data_vencimento_.grid(row=7, column=1, padx=10, pady=5, sticky="nsew")


    label_ltima_alterao_contratual_ = ctk.CTkLabel(Viewer.tab("Societário"), text="Última alteração contratual (dd/mm/aaaa)")
    entry_ltima_alterao_contratual_ = ctk.CTkEntry(Viewer.tab("Societário"), width=50)

    label_ltima_alterao_contratual_.grid(row=8, column=0, padx=10, pady=5, sticky="nsew")
    entry_ltima_alterao_contratual_.grid(row=8, column=1, padx=10, pady=5, sticky="nsew")


    label_Nmero_alterao_contratual = ctk.CTkLabel(Viewer.tab("Societário"), text="Número alteração contratual")
    entry_Nmero_alterao_contratual = ctk.CTkEntry(Viewer.tab("Societário"), width=50)

    label_Nmero_alterao_contratual.grid(row=9, column=0, padx=10, pady=5, sticky="nsew")
    entry_Nmero_alterao_contratual.grid(row=9, column=1, padx=10, pady=5, sticky="nsew")


    label_Observaes_gerais = ctk.CTkLabel(Viewer.tab("Societário"), text="Observações gerais")
    entry_Observaes_gerais = ctk.CTkEntry(Viewer.tab("Societário"), width=50)

    label_Observaes_gerais.grid(row=0, column=2, padx=10, pady=5, sticky="nsew")
    entry_Observaes_gerais.grid(row=0, column=3, padx=10, pady=5, sticky="nsew")

#------------------------------DP Pessoal

    label_Folha_de_pagto = ctk.CTkLabel(Viewer.tab("Departamento pessoal"), text="Folha de pagto")
    entry_Folha_de_pagto = ctk.CTkComboBox(Viewer.tab("Departamento pessoal"), width=50)

    label_Folha_de_pagto.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
    entry_Folha_de_pagto.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")


    label_Quantidade_de_funcionrios = ctk.CTkLabel(Viewer.tab("Departamento pessoal"), text="Quantidade de funcionários")
    entry_Quantidade_de_funcionrios = ctk.CTkEntry(Viewer.tab("Departamento pessoal"), width=50)

    label_Quantidade_de_funcionrios.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
    entry_Quantidade_de_funcionrios.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")


    label_Prolabore = ctk.CTkLabel(Viewer.tab("Departamento pessoal"), text="Prolabore")
    entry_Prolabore = ctk.CTkComboBox(Viewer.tab("Departamento pessoal"), width=50)

    label_Prolabore.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")
    entry_Prolabore.grid(row=2, column=1, padx=10, pady=5, sticky="nsew")


    label_Quantidade_de_scios = ctk.CTkLabel(Viewer.tab("Departamento pessoal"), text="Quantidade de sócios")
    entry_Quantidade_de_scios = ctk.CTkEntry(Viewer.tab("Departamento pessoal"), width=50)

    label_Quantidade_de_scios.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")
    entry_Quantidade_de_scios.grid(row=3, column=1, padx=10, pady=5, sticky="nsew")


    label_Esocial_usurio = ctk.CTkLabel(Viewer.tab("Departamento pessoal"), text="Esocial usuário")
    entry_Esocial_usurio = ctk.CTkEntry(Viewer.tab("Departamento pessoal"), width=50)

    label_Esocial_usurio.grid(row=4, column=0, padx=10, pady=5, sticky="nsew")
    entry_Esocial_usurio.grid(row=4, column=1, padx=10, pady=5, sticky="nsew")


    label_Esocial_senha = ctk.CTkLabel(Viewer.tab("Departamento pessoal"), text="Esocial senha")
    entry_Esocial_senha = ctk.CTkEntry(Viewer.tab("Departamento pessoal"), width=50)

    label_Esocial_senha.grid(row=5, column=0, padx=10, pady=5, sticky="nsew")
    entry_Esocial_senha.grid(row=5, column=1, padx=10, pady=5, sticky="nsew")


    label_Esocial_cdigo_de_acesso = ctk.CTkLabel(Viewer.tab("Departamento pessoal"), text="Esocial código de acesso")
    entry_Esocial_cdigo_de_acesso = ctk.CTkEntry(Viewer.tab("Departamento pessoal"), width=50)

    label_Esocial_cdigo_de_acesso.grid(row=6, column=0, padx=10, pady=5, sticky="nsew")
    entry_Esocial_cdigo_de_acesso.grid(row=6, column=1, padx=10, pady=5, sticky="nsew")


    label_FAP_usurio = ctk.CTkLabel(Viewer.tab("Departamento pessoal"), text="FAP usuário")
    entry_FAP_usurio = ctk.CTkEntry(Viewer.tab("Departamento pessoal"), width=50)

    label_FAP_usurio.grid(row=7, column=0, padx=10, pady=5, sticky="nsew")
    entry_FAP_usurio.grid(row=7, column=1, padx=10, pady=5, sticky="nsew")


    label_FAP_senha = ctk.CTkLabel(Viewer.tab("Departamento pessoal"), text="FAP senha")
    entry_FAP_senha = ctk.CTkEntry(Viewer.tab("Departamento pessoal"), width=50)

    label_FAP_senha.grid(row=8, column=0, padx=10, pady=5, sticky="nsew")
    entry_FAP_senha.grid(row=8, column=1, padx=10, pady=5, sticky="nsew")


    label_Empregador_WEB_usurio = ctk.CTkLabel(Viewer.tab("Departamento pessoal"), text="Empregador WEB usuário")
    entry_Empregador_WEB_usurio = ctk.CTkEntry(Viewer.tab("Departamento pessoal"), width=50)

    label_Empregador_WEB_usurio.grid(row=9, column=0, padx=10, pady=5, sticky="nsew")
    entry_Empregador_WEB_usurio.grid(row=9, column=1, padx=10, pady=5, sticky="nsew")


    label_Empregador_WEB_senha = ctk.CTkLabel(Viewer.tab("Departamento pessoal"), text="Empregador WEB senha")
    entry_Empregador_WEB_senha = ctk.CTkEntry(Viewer.tab("Departamento pessoal"), width=50)

    label_Empregador_WEB_senha.grid(row=0, column=2, padx=10, pady=5, sticky="nsew")
    entry_Empregador_WEB_senha.grid(row=0, column=3, padx=10, pady=5, sticky="nsew")

#------------------------------BPO

    label_Sistema = ctk.CTkLabel(Viewer.tab("BPO"), text="Sistema")
    entry_Sistema = ctk.CTkEntry(Viewer.tab("BPO"), width=200)

    label_Sistema.grid(row=0, column=0, padx=10, pady=15, sticky="nsew")
    entry_Sistema.grid(row=0, column=1, padx=10, pady=15, sticky="nsew")


    label_Site = ctk.CTkLabel(Viewer.tab("BPO"), text="Site")
    entry_Site = ctk.CTkEntry(Viewer.tab("BPO"), width=50)

    label_Site.grid(row=1, column=0, padx=10, pady=15, sticky="nsew")
    entry_Site.grid(row=1, column=1, padx=10, pady=15, sticky="nsew")


    label_Usuario = ctk.CTkLabel(Viewer.tab("BPO"), text="Usuário")
    entry_Usurio = ctk.CTkEntry(Viewer.tab("BPO"), width=50)

    label_Usuario.grid(row=2, column=0, padx=10, pady=15, sticky="nsew")
    entry_Usurio.grid(row=2, column=1, padx=10, pady=15, sticky="nsew")


    label_Senha_simples = ctk.CTkLabel(Viewer.tab("BPO"), text="Senha simples")
    entry_Senha_simples = ctk.CTkEntry(Viewer.tab("BPO"), width=50)

    label_Senha_simples.grid(row=3, column=0, padx=10, pady=15, sticky="nsew")
    entry_Senha_simples.grid(row=3, column=1, padx=10, pady=15, sticky="nsew")


    label_Banco_1 = ctk.CTkLabel(Viewer.tab("BPO"), text="Banco 1")
    entry_Banco_1 = ctk.CTkEntry(Viewer.tab("BPO"), width=50)

    label_Banco_1.grid(row=4, column=0, padx=10, pady=15, sticky="nsew")
    entry_Banco_1.grid(row=4, column=1, padx=10, pady=15, sticky="nsew")


    label_Banco_2 = ctk.CTkLabel(Viewer.tab("BPO"), text="Banco 2")
    entry_Banco_2 = ctk.CTkEntry(Viewer.tab("BPO"), width=50)

    label_Banco_2.grid(row=5, column=0, padx=10, pady=15, sticky="nsew")
    entry_Banco_2.grid(row=5, column=1, padx=10, pady=15, sticky="nsew")


    label_Tipo_de_BPO = ctk.CTkLabel(Viewer.tab("BPO"), text="Tipo de BPO")
    entry_Tipo_de_BPO = ctk.CTkEntry(Viewer.tab("BPO"), width=50)

    label_Tipo_de_BPO.grid(row=6, column=0, padx=10, pady=15, sticky="nsew")
    entry_Tipo_de_BPO.grid(row=6, column=1, padx=10, pady=15, sticky="nsew")


    label_Observaes_gerais = ctk.CTkLabel(Viewer.tab("BPO"), text="Observações gerais")
    entry_Observaes_gerais = ctk.CTkEntry(Viewer.tab("BPO"), width=50)

    label_Observaes_gerais.grid(row=7, column=0, padx=10, pady=15, sticky="nsew")
    entry_Observaes_gerais.grid(row=7, column=1, padx=10, pady=15, sticky="nsew")

