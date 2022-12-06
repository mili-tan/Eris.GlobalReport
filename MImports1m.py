
import ipdb
import pandas as pd

asName = {}
asCounty = {}
global data, country, tlds, cnData, cnCityData

with open("as-name.csv", "r") as f:
    lines = f.readlines()
    for i in lines:
        sp = i.split(',')
        asName[sp[0]] = "".join(sp[1:-1]).strip()
        asCounty[sp[0]] = sp[-1].strip()

data = pd.read_csv("global-list-1m.csv", sep=",", header=None)
country = pd.read_csv('country-of-pyecharts.csv', header=None, index_col=1).squeeze().to_dict()

tlds = data[1].str.upper().str.split('.', expand=True)[1]

# print(data[1], data[0])
# print(data[3].value_counts().head(10))
# print(data[4].value_counts().head(10))
# print(data)

cnData = data[data[3] == "CN"]
cnData = cnData.append(data[data[3] == "TW"])
cnData = cnData.append(data[data[3] == "HK"])
cnData = cnData.append(data[data[3] == "MO"])

db = ipdb.City("ipipfree.ipdb")
cnCityData = []
for item in cnData[2]:
    city = db.find_info(addr=str(item), language="CN").city_name
    if city == "桃园市" or city == "新北市": city = "桃园"
    if len(city) == 0: city = "香港"
    cnCityData.append([item, city])
cnCityData = pd.DataFrame(cnCityData)[1].value_counts()

print("OK".center(30, "-"))