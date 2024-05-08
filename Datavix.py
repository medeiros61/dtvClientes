import Modulos.Database.Parametros as bdp
import os
import requests




diretorio_atual = os.getcwd()


caminho_completo = os.path.join(diretorio_atual, "logodatavix.ico")

# Garantir que a pasta de saída exista
if not os.path.exists(diretorio_atual):
        os.makedirs(diretorio_atual)

url = 'https://github.com/Datavixdev/Datavix_Clientes_APP/releases/download/UpdateModulo/logodatavix.ico'
resposta = requests.get(url)


with open(caminho_completo, 'wb') as arquivo_zip:
        arquivo_zip.write(resposta.content)


diretorio_atual = os.getcwd()


caminho_completo = os.path.join(diretorio_atual, "DatavixAPP_Update.exe")

# Garantir que a pasta de saída exista
if not os.path.exists(diretorio_atual):
        os.makedirs(diretorio_atual)

url = 'https://github.com/Datavixdev/Datavix_Clientes_APP/releases/download/UpdateModulo/DatavixAPP_Update.exe'
resposta = requests.get(url)


with open(caminho_completo, 'wb') as arquivo_zip:
        arquivo_zip.write(resposta.content)





Vatual = bdp.pegar_parametro('versao_atual')

caminho_do_exe = r'DatavixAPP_Update.exe'

os.execl(caminho_do_exe,'DatavixAPP.exe',Vatual)    






