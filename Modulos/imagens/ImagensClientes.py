import requests ,os

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params={'id': id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)

    save_response_content(response, destination)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:
                f.write(chunk)


def pegarcaminhodaappdata():
    # Obter o diretório de dados do usuário (AppData/Roaming)
    appdata_roaming = os.getenv('APPDATA')
    # Caminho completo para a pasta Datavix
    datavix_path = os.path.join(appdata_roaming, 'Datavix')
    # Caminho para a pasta de imagens dentro de Datavix
    imagens_path = os.path.join(datavix_path, 'imagens')
    return imagens_path

def baixarimagemPgclientes():

    imagens_path = pegarcaminhodaappdata()

    imagens_path = os.path.join(imagens_path, 'Clientes')
    # Verificar se a pasta de imagens dentro de Datavix existe, e criar se não existir
    if not os.path.exists(imagens_path):
        os.makedirs(imagens_path)

    Caminho_Logo_Add = os.path.join(imagens_path,"Adicionar.png")
    Caminho_Logo_Edit = os.path.join(imagens_path,"Editar.png")
    Caminho_Logo_Rem = os.path.join(imagens_path,"Excluir.png")
    Caminho_Logo_Comt = os.path.join(imagens_path,"Comentario.png")
    Caminho_Logo_Excel = os.path.join(imagens_path,"Excel.png")

    ##Funções 
    #Baixar as imagens dos botões caso não exista
  
        #Imagem Adicionar
    if not os.path.exists(Caminho_Logo_Add):
            file_id = "1TAD6pW2-csTySNf6Tzrl7vSkVl-e1HC4"
            destination_path = Caminho_Logo_Add  
            download_file_from_google_drive(file_id, destination_path)
        #Imagem Excluir
    if not os.path.exists(Caminho_Logo_Rem):
            file_id = "1i86KfUpYoNAioimIqcPUm83ypQpWQLWY"
            destination_path = Caminho_Logo_Rem  
            download_file_from_google_drive(file_id, destination_path)
        #Imagem Editar
    if not os.path.exists(Caminho_Logo_Edit):
            file_id = "1Fsi8WYXOhrkiCjlq0bnTpdJlDIc9kruL"
            destination_path = Caminho_Logo_Edit  
            download_file_from_google_drive(file_id, destination_path)
        #Imagem Comentar
    if not os.path.exists(Caminho_Logo_Comt):
            file_id = "1vGo74BbITBjiljU5Mxy6KpjCQYKUMR9V"
            destination_path = Caminho_Logo_Comt  
            download_file_from_google_drive(file_id, destination_path)
        #Imagem Excel
    if not os.path.exists(Caminho_Logo_Excel):
            
            file_id = "17pFP8y2H_F9dN5N-LpqeFuHUNHDR0O6q"
            destination_path = Caminho_Logo_Excel  
            download_file_from_google_drive(file_id, destination_path)

    return Caminho_Logo_Add,Caminho_Logo_Edit,Caminho_Logo_Rem ,Caminho_Logo_Comt,Caminho_Logo_Excel  

def baixarimagemLogoDTV():

    imagens_path = pegarcaminhodaappdata()
    if not os.path.exists(imagens_path):
        os.makedirs(imagens_path)

    Logo_DTV = os.path.join(imagens_path,"logodatavix.png")

    ##Funções 
    #Baixar as imagens dos botões caso não exista
    if not os.path.exists(Logo_DTV):
            file_id = "1q_sYTdMgVqPKMcj_PGk-Cy6RWuwDUkDp"
            destination_path = Logo_DTV  
            download_file_from_google_drive(file_id, destination_path)
   
    return Logo_DTV                                

def baixarimagemLogoDTVIcon():

    imagens_path = pegarcaminhodaappdata()
    if not os.path.exists(imagens_path):
        os.makedirs(imagens_path)

    Logo_DTV = os.path.join(imagens_path,"logodatavix.ico")

    ##Funções 
    #Baixar as imagens dos botões caso não exista
    if not os.path.exists(Logo_DTV):
            file_id = "1RRPgMFYm2ssaY5sbtkO46ERYMyuNWpuF"
            destination_path = Logo_DTV  
            download_file_from_google_drive(file_id, destination_path)
   
                                


def baixarimagemLogin():


    imagens_path = pegarcaminhodaappdata()
    if not os.path.exists(imagens_path):
        os.makedirs(imagens_path)

    i_login = os.path.join(imagens_path,"login.png")

    ##Funções 
    #Baixar as imagens dos botões caso não exista
    if not os.path.exists(i_login):
            file_id = "1vudOlN3YTCfPPIXJMVmuCM4ZHnMvwRaT"
            destination_path = i_login  
            download_file_from_google_drive(file_id, destination_path)
   
    return i_login                                   