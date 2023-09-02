import psutil
import time

while(True):

        #informações do disco
        disk_usage = psutil.disk_usage('/')
        total_disk = disk_usage.total
        used_disk = disk_usage.used
        uso_disco = round(psutil.disk_usage('/').percent, 2)
        total_disk_gb = round(total_disk / (1024 ** 3), 2)  # Convertendo bytes para GB
        used_disk_gb = round(used_disk / (1024 ** 3), 2)    # Convertendo bytes para GB


        #informações da cpu
        uso_cpu = round(psutil.cpu_percent(interval=1), 2)
        cpu_freq = psutil.cpu_freq()
        load = psutil.getloadavg()

        #informações da memória ram
        memory = psutil.virtual_memory()
        used_ram = memory.used
        total_ram = memory.total
        uso_memoria = round(psutil.virtual_memory().percent, 2)
        total_ram_gb = round(total_ram / (1024 ** 3), 2)  # Convertendo bytes para GB
        used_ram_gb = round(used_ram / (1024 ** 3), 2)    # Convertendo bytes para GB

        print("\r\n")
        print("MONITORAMENTO DO DISCO")
        print(f"Total do disco: {total_disk_gb}GB")
        print(f"Uso do disco: {used_disk_gb}GB")
        print(f"Porcentagem do uso do disco: {uso_disco}%")
        print("\r\n")
    
        print("MONITORAMENTO DA MEMÓRIA RAM")
        print(f"Total da memória: {total_ram_gb}GB")
        print(f"Uso da memória: {used_ram_gb}GB") 
        print(f"Porcentagem de uso da memória: {uso_memoria}%")
        print("\r\n")

        print("MONITORAMENTO DA CPU")
        print(f"Uso da CPU: {uso_cpu}%")
        print(f"Frequência da CPU: {cpu_freq.current:.2f} MHz")
        print("=" * 40)

        
        
        time.sleep(10)
   


    



