import flag
import pandas as pd
import pywebio.output
from pyecharts import options as opts
from pyecharts.charts import Map, Bar, Geo
from pyecharts.globals import ThemeType

from pywebio.output import *
import MContext
import MImports10k

import MImports1m

def app():
    clear()
    put_html(MContext.nav)

    put_html("<h1>前一万</h1>")
    cnCityChart = (
        Geo(init_opts=opts.InitOpts(width="850px",
                                    height="500px",
                                    theme=ThemeType.LIGHT))
        .add_schema(maptype="china")
        .add(
            "站点数",
            [list(z) for z in zip(MImports10k.cnCityData.keys().tolist(), MImports10k.cnCityData.values.tolist())],
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title="中国（含港澳台）热门网站服务器 IP 分布城市"),
                         visualmap_opts=opts.VisualMapOpts(max_=15))
    )
    pywebio.output.put_html(cnCityChart.render_notebook())

    asNumberCN = ", AS" + MImports10k.cnData[4].value_counts().head(20).keys().astype('str')
    asnNameCN = (MImports10k.cnData[4].value_counts().head(20).keys().astype('str').map(MImports10k.asName) + asNumberCN).tolist()
    asnValueCN = MImports10k.cnData[4].value_counts().head(20).values.tolist()

    asnChart1 = (
        Bar(init_opts=opts.InitOpts(width="1024px", height="500px", theme=ThemeType.LIGHT))
        .add_xaxis(asnNameCN)
        .add_yaxis("站点数", asnValueCN)
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title="中国（含港澳台）热门网站服务器网络所属 ASN"))
    )

    pywebio.output.put_html(asnChart1.render_notebook())
    put_html("<hr>")

    put_html("<h1>前一百万</h1>")
    cnCityChart = (
        Geo(init_opts=opts.InitOpts(width="850px",
                                    height="500px",
                                    theme=ThemeType.LIGHT))
        .add_schema(maptype="china")
        .add(
            "站点数",
            [list(z) for z in zip(MImports1m.cnCityData.keys().tolist(), MImports1m.cnCityData.values.tolist())],
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title="中国（含港澳台）热门网站服务器 IP 分布城市"),
                         visualmap_opts=opts.VisualMapOpts(max_=50))
    )
    pywebio.output.put_html(cnCityChart.render_notebook())

    asNumberCN = ", AS" + MImports1m.cnData[4].value_counts().head(20).keys().astype('str')
    asnNameCN = (MImports1m.cnData[4].value_counts().head(20).keys().astype('str').map(MImports1m.asName) + asNumberCN).tolist()
    asnValueCN = MImports1m.cnData[4].value_counts().head(20).values.tolist()

    asnChart1 = (
        Bar(init_opts=opts.InitOpts(width="1024px", height="500px", theme=ThemeType.LIGHT))
        .add_xaxis(asnNameCN)
        .add_yaxis("站点数", asnValueCN)
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title="中国（含港澳台）热门网站服务器网络所属 ASN"))
    )

    pywebio.output.put_html(asnChart1.render_notebook())
    put_html("<hr>")
