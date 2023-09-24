import statistics as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

data_temp = pd.read_csv(r"C:\Users\Gisele\Documents\noc_line-sp1\ETL_python/ohml_trusted.csv")
array_temp = data_temp["CPU Package"].to_numpy()
print(data_temp)

data_ram = pd.read_csv(r"C:\Users\Gisele\Documents\noc_line-sp1\bolinha_ram.csv")
print(data_ram)
array_ram = data_ram['uso'].to_numpy()

a_coef_angular, b_coef_linear = st.linear_regression(array_ram, array_temp)
solucao = stats.linregress(array_ram, array_temp)

def formula(a,b,x):
    return a*x + b

def graph(a,b , x_range):
     x = array_ram
     y = formula(a,b,x)
     plt.scatter(array_ram,array_temp)
     plt.plot(x,y)
     plt.xticks(np.arange(5, 40, step=5))
     plt.xlabel('RAM')
     plt.ylabel('Temperatura')
     plt.title('Relação RAM X TEMP')
     plt.grid()
     plt.show()

graph(a_coef_angular, b_coef_linear, range(5, 35))
