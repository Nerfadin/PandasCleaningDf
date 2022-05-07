import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import openpyxl

# Load files into pandas
df2019 = pd.read_csv("vendas_linha_petshop_2019.csv", sep=';', encoding='unicode_escape')
df2020 = pd.read_csv("vendas_linha_petshop_2020.csv", sep=';', encoding='unicode_escape')
df2021 = pd.read_csv("vendas_linha_petshop_2021.csv", sep=';', encoding='unicode_escape')
df2022 = pd.read_csv("vendas_linha_petshop_2022.csv", sep=';', encoding='unicode_escape')

#create dataFrame with concatenated files
df = pd.concat([ df2020, df2021, df2019 ])

def IterateSpecificColumnByName(dataFrame):
    for i in range(len(dataFrame)):
        print(dataFrame.loc[i, "valor"])

def IterateSpecificColumnByIndex(dataFrame, index):
    for i in range(len(dataFrame)):
        df.loc[i, index]


IterateSpecificColumnByIndex(df, 0)

"""
missing_cod.assign(missing =missing_cod['n']/n_empty).sort_values('n')
print(missing_cod)
df_missing = pd.DataFrame([range(3), [0, np.NaN, 0], [0, 0, np.NaN], range(3), range(3)])
df_missing.isnull()
"""
