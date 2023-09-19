import psutil
import threading
import time
import keyboard
import datetime
import mysql.connector
from cred import usr, pswd

event = threading.Event()
print(event)

def stop():
    event.set()
    print("\nFinalizando monitoramento")
    print('event')

keyboard.add_hotkey("esc", stop)

print('monitorando do hardware...')

while not event.is_set():
    uso_cpu = round(psutil.cpu_percent(), 2)
    uso_disco = round(psutil.disk_usage('/').percent, 2)
    uso_memoria = round(psutil.virtual_memory().percent, 2)
    data = datetime.datetime.now()
    if (uso_cpu < 0 or uso_disco < 0 or uso_memoria < 0):
        print("\r\n")
        print("valores dentro do padrão")
        print('DISCO {:.2f}%'.format(uso_disco))
        print('RAM {:.2f}%'.format(uso_memoria))
        print('CPU {:.2f}%'.format(uso_cpu))
    else:
        print("\r\n")
        print("valores acima do padrão")
        print('DISCO {:.2f}% ...ALERTA'.format(uso_cpu))
        print('RAM {:.2f}% ...ALERTA'.format(uso_disco))
        print('CPU {:.2f}% ...ALERTA'.format(uso_memoria))
        try:
            mydb = mysql.connector.connect(host = 'localhost', user = 'root', password = 'sptech', database = 'nocLine')
            if mydb.is_connected():
                db_info = mydb.get_server_info()
                
                mycursor = mydb.cursor()

                sql_query = "insert into monitoramento(uso_percent, fkMaquinaMonitoramento, fkEmpresaMonitoramento, fkComponentes, dtHora)VALUES (%s, %s, %s, %s, %s), (%s, %s, %s, %s, %s), (%s, %s, %s,%s,%s);"
                val = [uso_cpu, 1, 1, 1, data, uso_disco, 1, 1, 3, data, uso_memoria, 1, 1, 2, data]
                mycursor.execute(sql_query, val)

                mydb.commit()
                print(mycursor.rowcount, "registros inseridos no banco")
                print("\r\n")
        except mysql.connector.Error as e:
            print("Erro ao conectar com o MySQL", e)
        finally:
            if(mydb.is_connected()):
                mycursor.close()
                mydb.close()
    time.sleep(2)
