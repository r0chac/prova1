#print('hello world')

import matplotlib.pyplot as plt

num =(2.7,54,140,3.6,36,90,3.6,180,27,110,9,470,665,65,72,6500,180,6500,258,1080,430,540,50)


plt.hist(num,bins=10,edgecolor='black')
plt.title('Histograma de Valores de Corrosão')
plt.xlabel('Valores')
plt.ylabel('Frequência')

plt.show()

