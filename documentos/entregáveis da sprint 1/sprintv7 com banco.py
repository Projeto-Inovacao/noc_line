import psutil
import time
import platform
from mysql.connector import connect
import datetime

def mysql_connection(host, user, passwd, database=None):
    connection = connect(
        host = host,
        user = user,
        passwd = passwd,
        database = database
    )
    return connection

connection = mysql_connection('localhost', 'root', 'sptech','nocLine')
while True:
        uso_cpu = round(psutil.cpu_percent(interval=1), 2)
        uso_disco = round(psutil.disk_usage('/').percent, 2)
        uso_memoria = round(psutil.virtual_memory().percent, 2)
        data = datetime.datetime.now()

        query = '''
        insert into monitoramento(uso_percent, fkMaquinaMonitoramento, fkEmpresaMonitoramento, fkComponentes, dtHora)
        VALUES (%s, %s, %s, %s, %s), (%s, %s, %s, %s, %s), (%s, %s, %s,%s,%s);
        '''
        insert = [uso_cpu, 1, 1, 1, data, uso_disco, 1, 1, 3, data, uso_memoria, 1, 1, 2, data]
        cursor = connection.cursor()
        cursor.execute(query, insert)
        connection.commit()

        print(f"Uso da CPU: {uso_cpu}%")
        print(f"Uso do disco: {uso_disco}%")
        print(f"Uso da memória: {uso_memoria}%")
        print("=" * 40)
        print("")
        
        time.sleep(20)
   


    



