import json
import os

import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map, Bar
from pyecharts.globals import ThemeType

asnames = pd.read_json('asnames.json', typ='series')
data = pd.read_csv("cnlist.csv", sep=",", header=None)
country = pd.read_csv('Country_of_pyecharts.csv', header=None, index_col=1).squeeze().to_dict()

data[3] = data[3].map(country)
print(data[1], data[0])
print(data[3].value_counts().head(10))
print(data[4].value_counts().head(10))
print(data)

print("OK".center(30, "-"))

# countryValue = data[3].value_counts().values.tolist()
# countryName = data[3].value_counts().keys().tolist()
#
# countryValue15 = data[3].value_counts().head(15).values.tolist()
# countryName15 = data[3].value_counts().head(15).keys().tolist()
#
# ndata = []
# for index in range(len(countryName)):
#     info = [countryName[index], countryValue[index]]
#     ndata.append(info)
#
# c = (
#     Map()
#     .add("站点数", ndata, "world")
#     .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
#     .set_global_opts(
#         title_opts=opts.TitleOpts(title="全球前10K热门网站分布国家（地区）"),
#         visualmap_opts=opts.VisualMapOpts(max_=1000),
#
#     )
#     .render()
# )


# bar = (
#     Bar(init_opts=opts.InitOpts(width="1024px",
#                                 height="500px",
#                                 theme=ThemeType.LIGHT))
#     .add_xaxis(countryName15)
#     .add_yaxis("站点数", countryValue15)
#     .reversal_axis()
#     .set_series_opts(label_opts=opts.LabelOpts(position="right"))
#     .set_global_opts(title_opts=opts.TitleOpts(title="全球前10K热门网站分布国家（地区）"))
#     # .set_global_opts(yaxis_opts=opts.AxisOpts())
#     # .set_global_opts(yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)))
#     .render()
# )

asNumber = ", AS" + data[4].value_counts().head(15).keys().astype('str')
asnName = (data[4].value_counts().head(15).keys().map(asnames) + asNumber).tolist()
asnValue = data[4].value_counts().head(15).values.tolist()

bar = (
    Bar(init_opts=opts.InitOpts(width="1024px", height="500px", theme=ThemeType.LIGHT))
    .add_xaxis(asnName)
    .add_yaxis("站点数", asnValue)
    .reversal_axis()
    .set_series_opts(label_opts=opts.LabelOpts(position="right"))
    .set_global_opts(title_opts=opts.TitleOpts(title="全球前10K热门网站服务器网络所属 ASN"))
    .render()
)

# 打开html
os.system("render.html")
