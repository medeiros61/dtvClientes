
import pymysql
from datetime import datetime, date,timedelta
import socket
import uuid
import requests
import threading
import time
execução = 0
dadosdeLog=[]

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
    global segurança
    segurança = f"HOST:{hostname}_IP:{ip}_MAC:{endereco_mac}"
    
def dadosusuario(dadosusuario):
    global usuario
    usuario = dadosusuario
    dadosdesegurnaça()

def activites(type):
    def Sessão_func():
        global Sessão
        if type == "Entrar":
            
            Sessão = True
            User = f"{usuario[3]}({usuario[1]}-{usuario[0]})"
            connect_to_da()
            try:
                with connection.cursor() as cursor:
                    ConsultaSQL = f"INSERT INTO `pyactivite` (`Usuarios`, `IPs`) VALUES ('{User}', '{ip}')"
                    cursor.execute(ConsultaSQL)
                    connection.commit()       
            finally:
                connection.close()
          

        if type == "Sair":
            time.sleep(1)
            
            Sessão = False
            connect_to_da()
            
            try:
                with connection.cursor() as cursor:
                    ConsultaSQL = f"DELETE FROM `pyactivite` WHERE `IPs` ='{ip}'"
                    cursor.execute(ConsultaSQL)
                    connection.commit()  
            except Exception as e:
                # Se ocorrer algum erro, faça rollback para reverter a transação
                connection.rollback()
                #print(f"Erro ao deletar: {e}")             
            finally:
                connection.close()

           
        

    #é preciso iniciar thread se nao o processo de registro fica lento
    ThredSessão = threading.Thread(target=Sessão_func)
    ThredSessão.start()

def RegistrarEventosdeLOG(evento,obs):
    
    global dadosdeLog,execução,segurança

        
        #segurança = f'HOST: IP: MAC:'

    #Obter a data e hora atual
    agora = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")

    dadosdeLog.append([f'{usuario[3]}({usuario[0]})', usuario[2], evento, segurança,agora])
   


def AtivarRegistrodeLog():
    def registro():

        while Sessão ==True:
            
            Contagem=0
            #é preciso dar um time sleep para a thread não entra em loop e travar programa
            time.sleep(10)
            qt = len(dadosdeLog)
            while Contagem < qt:
                Contagem +=1
                if len(dadosdeLog)>0:
                    #puxa os dados que é adicionado na listagem 
                    DadosparaRegistro=dadosdeLog[0]
                    connect_to_da()
                    try:
                        with connection.cursor() as cursor:
                            ConsultaSQL = f"CALL InsertPyLog('{DadosparaRegistro[0]}', '{DadosparaRegistro[1]}', '{DadosparaRegistro[4]}', '{DadosparaRegistro[2]}', '{DadosparaRegistro[3]}')"
                            
                            cursor.execute(ConsultaSQL)
                            connection.commit() 

                    finally:
                        dadosdeLog.pop(0)
                        connection.close()
                       
    #é preciso iniciar thread se nao o processo de registro fica lento
    BDLOGTread = threading.Thread(target=registro)
    BDLOGTread.start()