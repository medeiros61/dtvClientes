import requests
import random
import string

#remetente = 'noreplaydatavix@gmail.com'
#senha = 'Dtv@KKNoRpy2024'
def gerar_codigo():
    caracteres = string.ascii_letters + string.digits
    codigo = ''.join(random.choice(caracteres) for _ in range(6))
    global Token
    Token = codigo


def EnviodoToken(Email):
    gerar_codigo()
    # URL do script Google Apps Script
    url = "https://script.google.com/macros/s/AKfycbxGBoDHMuD87e9b9HF3eitZ7kYGOSgoxkNcZhjTRcXhd7ZsvrUZbDSQQyF8Ybj4pi4ijg/exec"

    # Parâmetros a serem passados para o script (codigo e destinatario)
    params = {
        "codigo": f"{Token}",  # Substitua pelo código de verificação desejado
        "destinatario": f"{Email}"  # Substitua pelo destinatário do email
    }

    # Faz a requisição GET para o script
    response = requests.get(url, params=params)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        #print("Email enviado com sucesso!")
        return True
    else:
        return False
        #print("Erro ao enviar o email:", response.text)

def verificação(Valorinformado):
    if Token == Valorinformado:
        return True
    else:
        return False