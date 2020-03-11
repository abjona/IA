import pandas as pd

dados = { 'Empresa':[
    'GOOGLE',
    'MICROSOFT',
    'MICROSOFT',
    'GOOGLE',
    'FACEBOOK',
    'MICROSOFT',
    'FACEBOOK',
    'GOOGLE',
],
'Nome' :[
    'Rodrigo',
    'Maisa',
    'Pedro',
    'Isabela',
    'Carlos',
    'Eder',
    'Carmem',
    'Lucio'
],
'Venda':[200, 120, 340, 124, 243, 350, 310, 280],
'Funcionario': [20, 13, 29, 12, 25, 39, 36, 27]
}

df = pd.DataFrame(dados)

dfPaciente = pd.read_csv('./DATABASE/paciente.csv', sep=";")
dfPaciente = pd.DataFrame(dfPaciente)

grupoEmpresa = df.groupby('Empresa')

#print(df)

#correlação
#print(df.corr())

#desvio padrao
#print(df['Venda'].std())

#media por grupo de empresa
#print(grupoEmpresa.mean())

#desvio padrao por grupo de empresa na coluna venda
#print(grupoEmpresa['Venda'].std())

#desc por grupo de empresa na tabela venda
#print(grupoEmpresa['Venda'].describe())

#media e desvio
#print(grupoEmpresa.agg(['mean','std']))

diag = dfPaciente.groupby('Diagnostico')

print(diag[['Idade','Peso','Temp.']].agg(['count','mean','std']))
