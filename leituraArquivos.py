import pandas as pd

#leitura de arquivo HTML
df_html = pd.read_html('https://www.muz.ifsuldeminas.edu.br/vestibular/2686-divulgado-resultado-final-do-processo-seletivo-para-cursos-tecnicos-integrado-e-subsequente')
df_html = df_html[0]

df_aluguel = pd.read_csv('./DATABASE/aluguel.csv', sep=";")

#criando um dataFrame com a coluna Tipo
df_tipos = pd.DataFrame(df_aluguel['Tipo'])
df_tipos.drop_duplicates(keep='first', inplace=True)
df_tipos.index = list(range(22))
df_tipos.to_csv('./NEWDATABASES/tipo_movel.csv',sep=",", index=False)

#print(df_tipos)

#leitura de arquivo TXT
# dados_txt = pd.read_table('./DATABASE/paciente.txt')
# dados_txt = pd.read_csv('./DATABASE/paciente.txt',sep="\t")
# print(dados_txt)

df_bairro = pd.DataFrame(df_aluguel['Bairro'])
df_bairro.drop_duplicates(keep='first', inplace=True)
df_bairro.index = list(range(162))
df_bairro.to_csv('./NEWDATABASES/bairro_movel.csv',sep=",", index=False)
df_bairro.to_html('./NEWDATABASES/bairro_movel.html', index=False)
df_bairro.to_excel('./NEWDATABASES/bairro_movel.xlsx', index=False)
df_bairro.to_json('./NEWDATABASES/bairro_movel.json')