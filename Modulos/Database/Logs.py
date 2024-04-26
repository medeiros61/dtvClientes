
import pymysql
from datetime import datetime, date,timedelta
import socket
import uuid
import requests

execução = 0

def connect_to_da():
    global connection
    connection = pymysql.connect(
            host='mysql02-farm10.kinghost.net',
            user='datavixsolucao',
            password='R4QePW2ze9Hpa6F',
            database='datavixsolucao'
        )
    
def dadosdesegurnaça():
    global hostname,ip,endereco_mac
    ## Dados de Segurança
    # Obtém o nome da máquina
    hostname = socket.gethostname()

    def getip():
        try:
            response = requests.get('https://httpbin.org/ip')
            if response.status_code == 200:
                ip_info = response.json()
                global_ip = ip_info['origin']
                return global_ip
            else:
                return "NO IP"
        except Exception as e:
            return f'Erro: {e}'

    ip = getip()
    # Obtém o endereço MAC da interface de rede padrão
    
    endereco_mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])

def RegistrarEventosdeLOG(evento,usuario):
    if execução == 0 :
        global segurança
        dadosdesegurnaça()

        segurança = f'HOST:{hostname} IP:{ip} MAC:{endereco_mac}'

    # Obter a data e hora atual
    #agora = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")

    dadosdeLog=[usuario[3],usuario[2],evento,segurança]
    connect_to_da()
    
    try:
        with connection.cursor() as cursor:
            ConsultaSQL = f"INSERT INTO `pylogs` (`nome`,`role`, `action`, `security_data`) VALUES ('{dadosdeLog[0]}', '{dadosdeLog[1]}', '{dadosdeLog[2]}', '{dadosdeLog[3]}')"
            
            cursor.execute(ConsultaSQL)
            connection.commit() 

    finally:
        connection.close()
