import os
import json
import pandas as pd
import pyreadstat as pyspss

os.chdir('/Users/angelseda/Documents/angel/workingWithLocalFiles/data')

#Open json file
print('Json File')
file = 'subvenciones.json'
with open(file, encoding ='utf-8') as fichero:
    datos = json.load(fichero)
print(datos[0:5])

#show types
#print(type(datos))
#print(type(datos[0]))

subvenciones = pd.DataFrame(datos)
print(subvenciones.head(10))
print('******************************************************************')

#Open excel file
print('Excel File')
file_xlsx ='subvenciones.xls'
dataExcel=pd.read_excel(file_xlsx,sheet_name='Hoja1')
print(dataExcel.head(10))
print('******************************************************************')

#Open spss file
print('SPSS File')
filesav = 'distritos.sav'
df,meta =pyspss.read_sav(filesav)
print(df.head(10))
print('******************************************************************')

#Open stata file
print('Stata File')
varsOfInterest=["libcpre_self","libcpo_self","randordq_casitherm_illegal","strata_full","psu_full"]
file = 'anes_timeseries_2012.dta'
dataStata =pd.read_stata(file,columns=varsOfInterest)
print(dataStata.head(10))
print('******************************************************************')

#Open Csv file
print('CSV File')
fileCSV = 'bank.csv'
dataCSV = pd.read_csv(fileCSV,sep=';')
print(dataCSV.head(10))
print('******************************************************************')

#Open txt file
print('txt File')
fileTXT = 'FinancialSample.txt'
df=pd.read_csv(fileTXT,header=None,sep=';')
df.columns = ["Segment","Country","Product","Discount Band","Units Sold","Manufacturing Price",
              "Sale Price","Gross Sales","Discounts","Sales","COGS","Profit","Date","Month Number","Month Name","Year"]
print(df.head(10))