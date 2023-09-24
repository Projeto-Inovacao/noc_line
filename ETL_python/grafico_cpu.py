import statistics as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

data_temp = pd.read_csv(r"C:\Users\Gisele\Documents\noc_line-sp1\ETL_python/ohml_trusted.csv")
array_temp = data_temp["CPU Package"].to_numpy()
print(data_temp)

data_cpu = pd.read_csv(r"C:\Users\Gisele\Documents\noc_line-sp1\ETL_python/bolinha_cpu.csv")
array_cpu = data_cpu['uso(%)'].to_numpy()
print(data_cpu)

a_coef_angular, b_coef_linear = st.linear_regression(array_cpu, array_temp)
solucao = stats.linregress(array_cpu, array_temp)

def formula(a,b,x):
    return a*x + b

def graph(a,b , x_range):
     x = array_cpu
     y = formula(a,b,x)
     plt.scatter(array_cpu,array_temp)
     plt.plot(x,y)
     plt.xticks(np.arange(5, 40, step=5))
     plt.xlabel('CPU')
     plt.ylabel('Temperatura')
     plt.title('Relação CPU X TEMP')
     plt.grid()
     plt.show()

graph(a_coef_angular, b_coef_linear, range(5, 35))
