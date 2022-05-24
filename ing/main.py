import requests
import json
import pandas as pd

from request import request


category_list = ["beer", "wine", "cider", "mead", "sake", "gin", "brandy", "whiskey", "rum", "tequila", "vodka", "absinthe"]
URL = "https://urlkeywords.cloudtechnologies.dev/keywordURLs"

headers = {"Content-Type": "application/json"}


optional_threshold = 1

df = pd.read_csv(r"C:\Users\Maciek\Desktop\python\fastAPI\ing\wines.csv")
Brand = df["brand"]
Name = df["name"]
category = df["category"]

matched_res = request(Brand, Name, category, URL, headers, optional_threshold)
print(matched_res)
'''
with open("results.json","r") as f:
    data = json.load(f)
    for i in data['alcohol']:
        print("id:", i['alcohol_id'])
        for key,value in i["payload"].items():
            print(key, value)
        print("urls: ")
        for item in i["urls"]:
            print(item)
'''
