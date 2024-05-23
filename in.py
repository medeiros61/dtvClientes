import subprocess
import tkinter as tk

def baixar_aplicativo_via_powershell(url):
    # Comando PowerShell para baixar um arquivo via URL
    comando_powershell = f"Invoke-WebRequest -Uri '{url}' -OutFile 'C:\\Caminho\\Para\\Download\\Aplicativo.exe'"

    # Executar o comando PowerShell para baixar o aplicativo
    subprocess.run(["powershell", "-Command", comando_powershell], shell=True, check=True)

def baixar_aplicativo():
    # URL do aplicativo a ser baixado
    url_aplicativo = 'https://github.com/Datavixdev/Datavix_Clientes_APP/releases/download/UpdateModulo/DatavixAPP_Update.exe'
    # Chamar a função para baixar o aplicativo via PowerShell
    baixar_aplicativo_via_powershell(url_aplicativo)

# Criar a janela principal
janela = tk.Tk()
janela.title("Baixar Aplicativo")

# Criar o botão
botao_baixar = tk.Button(janela, text="Baixar Aplicativo", command=baixar_aplicativo)
botao_baixar.pack(padx=20, pady=10)

# Iniciar o loop principal da interface gráfica
janela.mainloop()
