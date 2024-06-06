import urllib.request
import requests
import json
import os
from tkinter import messagebox
import threading
import ctypes
import sys
import customtkinter as ctk
from tkinter import ttk

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    try:
        if os.name == 'nt' and sys.platform == "win32":
            # Executar o programa com privilégios de administrador no Windows
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            sys.exit()
        else:
            # Caso contrário, não é possível abrir como administrador em outros sistemas
            print("Não é possível abrir como administrador em sistemas não-Windows.")
    except Exception as e:
        print(f"Erro ao abrir como administrador: {e}")

if not is_admin():
    print("O programa não está sendo executado como administrador. Tentando abrir novamente como administrador...")
    ##Destativar para o DEBUG 

    run_as_admin()
    
    ##Destativar para o DEBUG 

else:
    print("O programa está sendo executado como administrador.")



# Função para atualizar o valor da barra de progresso e os rótulos
def update_progress_bar(num_blocks, block_size, total_size):
    downloaded_size = num_blocks * block_size
    percent = min(100, int(downloaded_size / total_size * 100))
    progress_bar['value'] = percent
    downloaded_label.configure(text=f"Baixado: {downloaded_size / (1024*1024):.2f} MB")
    total_label.configure(text=f"Total: {total_size / (1024*1024):.2f} MB")
    window.update_idletasks()

# Função para realizar o download em uma thread separada
def download_exe():
    try:
        exe_url = f"https://github.com/Datavixdev/Datavix_Clientes_APP/releases/download/DatavixAPP_V{versão}/{Executavel}"
        
        if os.path.exists(Executavel):
            os.remove(Executavel)
        
        urllib.request.urlretrieve(exe_url, Executavel, reporthook=update_progress_bar)
        
        
        messagebox.showinfo("Download Concluído", "O download foi concluído com sucesso!")
        
        window.withdraw()
        
        diretorio = "./"  # Substitua pelo caminho real do diretório
        ProgramaDir = os.path.join(diretorio, Executavel)

        
        diretorio_atual = os.getcwd()


        caminho_completo = os.path.join(diretorio_atual, "datavix.exe")

        # Garantir que a pasta de saída exista
        if os.path.exists(caminho_completo):
            os.remove(caminho_completo)   

        os.execl(ProgramaDir, Executavel)
 
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")


#Recebe os Argumentos
if len(sys.argv) >= 2:

    Executavel = sys.argv[1]
    messagebox.showinfo("Informações", f"O programa {Executavel} será atualizado para a ultima versão ")
    versão = sys.argv[2]


    # Cria a janela da interface gráfica
    window = ctk.CTk()
    window.title("Atualização")
    window.geometry("400x150")
    #window.iconbitmap(default='logodatavix.ico')
    # Cria a barra de progresso
    progress_bar = ttk.Progressbar(window, mode="determinate", length=350)
    progress_bar.pack(pady=20)

    # Cria rótulos para exibir o tamanho baixado e o tamanho total
    downloaded_label = ctk.CTkLabel(window, text="Baixado: 0.00 MB")
    downloaded_label.pack()
    total_label = ctk.CTkLabel(window, text="Total: 0.00 MB")
    total_label.pack()

    # Cria uma thread para realizar o download
    download_thread = threading.Thread(target=download_exe)
    download_thread.start()
    
    # Inicie a interface gráfica
    window.mainloop()

else:
    print("Erro: Não conseguiu receber os argumentos.")