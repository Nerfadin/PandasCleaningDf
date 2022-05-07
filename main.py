import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import openpyxl

# Load files into pandas
df2019 = pd.read_csv("vendas_linha_petshop_2019.csv", sep=';', thousands=',', encoding='unicode_escape')
df2020 = pd.read_csv("vendas_linha_petshop_2020.csv", sep=';',thousands=',', encoding='unicode_escape')
df2021 = pd.read_csv("vendas_linha_petshop_2021.csv", sep=';',thousands=',', encoding='unicode_escape')
df2022 = pd.read_csv("vendas_linha_petshop_2022.csv", sep=';',thousands=',', encoding='unicode_escape')

#create dataFrame with concatenated files
df = pd.concat([ df2020, df2021, df2019 ])

def IterateSpecificColumnByName(dataFrame, name):
    for i in range(len(dataFrame)):
        print(dataFrame.loc[i, name])


def IterateSpecificColumnByIndex(dataFrame, index):
    for i in range(len(dataFrame)):
        df.loc[i, index]

df.insert(4, "valor_calculado", 0)
df["valor_total_bruto"] = df["valor_total_bruto"].astype(float)

df.astype({'valor_total_bruto': 'int32'}, errors='ignore').dtypes


"""
missing_cod.assign(missing =missing_cod['n']/n_empty).sort_values('n')
print(missing_cod)
df_missing = pd.DataFrame([range(3), [0, np.NaN, 0], [0, 0, np.NaN], range(3), range(3)])
df_missing.isnull()
"""

def getValorCalculado (a, b):
    return a * b

print(len(df))
for i in range(len(df)):
    if i < len(df):
        valorCalculado = getValorCalculado(df.loc[i, "valor"], df.loc[i, "valor_total_bruto"])
        
