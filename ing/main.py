import requests
import json
import pandas as pd

from request import request


category_list = ["beer", "wine", "cider", "mead", "sake", "gin", "brandy", "whiskey", "rum", "tequila", "vodka", "absinthe"]

URL = "https://urlkeywords.cloudtechnologies.dev/keywordURLs"

headers = {"Content-Type": "application/json"}

optional_threshold = 1

df = pd.read_csv(r"C:\Users\Maciek\Desktop\python\fastAPI\ing\alcohols.csv")
Brand = df["brand"]
Name = df["name"]
category = df["category"]

matched_res = request(Brand, Name, category, URL, headers, optional_threshold)
print(matched_res)


