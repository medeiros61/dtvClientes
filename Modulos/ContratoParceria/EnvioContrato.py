from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import re




def enviarcontrato(Dados):
    DadosContratante,Profissional_Parceiro,Profissional_Parceiro_CNPJ,Contabilidade_Profissional_Parceiro,OutrasInformacoes,Servicos = Dados


    def clicckcontinuar():
            Contrato = wait.until(EC.presence_of_element_located((By.XPATH, f'//button[contains(text(), "Continuar")]')))
            # Rola a página até que o botão esteja visível
            driver.execute_script("arguments[0].scrollIntoView();", Contrato)
            
            # Clica no botão usando JavaScript
            driver.execute_script("arguments[0].click();", Contrato)

    def ajustar_numeros_para_telefone(input_string):
    # Encontrar todos os números na string
        numeros = re.findall(r'\d+', input_string)
        
        # Concatenar os números em uma única string
        numeros_concatenados = ''.join(numeros)
        
        # Verificar o comprimento dos números concatenados
        while len(numeros_concatenados) < 9:
            numeros_concatenados = '0' + numeros_concatenados
        
        return numeros_concatenados

    def apenas_Numeros(input_string):
    # Encontrar todos os números na string
        numeros = re.findall(r'\d+', input_string)
        
        # Concatenar os números em uma única string
        numeros_concatenados = ''.join(numeros)

        return numeros_concatenados
    

    driver = webdriver.Chrome()
    # Abre uma página web
    driver.get('https://homologa.probeleza.org.br/login')
    
    try:
        #tempo de espera para encontrar item ou pagina carregar
        wait = WebDriverWait(driver, 120)

        
        Input_cpf = wait.until(EC.presence_of_element_located((By.ID, 'cpf')))
        Input_cpf.send_keys('22549210883')

        Input_senha = wait.until(EC.presence_of_element_located((By.ID, 'password')))
        Input_senha.send_keys('Datavix@159')

        form = wait.until(EC.presence_of_element_located((By.ID, 'home-tab-pane')))
        # Envia o formulário
        form.submit()


        Agente_credenciado = wait.until(EC.presence_of_element_located((By.XPATH, '//a[.//b[contains(text(), "Agente Credenciado")]]')))
        Agente_credenciado.click()

        bt_documentos = wait.until(EC.presence_of_element_located((By.XPATH, '//a[@href="https://homologa.probeleza.org.br/documentos"]')))
        bt_documentos.click()

        bt_Novocontrato = wait.until(EC.presence_of_element_located((By.XPATH, '//a[@href="https://homologa.probeleza.org.br/documentos/create"]')))
        bt_Novocontrato.click()


        ModeloContrato = f"{OutrasInformacoes[5]}"
        
        Contrato = wait.until(EC.presence_of_element_located((By.XPATH, f'//button[contains(text(), "{ModeloContrato}")]')))
        Contrato.click()

        time.sleep(2)
        Contrato = wait.until(EC.presence_of_element_located((By.XPATH, f'//button[contains(text(), "Continuar")]')))
        # Rola a página até que o botão esteja visível
        driver.execute_script("arguments[0].scrollIntoView();", Contrato)
        
        # Clica no botão usando JavaScript
        driver.execute_script("arguments[0].click();", Contrato)
        
        


        ##Salão parceiro
        i = 0
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'cnpj_salao_parceiro')))
        input_valor.clear()
        dados = apenas_Numeros(DadosContratante[i])
        input_valor.send_keys(f'{dados}')
        input_valor.send_keys(Keys.TAB)
        time.sleep(3) 
        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'razao_social_salao_parceiro')))
        input_valor.clear()
        input_valor.send_keys(f'{DadosContratante[i]}')
        

        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'nome_fantasia_salao_parceiro')))
        input_valor.clear()
        input_valor.send_keys(f'{DadosContratante[i]}')


        i = 8
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'telefone_salao_parceiro')))
        input_valor.clear()
        telefone = ajustar_numeros_para_telefone(DadosContratante[i])
        input_valor.send_keys(f'{telefone}')
        

        i = 7
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'email_salao_parceiro')))
        input_valor.clear()
        input_valor.send_keys(f'{DadosContratante[i]}')
        

        i = 12
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'cep_salao_parceiro')))
        input_valor.clear()
        dados = apenas_Numeros(DadosContratante[i])
        input_valor.send_keys(f'{dados}')
      
        input_valor.send_keys(Keys.TAB)
        time.sleep(3) 

        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'rua_salao_parceiro')))
        input_valor.clear()
        input_valor.send_keys(f'{DadosContratante[i]}')
        
        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'numero_salao_parceiro')))
        input_valor.clear()
        input_valor.send_keys(f'{DadosContratante[i]}')

        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'complemento_salao_parceiro')))
        input_valor.clear()
        input_valor.send_keys(f'{DadosContratante[i]}')

        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'bairro_salao_parceiro')))
        input_valor.clear()
        input_valor.send_keys(f'{DadosContratante[i]}')

        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'cidade_salao_parceiro')))
        input_valor.clear()
        input_valor.send_keys(f'{DadosContratante[i]}')

        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'estado_salao_parceiro')))
        input_valor.clear()
        input_valor.send_keys(f'{DadosContratante[i]}')

        clicckcontinuar()

        ## Representante legal - Salão parceiro
        i = 3
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'cpf_representante_legal')))
        input_valor.clear()
        dados = apenas_Numeros(DadosContratante[i])
        input_valor.send_keys(f'{dados}')

        input_valor.send_keys(Keys.TAB)
        time.sleep(3)

        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'nome_representante_legal')))
        input_valor.clear()
        input_valor.send_keys(f'{DadosContratante[i]}')

        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'sobrenome_representante_legal')))
        input_valor.clear()
        input_valor.send_keys(f'{DadosContratante[i]}')

        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'data_nascimento_representante_legal')))
        input_valor.clear()
        input_valor.send_keys(f'{DadosContratante[i]}')

        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'email_representante_legal')))
        input_valor.clear()
        input_valor.send_keys(f'{DadosContratante[i]}')

        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'celular_representante_legal')))
        input_valor.clear()
        telefone = ajustar_numeros_para_telefone(DadosContratante[i])
        input_valor.send_keys(f'{telefone}')

        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'nome_mae_representante_legal')))
        input_valor.clear()
        input_valor.send_keys(f'{DadosContratante[i]}')
   
        
 
        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'estado_civil_representante_legal')))
        
        input_valor.send_keys(f'{DadosContratante[i]}')
    
 
        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'genero_representante_legal')))
    
        input_valor.send_keys(f'{DadosContratante[i]}')
        
 
        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'cep_representante_legal')))
        input_valor.clear()
        dados = apenas_Numeros(DadosContratante[i])
        input_valor.send_keys(f'{dados}')
  
        input_valor.send_keys(Keys.TAB)
        time.sleep(3) 

        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'rua_representante_legal')))
        input_valor.clear()
        input_valor.send_keys(f'{DadosContratante[i]}')

        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'numero_representante_legal')))
        input_valor.clear()
        input_valor.send_keys(f'{DadosContratante[i]}')
        
        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'complemento_representante_legal')))
        input_valor.clear()
        input_valor.send_keys(f'{DadosContratante[i]}')

        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'bairro_representante_legal')))
        input_valor.clear()
        input_valor.send_keys(f'{DadosContratante[i]}')

        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'cidade_representante_legal')))
        input_valor.clear()
        input_valor.send_keys(f'{DadosContratante[i]}')

        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'estado_representante_legal')))
        input_valor.clear()
        
        input_valor.send_keys(f'{DadosContratante[i]}')

        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'rg_representante_legal')))
        input_valor.clear()
        dados = apenas_Numeros(DadosContratante[i])
        input_valor.send_keys(f'{dados}')
  
        
        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'orgao_expedidor_representante_legal')))
        input_valor.clear()
        input_valor.send_keys(f'{DadosContratante[i]}')
        
        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'data_expedicao_representante_legal')))
        input_valor.clear()
        input_valor.send_keys(f'{DadosContratante[i]}')

        clicckcontinuar()


        ##profissional parceiro

        i = 00
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'cpf_profissional_parceiro')))
        input_valor.clear()
        dados = apenas_Numeros(Profissional_Parceiro[i])
        input_valor.send_keys(f'{dados}')
 
        input_valor.send_keys(Keys.TAB)
        time.sleep(3)

        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'nome_profissional_parceiro')))
        input_valor.clear()
        input_valor.send_keys(f'{Profissional_Parceiro[i]}')

        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'sobrenome_profissional_parceiro')))
        input_valor.clear()
        input_valor.send_keys(f'{Profissional_Parceiro[i]}')

        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'data_nascimento_profissional_parceiro')))
        input_valor.clear()
        input_valor.send_keys(f'{Profissional_Parceiro[i]}')

        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'email_profissional_parceiro')))
        input_valor.clear()
        input_valor.send_keys(f'{Profissional_Parceiro[i]}')

        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'celular_profissional_parceiro')))
        input_valor.clear()
        telefone = ajustar_numeros_para_telefone(Profissional_Parceiro[i])
        input_valor.send_keys(f'{telefone}')


        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'nome_mae_profissional_parceiro')))
        input_valor.clear()
        input_valor.send_keys(f'{Profissional_Parceiro[i]}')

        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'estado_civil_profissional_parceiro')))
        input_valor.send_keys(f'{Profissional_Parceiro[i]}')

        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'genero_profissional_parceiro')))
        input_valor.send_keys(f'{Profissional_Parceiro[i]}')

        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'cep_profissional_parceiro')))
        input_valor.clear()
        dados = apenas_Numeros(Profissional_Parceiro[i])
        input_valor.send_keys(f'{dados}')
     
        input_valor.send_keys(Keys.TAB)
        time.sleep(3)

        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'rua_profissional_parceiro')))
        input_valor.clear()
        input_valor.send_keys(f'{Profissional_Parceiro[i]}')

        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'numero_profissional_parceiro')))
        input_valor.clear()
        input_valor.send_keys(f'{Profissional_Parceiro[i]}')

        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'complemento_profissional_parceiro')))
        input_valor.clear()
        input_valor.send_keys(f'{Profissional_Parceiro[i]}')

        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'bairro_profissional_parceiro')))
        input_valor.clear()
        input_valor.send_keys(f'{Profissional_Parceiro[i]}')

        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'cidade_profissional_parceiro')))
        input_valor.clear()
        input_valor.send_keys(f'{Profissional_Parceiro[i]}')

        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'estado_profissional_parceiro')))
        input_valor.clear()
        input_valor.send_keys(f'{Profissional_Parceiro[i]}')

        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'rg_profissional_parceiro')))
        input_valor.clear()
        
        dados = apenas_Numeros(Profissional_Parceiro[i])
        input_valor.send_keys(f'{dados}')
        

        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'orgao_expedidor_profissional_parceiro')))
        input_valor.clear()
        input_valor.send_keys(f'{Profissional_Parceiro[i]}')

        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'data_expedicao_profissional_parceiro')))
        input_valor.clear()
        input_valor.send_keys(f'{Profissional_Parceiro[i]}')

        clicckcontinuar()

        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'utilizar_cpf')))

        driver.execute_script("arguments[0].click();", input_valor)
        time.sleep(3)

        i = 0
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'cnpj_profissional_parceiro')))
        input_valor.clear()
        dados = apenas_Numeros(Profissional_Parceiro_CNPJ[i])
        input_valor.send_keys(f'{dados}')
        input_valor.send_keys(Keys.TAB)
        time.sleep(3)

        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'razao_social_profissional_parceiro')))
        input_valor.clear()
        input_valor.send_keys(f'{Profissional_Parceiro_CNPJ[i]}')
        input_valor.send_keys(Keys.TAB)


        i += 1
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'cnaes-selectized')))

        number_str = str(Profissional_Parceiro_CNPJ[i])
        # Formate o número
        formatted_number = f"{number_str[:4]}-{number_str[4]}/{number_str[5:]}"

        input_valor.send_keys(f'{formatted_number}')
        input_valor.send_keys(Keys.TAB)
        clicckcontinuar()

        for item in Servicos:
            if str(item[0]) == 'Percentual':
                input_valor = wait.until(EC.presence_of_element_located((By.ID, 'tipo_repasse_P')))

                driver.execute_script("arguments[0].click();", input_valor)
            if str(item[0]) == 'Valor':
                input_valor = wait.until(EC.presence_of_element_located((By.ID, 'tipo_repasse_v')))

                driver.execute_script("arguments[0].click();", input_valor)  


                
                                                    
                                                  
        Numero_servicos = 0
        for item in Servicos:
            Numero_servicos += 1
            Botão_ADD = wait.until(EC.presence_of_element_located((By.XPATH, f'//button[contains(text(), "Adicionar Serviço")]')))
            
            driver.execute_script("arguments[0].click();", Botão_ADD) 

            input_valor = wait.until(EC.presence_of_element_located((By.NAME, f'servico[{Numero_servicos}]')))
            input_valor.clear()
            input_valor.send_keys(f'{item[1]}')

            input_valor = wait.until(EC.presence_of_element_located((By.NAME, f'valor_salao[{Numero_servicos}]')))
            input_valor.clear()
            input_valor.send_keys(f'{item[2]}')

            input_valor = wait.until(EC.presence_of_element_located((By.NAME, f'comissao_profissional[{Numero_servicos}]')))
            input_valor.clear()
            input_valor.send_keys(f'{item[3]}')    

            Botao_add_item = wait.until(EC.presence_of_element_located((By.XPATH, f'//a[@onclick="confirmaServicoTabelaRepasse({Numero_servicos})"]')))
            driver.execute_script("arguments[0].click();", Botao_add_item)
        clicckcontinuar()
        
        if Contabilidade_Profissional_Parceiro[0]=='Sim':
            bt = wait.until(EC.presence_of_element_located((By.ID, 'possui_contabilidade_1')))
            driver.execute_script("arguments[0].click();", bt) 

            valor = Contabilidade_Profissional_Parceiro[1].split('(')
            Contabiliddade = valor[0]
            valor2 =valor[1].split(')')
            Contabilidade_CNPJ = re.findall(r'\d+', valor2[0])
            Contabilidade_CNPJ = ''.join(Contabilidade_CNPJ)
            valor3 = valor2[1].split(':')
            Numero = re.findall(r'\d+', valor3[1])
            Numero = ''.join(Numero)

            input_valor = wait.until(EC.presence_of_element_located((By.ID, 'cpf_cnpj_contabilidade')))
            input_valor.clear()
            input_valor.send_keys(f'{Contabilidade_CNPJ}')
            input_valor.send_keys(Keys.TAB)
            time.sleep(3)

            input_valor = wait.until(EC.presence_of_element_located((By.ID, 'razao_social_contabilidade')))
            input_valor.clear()
            input_valor.send_keys(f'{Contabiliddade}')

            input_valor = wait.until(EC.presence_of_element_located((By.ID, 'telefone_contabilidade')))
            input_valor.clear()
            input_valor.send_keys(f'{Numero}')
          


        else:
            bt = wait.until(EC.presence_of_element_located((By.ID, 'possui_contabilidade_0')))
            driver.execute_script("arguments[0].click();", bt) 
  
 
        clicckcontinuar()

        i = 0
        input_valor = wait.until(EC.presence_of_element_located((By.ID, 'data_inicio_parceria')))
        input_valor.clear()
        input_valor.send_keys(f'{OutrasInformacoes[i]}')

        i += 1
        div_opcoes = driver.find_element(By.XPATH, "//div[label[contains(text(), 'Responsável pelo recolhimento/retenção')]]")
        label = div_opcoes.find_element(By.XPATH, f"//label[text()='{OutrasInformacoes[i]}']")

        # Encontra o elemento de entrada associado ao label e clica nele
        input_valor = label.find_element(By.XPATH, ".//preceding-sibling::input")
        driver.execute_script("arguments[0].click();", input_valor) 


        i += 1
        div_opcoes = driver.find_element(By.XPATH, "//div[label[contains(text(), 'Periodicidade do repasse')]]")
        label = div_opcoes.find_element(By.XPATH, f"//label[text()='{OutrasInformacoes[i]}']")

        # Encontra o elemento de entrada associado ao label e clica nele
        input_valor = label.find_element(By.XPATH, ".//preceding-sibling::input")
        driver.execute_script("arguments[0].click();", input_valor)


       
        i += 1
        div_opcoes = driver.find_element(By.XPATH, "//div[label[contains(text(), 'Os valores recebidos pelo cliente final')]]")
        label = div_opcoes.find_element(By.XPATH, f"//label[text()='{OutrasInformacoes[i]}']")

        # Encontra o elemento de entrada associado ao label e clica nele
        input_valor = label.find_element(By.XPATH, ".//preceding-sibling::input")
        driver.execute_script("arguments[0].click();", input_valor)

        botao_adicionar = driver.find_element(By.XPATH, "//button[contains(text(), 'Adicionar Bem Material')]")

        i += 1
        # Verifica se o botão está desabilitado
        if botao_adicionar.is_enabled():
            if OutrasInformacoes[i] == '0':
                bt = wait.until(EC.presence_of_element_located((By.ID, 'utilizar_kit_padrao')))
                driver.execute_script("arguments[0].click();", bt)
        else:
            if OutrasInformacoes[i] == '1':
                bt = wait.until(EC.presence_of_element_located((By.ID, 'utilizar_kit_padrao')))
                driver.execute_script("arguments[0].click();", bt)

        DiasAbertos = DadosContratante[22].split(',')
        for index,dia in enumerate(DiasAbertos):
            if dia =='DOM':
                bt = wait.until(EC.presence_of_element_located((By.ID, 'dia_0')))
                driver.execute_script("arguments[0].click();", bt)

                horas = DadosContratante[29].split('-')

                input_valor = wait.until(EC.presence_of_element_located((By.ID, 'entrada_0')))
                input_valor.clear()
                input_valor.send_keys(f'{horas[0]}{horas[1]}')

                input_valor = wait.until(EC.presence_of_element_located((By.ID, 'saida_0')))
                input_valor.clear()
                input_valor.send_keys(f'{horas[2]}{horas[3]}')

            elif dia =='SEG':
                bt = wait.until(EC.presence_of_element_located((By.ID, 'dia_1')))
                driver.execute_script("arguments[0].click();", bt)

                horas = DadosContratante[23].split('-')

                input_valor = wait.until(EC.presence_of_element_located((By.ID, 'entrada_1')))
                input_valor.clear()
                input_valor.send_keys(f'{horas[0]}{horas[1]}')

                input_valor = wait.until(EC.presence_of_element_located((By.ID, 'saida_1')))
                input_valor.clear()
                input_valor.send_keys(f'{horas[2]}{horas[3]}')

            elif dia =='TER':
                bt = wait.until(EC.presence_of_element_located((By.ID, 'dia_2')))
                driver.execute_script("arguments[0].click();", bt)

                horas = DadosContratante[24].split('-')

                input_valor = wait.until(EC.presence_of_element_located((By.ID, 'entrada_2')))
                input_valor.clear()
                input_valor.send_keys(f'{horas[0]}{horas[1]}')

                input_valor = wait.until(EC.presence_of_element_located((By.ID, 'saida_2')))
                input_valor.clear()
                input_valor.send_keys(f'{horas[2]}{horas[3]}')

            elif dia =='QUA':
                bt = wait.until(EC.presence_of_element_located((By.ID, 'dia_3')))
                driver.execute_script("arguments[0].click();", bt)

                horas = DadosContratante[25].split('-')

                input_valor = wait.until(EC.presence_of_element_located((By.ID, 'entrada_3')))
                input_valor.clear()
                input_valor.send_keys(f'{horas[0]}{horas[1]}')

                input_valor = wait.until(EC.presence_of_element_located((By.ID, 'saida_3')))
                input_valor.clear()
                input_valor.send_keys(f'{horas[2]}{horas[3]}')
            elif dia =='QUI':
                bt = wait.until(EC.presence_of_element_located((By.ID, 'dia_4')))
                driver.execute_script("arguments[0].click();", bt)

                horas = DadosContratante[26].split('-')

                input_valor = wait.until(EC.presence_of_element_located((By.ID, 'entrada_4')))
                input_valor.clear()
                input_valor.send_keys(f'{horas[0]}{horas[1]}')

                input_valor = wait.until(EC.presence_of_element_located((By.ID, 'saida_4')))
                input_valor.clear()
                input_valor.send_keys(f'{horas[2]}{horas[3]}')
            elif dia =='SEX':
                bt = wait.until(EC.presence_of_element_located((By.ID, 'dia_5')))
                driver.execute_script("arguments[0].click();", bt)

                horas = DadosContratante[27].split('-')

                input_valor = wait.until(EC.presence_of_element_located((By.ID, 'entrada_5')))
                input_valor.clear()
                input_valor.send_keys(f'{horas[0]}{horas[1]}')

                input_valor = wait.until(EC.presence_of_element_located((By.ID, 'saida_5')))
                input_valor.clear()
                input_valor.send_keys(f'{horas[2]}{horas[3]}')
            elif dia =='SAB':
                bt = wait.until(EC.presence_of_element_located((By.ID, 'dia_6')))
                driver.execute_script("arguments[0].click();", bt)

                horas = DadosContratante[28].split('-')

                input_valor = wait.until(EC.presence_of_element_located((By.ID, 'entrada_6')))
                input_valor.clear()
                input_valor.send_keys(f'{horas[0]}{horas[1]}')

                input_valor = wait.until(EC.presence_of_element_located((By.ID, 'saida_6')))
                input_valor.clear()
                input_valor.send_keys(f'{horas[2]}{horas[3]}')


          

        clicckcontinuar()
        
        
    finally:
        # Fecha o navegador
        driver.quit()



##Salão parceiro
id="cnpj_salao_parceiro"
id="razao_social_salao_parceiro" 
id="nome_fantasia_salao_parceiro"
id="telefone_salao_parceiro"
id="email_salao_parceiro"
id="cep_salao_parceiro"
id="rua_salao_parceiro"
id="numero_salao_parceiro" 
id="complemento_salao_parceiro"
id="bairro_salao_parceiro"
id="cidade_salao_parceiro" 
id="estado_salao_parceiro"

## Representante legal - Salão parceiro
id="cpf_representante_legal"
id="nome_representante_legal"
id="sobrenome_representante_legal"
id="data_nascimento_representante_legal"
id="email_representante_legal"
id="celular_representante_legal"
id="nome_mae_representante_legal"
id="estado_civil_representante_legal"
#class="form-control"><option value="">Selecione o estado civil</option>
id="genero_representante_legal"
id="cep_representante_legal"
id="rua_representante_legal"
id="numero_representante_legal"
id="complemento_representante_legal"
id="bairro_representante_legal"
id="cidade_representante_legal"
id="estado_representante_legal"
id="rg_representante_legal"
id="orgao_expedidor_representante_legal"
id="data_expedicao_representante_legal"

##profissional parceiro
id="cpf_profissional_parceiro" 
id="nome_profissional_parceiro"
id="sobrenome_profissional_parceiro"
id="data_nascimento_profissional_parceiro"
id="email_profissional_parceiro"
id="celular_profissional_parceiro"
id="nome_mae_profissional_parceiro"
id="estado_civil_profissional_parceiro" 
#class="form-control"><option value="">Selecione o estado civil</option>
id="genero_profissional_parceiro" 
#class="form-control" required=""><option value="">Selecione o gênero</option>
id="cep_profissional_parceiro"
id="rua_profissional_parceiro"
id="numero_profissional_parceiro"
id="complemento_profissional_parceiro"
id="bairro_profissional_parceiro"
id="cidade_profissional_parceiro"
id="estado_profissional_parceiro"
id="rg_profissional_parceiro"
id="orgao_expedidor_profissional_parceiro"
id="data_expedicao_profissional_parceiro"

#CNPJ - PROFISSIONAL PARCEIRO
## Comnando para clic no ##utilizar_cpf
id="cnpj_profissional_parceiro"
id="razao_social_profissional_parceiro"
id="cnaes-selectized"

#TPC - TABELA DE PREÇO CONVENCIONADA
#Tipo Repasse ID tipo_repasse_v ou ID tipo_repasse_P
##Clicar no botão com texto "Adicionar Serviço"
name="servico[1]"
name= "valor_salao[1]"
name="comissao_profissional[1]"
#Se for add mais servicos os campos vao aumentando [1] > [2] > [3]
#Depois clica aqui <a href="#" class="btn btn-outline-success btn-sm confirm1 me-1" onclick="confirmaServicoTabelaRepasse(1)"><i class="fa-solid fa-check fa-fw"></i></a>

#CONTABILIDADE - PROFISSIONAL PARCEIRO
id="possui_contabilidade_1" # Sim
#Ou
id="possui_contabilidade_0" #Não
##Se Sim
id="cpf_cnpj_contabilidade"
id="razao_social_contabilidade"
id="telefone_contabilidade"

#GESTÃO DE OUTRAS INFORMAÇÕES
id="data_inicio_parceria"
#Responsável pelo recolhimento/retenção e pagamento das obrigações do PROFISSIONAL PARCEIRO:

#Clicar na div que tem o nome informado <div class="form-check form-check-inline"><input class="form-check-input" type="radio" name="responsavel_taxa_mensal" id="responsavel_taxa_mensal_sp" value="SP" required=""><label class="form-check-label" for="responsavel_taxa_mensal_sp">Salão Parceiro</label></div>


#segunda
id = "dia_1"
id = "entrada_1"
id="saida_1"

#terca
id = "dia_2"
id = "entrada_2"
id="saida_2"

#Quarta
id = "dia_3"
id = "entrada_3"
id="saida_3"

#quinta
id = "dia_4"
id = "entrada_4"
id="saida_4"

#sexta
id = "dia_5"
id = "entrada_5"
id="saida_5"

#sabado
id = "dia_6"
id = "entrada_6"
id="saida_6"

#domingo
id = "dia_0"
id = "entrada_0"
id="saida_0"

#Periodicidade do repasse:
##Selecioanr com percentual <div class="form-check form-check-inline"><input class="form-check-input" type="radio" name="periodicidade_repasse" id="periodicidade_repasse_17" value="15"><label class="form-check-label" for="periodicidade_repasse_17">Quinzenal</label></div>

#Os valores recebidos pelo cliente final serão geridos e administrados por:
#<div class="form-check form-check-inline"><input class="form-check-input" type="radio" name="gestao_caixa" id="gestao_caixa_sp" value="SP" onchange="changeGestaoCaixaNovoContrato(this.value)"><label class="form-check-label" for="gestao_caixa_sp">Salão Parceiro</label></div>

id="utilizar_kit_padrao"

#clicar neste botão dps 
#<a href="https://homologa.probeleza.org.br/storage/35213857000174.24052024143244/contrato-de-parceria-profissional.f2580ebc.pdf" target="_blank" class="btn btn-purple btn-sm">                        <i class="fa-solid fa-file-contract"></i>Visualizar Contrato</a>