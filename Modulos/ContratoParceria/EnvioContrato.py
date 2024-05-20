from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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


    ModeloContrato = "Contrato Padrão - Versão Datavix Contábil Digital Eireli"
    Contrato = wait.until(EC.presence_of_element_located((By.XPATH, f'//button[contains(text(), "{ModeloContrato}")]')))
    Contrato.click()

    time.sleep(2)
    #Contrato = wait.until(EC.presence_of_element_located((By.XPATH, f'//button[contains(text(), "Continuar")]')))
    #Contrato.click()
    
    Input_cnpj_salao_parceiro = wait.until(EC.presence_of_element_located((By.ID, 'cnpj_salao_parceiro')))
    Input_cnpj_salao_parceiro.send_keys('1')
    

    time.sleep(90000)
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