import pandas as pd
import numpy as np

data_hami = pd.read_excel(r'Book2.xlsx', sheet_name='sheet1')
columns = data_hami.columns
columns = np.ravel(columns)
columns0List = data_hami[columns[0]].tolist()
columns1List = data_hami[columns[1]].tolist()
columns2List = data_hami[columns[2]].tolist()
columns3List = data_hami[columns[3]].tolist()
columns4List = data_hami[columns[4]].tolist()

df = pd.DataFrame({columns[1]:columns1List,
                    columns[2]:columns2List,
                    columns[3]:columns3List,
                    columns[4]:columns4List},
                    index=columns0List)

df["HAMI"] = df[columns[1]] + df[columns[2]] + df[columns[3]] - df[columns[4]]

df = df.drop(columns = [columns[1], columns[2], columns[3], columns[4]])

df.to_excel("HAMI-Georgia.xlsx")
