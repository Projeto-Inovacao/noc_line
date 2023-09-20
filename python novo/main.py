import psutil #interface para monitoramentos
import threading
import time #para pausar o sistema
import keyboard #intereção com as teclas
import datetime #para trabalhar com dataHora
import mysql.connector #para conectar com bd
from cred import usr, pswd 

event = threading.Event() #criado para conseguir para o sistema
print(event)

def stop(): #define o evento para parar o monitoramento (tecla esc)
    event.set() #para o evento
    print("\nFinalizando monitoramento")
    print('event')

keyboard.add_hotkey("esc", stop)

print('monitorando do hardware...')

while not event.is_set(): #inicia um loop que só para quando o evento stop for chamado
    uso_cpu = round(psutil.cpu_percent(), 2) #percent uso cpu
    uso_disco = round(psutil.disk_usage('/').percent, 2) #percent uso disco
    uso_memoria = round(psutil.virtual_memory().percent, 2) #percent uso ram
    data = datetime.datetime.now() #dataHora
    if (uso_cpu < 0 or uso_disco < 0 or uso_memoria < 0): # se os parametros estiverem ok roda isso
        print("\r\n")
        print("valores dentro do padrão")
        print('DISCO {:.2f}%'.format(uso_disco))
        print('RAM {:.2f}%'.format(uso_memoria))
        print('CPU {:.2f}%'.format(uso_cpu))
    else: #se os parametros do monitoramento não estiverem ok roda isso
        print("\r\n")
        print("valores acima do padrão")
        print('DISCO {:.2f}% ...ALERTA'.format(uso_cpu))
        print('RAM {:.2f}% ...ALERTA'.format(uso_disco))
        print('CPU {:.2f}% ...ALERTA'.format(uso_memoria))
        try: #tenta conectar no banco
            mydb = mysql.connector.connect(host = 'localhost', user = 'root', password = 'sptech', database = 'nocLine') #passa as credencias de acesso ao bd
            if mydb.is_connected():
                db_info = mydb.get_server_info() #obtem informações do servidor mysql
                
                mycursor = mydb.cursor() #ladainha do sql

                sql_query = "insert into monitoramento(uso_percent, fkMaquinaMonitoramento, fkEmpresaMonitoramento, fkComponentes, dtHora)VALUES (%s, %s, %s, %s, %s), (%s, %s, %s, %s, %s), (%s, %s, %s,%s,%s);" #aqui passa as colunas da tabela no sql
                val = [uso_cpu, 1, 1, 1, data, uso_disco, 1, 1, 3, data, uso_memoria, 1, 1, 2, data] #aqui pega os valores que vão ser inseridos na tabela
                mycursor.execute(sql_query, val) #executa a consulta no sql com a query e com e val

                mydb.commit() #se tiver tudo ok, aqui ele da o insert no banco
                print(mycursor.rowcount, "registros inseridos no banco") #esse rowcount fala o número de registros inseridos de uma vez
                print("\r\n")
        except mysql.connector.Error as e: #aqui é se der ruim com o banco, cai nesse erro
            print("Erro ao conectar com o MySQL", e)
        finally:
            if(mydb.is_connected()): #verifica se a conexão com o banco de dados está aberta
                mycursor.close() #aqui fecha uma parte
                mydb.close() #aqui fecha outra, só vai cair aqui dentro se clicar esq, ai chama a função de fechar o loop, caso contrario continua dando insert
    time.sleep(2)
