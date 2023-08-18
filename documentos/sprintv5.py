import psutil
import time

def monitorar_recursos():
    while True:
        uso_cpu = psutil.cpu_percent(interval=1)
        print(f"Uso da CPU: {uso_cpu}%")

        uso_disco = psutil.disk_usage('/')
        print(f"Uso do disco: {uso_disco.percent}%")

        uso_memoria = psutil.virtual_memory()
        print(f"Uso da memória: {uso_memoria.percent}%")

        print("=" * 40)

        time.sleep(3)

print("Monitoramento de recursos iniciado. Pressione Ctrl + C para pausar.")
try:
    monitorar_recursos()
except KeyboardInterrupt:
    print("\nMonitoramento pausado. Pressione Enter para retomar ou Ctrl + C para sair.")
    input()
    print("Retomando o monitoramento...")
    monitorar_recursos()

#para conseguirmos puxar o while true posteriormente, colocamos ele dentro de uma def (para o ciclo ficar salvo em algum lugar)
#utilizamos o try e except para parar e retornar o loop, ele para com o atalho KeyboardInterrupt (control c) e volta a funcionar com a tecla enter
#try e except é similiar a um If e Else, o programa tenta fazer algo (try) e só não irá fazer com uma condição (except)

#script feito pelo grupo 1: Anthony Bento, Yasmin Yuri, Gabriel Sanchez, Gabriel Nunes, Maria Paula e Davi Soo.
    


