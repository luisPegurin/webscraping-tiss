import tabula as tb
import pandas as pd
import numpy as np
from zipfile import ZipFile


filePath = './componente_organizacional.pdf'


def main():
	dfs = tb.read_pdf(filePath, pages='114-120' , pandas_options={'header': None},encoding='utf-8', lattice=True, multiple_tables = True)

	# Quadro 30
	table30 = dfs[0].iloc[4:9, [0,1]]
	table30.columns = ['Código', 'Descrição da categoria']

	# Quadro 31
	dfs[3] = dfs[3].iloc[2:, [0,1]]
	table31 = pd.concat([dfs[3], dfs[4], dfs[5], dfs[6], dfs[7], dfs[8]])
	table31.columns = ['Código', 'Descrição da categoria']
	table31.iloc[:, 0] = table31.iloc[:, 0].apply(int)
	table31.iloc[:, 1] = table31.iloc[:, 1].replace('\r', ' ', regex=True)

	#Quadro 32
	table32 = dfs[9].iloc[4:7, [0,1]]
	table32.columns = ['Código', 'Descrição da categoria']

	#create csv
	table30.to_csv('Quadro30.csv', sep=',', encoding='utf-8',index=False) 
	table31.to_csv('Quadro31.csv', sep=',', encoding='utf-8',index=False) 
	table32.to_csv('Quadro32.csv', sep=',', encoding='utf-8',index=False) 


	# zip csv's
	with ZipFile('Teste_Luis_Henrique.zip', 'w') as myzip:
	    myzip.write('Quadro30.csv') 
	    myzip.write('Quadro31.csv') 
	    myzip.write('Quadro32.csv') 

if __name__ == '__main__':
	main()