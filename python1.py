import numpy as np
path=('C:/Users/vikas/Downloads/flower.csv')
v=np.read_csv(path)
print(v)
table=pd.pivot_table(v,index=['Sepalwidthcm'],aggfunc=np.mean)
print(table)
