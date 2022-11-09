import os

import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map

data = pd.read_csv("cnlist.csv", sep=",", header=None)
country = pd.read_csv('Country_of_pyecharts.csv', header=None, index_col=1).squeeze().to_dict()

data[3] = data[3].map(country)
print(data[1], data[0])
print(data[3].value_counts().head(10))
print(data[4].value_counts().head(10))
print(data)

print("OK".center(30, "-"))

value = data[3].value_counts().values.tolist()
attr = data[3].value_counts().keys().tolist()

data = []
for index in range(len(attr)):
    city_ionfo = [attr[index], value[index]]
    data.append(city_ionfo)

c = (
    Map()
    .add("站点数", data, "world")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="全球前10K热门网站分布国家（地区）"),
        visualmap_opts=opts.VisualMapOpts(max_=1000),

    )
    .render()
)

# 打开html
os.system("render.html")
