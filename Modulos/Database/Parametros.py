import pymysql
from datetime import date,datetime
import Modulos.Database.Conexao as Conectar
   
def pegar_parametro(parametro):
    # Conecta ao banco de dados
    
    conexao = Conectar.BancoDados_Dtv()
    
    try:	

        with conexao.cursor() as cursor:
            ConsultaSQL = f"SELECT `valor` FROM `pyparameter` WHERE `parametro`= '{parametro}'"
            cursor.execute(ConsultaSQL)
            results = cursor.fetchone()

            return results[0]
 

    finally:
        conexao.close()
