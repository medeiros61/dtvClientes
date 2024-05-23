import Modulos.Database.Parametros as bdp
import os
import requests
import subprocess
import tkinter as tk


def instalarapp():
        def pegarcaminhodaappdata():
                # Obter o diretório de dados do usuário (AppData/Roaming)
                global appdata_roaming
                appdata_roaming = os.getenv('APPDATA')
                # Caminho completo para a pasta Datavix
                datavix_path = os.path.join('C:\\', 'Datavix')
                datavix_path = os.path.join(appdata_roaming, 'Datavix')
                # Caminho para a pasta de imagens dentro de Datavix
                imagens_path = os.path.join(datavix_path, 'App')
                if not os.path.exists(imagens_path):
                        os.makedirs(imagens_path)
                return imagens_path


        def adicionar_excecao_windows_defender(caminho_da_pasta):
                # Comando PowerShell para adicionar uma pasta à lista de exclusões do Windows Defender
                comando_powershell = f"Add-MpPreference -ExclusionPath '{caminho_da_pasta}'"

                # Executar o comando PowerShell
                subprocess.run(["powershell", "-Command", comando_powershell], check=True, shell=True)



        imagens_path = pegarcaminhodaappdata()
        adicionar_excecao_windows_defender(imagens_path)



        caminho_completo_imagem = os.path.join(imagens_path, "logodatavix.ico")


        url = 'https://github.com/Datavixdev/Datavix_Clientes_APP/releases/download/UpdateModulo/logodatavix.ico'
        resposta = requests.get(url)


        with open(caminho_completo_imagem, 'wb') as arquivo_zip:
                arquivo_zip.write(resposta.content)
        

        caminho_completo_Update = os.path.join(imagens_path, "DatavixAPP_Update.exe")


        url = 'https://github.com/Datavixdev/Datavix_Clientes_APP/releases/download/UpdateModulo/DatavixAPP_Update.exe'
        resposta = requests.get(url)


        with open(caminho_completo_Update, 'wb') as arquivo_zip:
                arquivo_zip.write(resposta.content)




        Vatual = bdp.pegar_parametro('versao_atual')

        caminho_do_exe = rf'{caminho_completo_Update}'

        # Mudar o diretório de execução
        os.chdir(imagens_path)
        ##Para executar como adm precisa repetir o primeiro parametro 2 vezes 
        
        os.execl(caminho_do_exe,'DatavixAPP.exe','DatavixAPP.exe',Vatual)   
        
               

        



global janela

# Criar a janela principal
janela = tk.Tk()
janela.title("Baixar Aplicativo")

# Criar o botão
botao_baixar = tk.Button(janela, text="Baixar Aplicativo", command=instalarapp)
botao_baixar.pack(expand=True,fill='both')

# Iniciar o loop principal da interface gráfica
janela.mainloop()
