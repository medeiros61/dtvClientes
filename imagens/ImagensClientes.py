import requests ,os

def baixarimagemPgclientes():

    # Obter o diretório de dados do usuário (AppData/Roaming)
    appdata_roaming = os.getenv('APPDATA')
    # Caminho completo para a pasta Datavix
    datavix_path = os.path.join(appdata_roaming, 'Datavix')
    # Caminho para a pasta de imagens dentro de Datavix
    imagens_path = os.path.join(datavix_path, 'Imagens')

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
            with open(Caminho_Logo_Add, 'wb') as imagem:
                resposta = requests.get("https://cdn-icons-png.flaticon.com/512/189/189689.png", stream=True)
                if not resposta.ok:
                    print("Ocorreu um erro, status:" , resposta.status_code)
                else:
                    for dado in resposta.iter_content(1024):
                        if not dado:
                            break
                        imagem.write(dado)
        #Imagem Excluir
    if not os.path.exists(Caminho_Logo_Rem):
            with open(Caminho_Logo_Rem, 'wb') as imagem:
                resposta = requests.get("https://cdn-icons-png.flaticon.com/512/6861/6861362.png", stream=True)
                if not resposta.ok:
                    print("Ocorreu um erro, status:" , resposta.status_code)
                else:
                    for dado in resposta.iter_content(1024):
                        if not dado:
                            break
                        imagem.write(dado)
        #Imagem Editar
    if not os.path.exists(Caminho_Logo_Edit):
            with open(Caminho_Logo_Edit, 'wb') as imagem:
                resposta = requests.get("https://cdn-icons-png.flaticon.com/512/45/45406.png", stream=True)
                if not resposta.ok:
                    print("Ocorreu um erro, status:" , resposta.status_code)
                else:
                    for dado in resposta.iter_content(1024):
                        if not dado:
                            break
                        imagem.write(dado)
        #Imagem Comentar
    if not os.path.exists(Caminho_Logo_Comt):
            with open(Caminho_Logo_Comt, 'wb') as imagem:
                resposta = requests.get("https://cdn-icons-png.flaticon.com/512/711/711739.png", stream=True)
                if not resposta.ok:
                    print("Ocorreu um erro, status:" , resposta.status_code)
                else:
                    for dado in resposta.iter_content(1024):
                        if not dado:
                            break
                        imagem.write(dado)
        #Imagem Adicionar
    if not os.path.exists(Caminho_Logo_Excel):
            with open(Caminho_Logo_Excel, 'wb') as imagem:
                resposta = requests.get("https://logodownload.org/wp-content/uploads/2020/04/excel-logo-3.png", stream=True)
                if not resposta.ok:
                    print("Ocorreu um erro, status:" , resposta.status_code)
                else:
                    for dado in resposta.iter_content(1024):
                        if not dado:
                            break
                        imagem.write(dado)            
    return Caminho_Logo_Add,Caminho_Logo_Edit,Caminho_Logo_Rem ,Caminho_Logo_Comt,Caminho_Logo_Excel  

def baixarimagemLogoDTV():

    # Obter o diretório de dados do usuário (AppData/Roaming)
    appdata_roaming = os.getenv('APPDATA')
    # Caminho completo para a pasta Datavix
    datavix_path = os.path.join(appdata_roaming, 'Datavix')
    # Caminho para a pasta de imagens dentro de Datavix
    imagens_path = os.path.join(datavix_path, 'imagens')
    # Verificar se a pasta de imagens dentro de Datavix existe, e criar se não existir
    if not os.path.exists(imagens_path):
        os.makedirs(imagens_path)

    Logo_DTV = os.path.join(imagens_path,"logodatavix.png")

    ##Funções 
    #Baixar as imagens dos botões caso não exista
    if not os.path.exists(Logo_DTV):
            with open(Logo_DTV, 'wb') as imagem:
                resposta = requests.get("https://lh5.googleusercontent.com/proxy/592TGgZkSYoKDjpxwHAc14ndg4834vedxPf4jLBFt1f5ffhsqcUMkvrFoIMmKUEXLh5UIWFkF44my7WATq_xa1k3-Tb8yqMTObSurQ4d", stream=True)
                if not resposta.ok:
                    print("Ocorreu um erro, status:" , resposta.status_code)
                else:
                    for dado in resposta.iter_content(1024):
                        if not dado:
                            break
                        imagem.write(dado)
   
    return Logo_DTV                                