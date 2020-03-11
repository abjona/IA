import pandas as pd

# dados = [1,2,3]

# indices1 = ['Calc1','AED1','LP1','LP2']

# s1 = pd.Series(data=[23,89,30,37],index=indices1)

# indices2 = ['LP1','LP2','Geo','His']

# s2 = pd.Series(data=[48,90,23,12],index=indices2)

# print(s1+s2)
# print(s2)

dados = [[1,2,3],[4,5,6],[7,8,9]]

colunas = ['coluna ' + str(i) for i in range(1,4)]
linhas = ['linha ' + str(i) for i in range(1,4)]

s1 = pd.DataFrame(data=dados,index=linhas, columns=colunas)

print(s1)

print(s1.loc['linha 3','coluna 2'])

print(s1.loc[['linha 2','linha 3'],'coluna 2'])

print(s1.iloc[0:2,0:2])

s1.iloc[0,0] = 200

print(s1)