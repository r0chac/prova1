# -*- coding: utf-8 -*-
"""
Created on Mon May 20 18:09:04 2024

@author: recad
"""
#print('hello world')

import numpy as np
import matplotlib.pyplot as plt

temperatura = (60, 80, 60, 40, 80, 40, 40, 40, 40, 15, 40, 15, 40, 15, 40, 15, 40, 15)
corrosao = (3.6,36,90,3.6,180,27,110,470,665,65,6500,180,6500,258,1080,430,540,50)
#print(len(temperatura))
#print(len(corrosao))

plt.scatter(temperatura, corrosao, color='black', edgecolor='black')
plt.title('Relação entre Temperatura e Corrosão')
plt.xlabel('Temperatura')
plt.ylabel('Corrosão')
plt.show()

correlacao = np.corrcoef(temperatura, corrosao)[0, 1]
print("Correlação Amostral:", correlacao)

from scipy.stats import linregress

slope, intercept, r_value, p_value, std_err = linregress(temperatura, corrosao)
print(f"Slope: {slope}, Intercept: {intercept}, R-squared: {r_value**2}, P-value: {p_value}")

