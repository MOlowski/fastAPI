import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\Maciek\Desktop\python\fastAPI\ing\alcohol_reviews.csv")

df = df[['brand','name']]
df_tmp = df

df_tmp['category'] = df_tmp['name']

print(df.columns)

category_list = ['beer', 'wine', 'cider', 'mead', 'sake', 'gin', 'brandy', 'whiskey', 'rum', 'tequila', 'vodka', 'absinthe']

#all data to lowercase
df_tmp = df_tmp.astype(str).apply(lambda col: col.str.lower())

#assign category based on values from name column
for item in category_list:
    df_tmp['category'] = df_tmp['category'].apply(lambda row: item if item in row else row)

#if category wasnt assinged, value in category column take value from brand column
df_tmp.loc[df_tmp['category']==df_tmp['name'], 'category'] = df_tmp['brand']

#assign unaassigned categories based values from brand column
for item in category_list:
    df_tmp['category'] = df_tmp['category'].apply(lambda row: item if item in row else row)

#if category is unassigned, take value 'alcohol'
df_tmp.loc[df_tmp['category']==df_tmp['brand'], 'category'] = 'alcohol'

#if name has more than 2 words drop others
df_tmp['name'] = df_tmp['name'].apply(lambda row: row.split()[0]+"-"+row.split()[1] if len(row.split())>2 else row)

#replace
df_tmp = df_tmp.replace(" ", "-", regex=True)
df_tmp = df_tmp.replace("\'", "", regex=True)
df_tmp = df_tmp.replace("\"", "", regex=True)

#drop duplicates
df_tmp = df_tmp.drop_duplicates()

#drop rows without brand value
df_tmp = df_tmp[df_tmp.brand != "nan"]

df_tmp.to_csv(r"C:\Users\Maciek\Desktop\python\fastAPI\ing\alcohols.csv")