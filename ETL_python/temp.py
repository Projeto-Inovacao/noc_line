import statistics as st #biblioteca que faz calculo de estasticas
import pandas as pd #biblioteca que faz a leitura do csv
import numpy 
data_temp = pd.read_csv(r"C:/Users/Gisele/Downloads/ohml_trusted.csv") #ajustar conforme alocação do arquivo
print(data_temp) #conferindo o arquivo ;)

temperatura = data_temp["CPU Package"]
array_temp = temperatura.to_numpy()
print(array_temp)

maximo_temp = max(array_temp)
minimo_temp = min(array_temp)

print('A media da amostra é {}'.format(st.mean(array_temp),2))
print('A mediana da amostra é {}'.format(st.median(array_temp)))
print("Maximum = {}, Minimum = {}".format(maximo_temp, minimo_temp))
print('Os quartis da amostra são:', st.quantiles(array_temp, n=4, method='inclusive'))

