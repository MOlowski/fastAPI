import pandas as pd

df = pd.read_csv(r"C:\Users\Maciek\Desktop\python\fastAPI\ing\wine_reviews.csv")
df = df[['brand','name']]


df_tmp = df
df_tmp['category'] = ""
print(df.columns)
category_list = ["beer", "wine", "cider", "mead", "sake", "gin", "brandy", "whiskey", "rum", "tequila", "vodka", "absinthe"]

df_tmp = df_tmp.astype(str).apply(lambda col: col.str.lower())

for index,row in df_tmp.iterrows():
    for item in category_list:
        if item in row['name']:
            row['category'] = item
    words = row['name'].split()
    if len(words) > 2:
        row['name'] = words[0] + "-" + words[1]
for index, row in df_tmp.iterrows():
    if row["category"] == "":
        row['category'] = 'alcohol'
df_tmp = df_tmp.replace(" ", "-", regex=True)
df_tmp = df_tmp.replace("\'", "", regex=True)
df_tmp = df_tmp.replace("\"", "", regex=True)

print(df_tmp.head)

df_tmp = df_tmp.drop_duplicates()
df_tmp = df_tmp[df_tmp.brand != "nan"]
df_tmp.to_csv(r"C:\Users\Maciek\Desktop\python\fastAPI\ing\wines.csv")


