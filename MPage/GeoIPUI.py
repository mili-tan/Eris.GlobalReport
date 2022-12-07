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

    countryValue = MImports10k.data[3].map(MImports10k.country).value_counts().values.tolist()
    countryName = MImports10k.data[3].map(MImports10k.country).value_counts().keys().tolist()

    countryChart1 = (
        Map(init_opts=opts.InitOpts(width="850px",
                                    height="500px",
                                    theme=ThemeType.LIGHT))
        .add("站点数",
             [list(z) for z in zip(countryName, countryValue)]
             , "world")
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="热门网站服务器 IP 分布国家（地区）"),
            visualmap_opts=opts.VisualMapOpts(max_=1000),
        )
    )

    pywebio.output.put_html(countryChart1.render_notebook())

    countryValue15 = MImports10k.data[3].value_counts().head(20).values.tolist()
    countryName15 = MImports10k.data[3].value_counts().head(20).keys().tolist()

    for n in range(len(countryName15)):
        if countryName15[n] != "AnyCast":
            countryName15[n] = flag.flag(countryName15[n]) + " " + countryName15[n]
        else:
            countryName15[n] = "🌏 " + countryName15[n]

    countryChart2 = (
        Bar(init_opts=opts.InitOpts(width="850px",
                                    height="500px",
                                    theme=ThemeType.LIGHT))
        .add_xaxis(countryName15)
        .add_yaxis("站点数", countryValue15)
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title="热门网站服务器 IP 分布国家（地区）"))
    )

    pywebio.output.put_html(countryChart2.render_notebook())

    asNumber = ", AS" + MImports10k.data[4].value_counts().head(20).keys().astype('str')
    asnName = (MImports10k.data[4].value_counts().head(20).keys().astype('str').map(MImports10k.asName) + asNumber).tolist()
    asnValue = MImports10k.data[4].value_counts().head(20).values.tolist()

    asnChart1 = (
        Bar(init_opts=opts.InitOpts(width="1024px", height="500px", theme=ThemeType.LIGHT))
        .add_xaxis(asnName)
        .add_yaxis("站点数", asnValue)
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title="热门网站服务器网络所属 ASN"))
    )
    pywebio.output.put_html(asnChart1.render_notebook())

    asnCountryValue15 = MImports10k.data[4].astype('str').map(MImports10k.asCounty).value_counts().head(20).values.tolist()
    asnCountryName15 = MImports10k.data[4].astype('str').map(MImports10k.asCounty).value_counts().head(20).keys().tolist()

    for n in range(len(asnCountryName15)):
        if asnCountryName15[n] != "AnyCast":
            asnCountryName15[n] = flag.flag(asnCountryName15[n]) + " " + asnCountryName15[n]

    asnChart2 = (
        Bar(init_opts=opts.InitOpts(width="850px",
                                    height="500px",
                                    theme=ThemeType.LIGHT))
        .add_xaxis(asnCountryName15)
        .add_yaxis("站点数", asnCountryValue15)
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title="热门网站服务器所属 ASN 国家（地区）"))
    )

    pywebio.output.put_html(asnChart2.render_notebook())

    put_html("<hr>")

    put_html("<h1>前一百万</h1>")
    countryValue = MImports1m.data[3].map(MImports1m.country).value_counts().values.tolist()
    countryName = MImports1m.data[3].map(MImports1m.country).value_counts().keys().tolist()
    countryChart1 = (
        Map(init_opts=opts.InitOpts(width="850px",
                                    height="500px",
                                    theme=ThemeType.LIGHT))
        .add("站点数",
             [list(z) for z in zip(countryName, countryValue)]
             , "world")
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="热门网站服务器 IP 分布国家（地区）"),
            visualmap_opts=opts.VisualMapOpts(max_=25000),
        )
    )
    pywebio.output.put_html(countryChart1.render_notebook())

    countryValue15 = MImports1m.data[3].value_counts().head(20).values.tolist()
    countryName15 = MImports1m.data[3].value_counts().head(20).keys().tolist()
    for n in range(len(countryName15)):
        if countryName15[n] != "AnyCast":
            countryName15[n] = flag.flag(countryName15[n]) + " " + countryName15[n]
        else:
            countryName15[n] = "🌏 " + countryName15[n]
    countryChart2 = (
        Bar(init_opts=opts.InitOpts(width="850px",
                                    height="500px",
                                    theme=ThemeType.LIGHT))
        .add_xaxis(countryName15)
        .add_yaxis("站点数", countryValue15)
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title="热门网站服务器 IP 分布国家（地区）"))
    )
    pywebio.output.put_html(countryChart2.render_notebook())

    asNumber = ", AS" + MImports1m.data[4].value_counts().head(20).keys().astype('str')
    asnName = (MImports1m.data[4].value_counts().head(20).keys().astype('str').map(MImports1m.asName) + asNumber).tolist()
    asnValue = MImports1m.data[4].value_counts().head(20).values.tolist()
    asnChart1 = (
        Bar(init_opts=opts.InitOpts(width="1024px", height="500px", theme=ThemeType.LIGHT))
        .add_xaxis(asnName)
        .add_yaxis("站点数", asnValue)
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title="热门网站服务器网络所属 ASN"))
    )
    pywebio.output.put_html(asnChart1.render_notebook())

    asnCountryValue15 = MImports1m.data[4].astype('str').map(MImports1m.asCounty).value_counts().head(20).values.tolist()
    asnCountryName15 = MImports1m.data[4].astype('str').map(MImports1m.asCounty).value_counts().head(20).keys().tolist()

    for n in range(len(asnCountryName15)):
        if asnCountryName15[n] != "AnyCast":
            asnCountryName15[n] = flag.flag(asnCountryName15[n]) + " " + asnCountryName15[n]

    asnChart2 = (
        Bar(init_opts=opts.InitOpts(width="850px",
                                    height="500px",
                                    theme=ThemeType.LIGHT))
        .add_xaxis(asnCountryName15)
        .add_yaxis("站点数", asnCountryValue15)
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title="热门网站服务器所属 ASN 国家（地区）"))
    )

    pywebio.output.put_html(asnChart2.render_notebook())
    put_html("<hr>")
