import flag
import pandas as pd
import pywebio.output
from pyecharts import options as opts
from pyecharts.charts import Map, Bar, Geo
from pyecharts.globals import ThemeType

from pywebio.output import *
import MContext

from MImports1m import data, country, asName, cnCityData, cnData, asCounty, tlds


def app():
    clear()
    put_html(MContext.nav)

    countryValue = data[3].map(country).value_counts().values.tolist()
    countryName = data[3].map(country).value_counts().keys().tolist()

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

    countryValue15 = data[3].value_counts().head(20).values.tolist()
    countryName15 = data[3].value_counts().head(20).keys().tolist()

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
        # .set_global_opts(yaxis_opts=opts.AxisOpts())
        # .set_global_opts(yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)))
    )

    pywebio.output.put_html(countryChart2.render_notebook())

    asNumber = ", AS" + data[4].value_counts().head(20).keys().astype('str')
    asnName = (data[4].value_counts().head(20).keys().astype('str').map(asName) + asNumber).tolist()
    asnValue = data[4].value_counts().head(20).values.tolist()

    asnChart1 = (
        Bar(init_opts=opts.InitOpts(width="1024px", height="500px", theme=ThemeType.LIGHT))
        .add_xaxis(asnName)
        .add_yaxis("站点数", asnValue)
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title="热门网站服务器网络所属 ASN"))
    )
    pywebio.output.put_html(asnChart1.render_notebook())

    cnCityChart = (
        Geo(init_opts=opts.InitOpts(width="850px",
                                    height="500px",
                                    theme=ThemeType.LIGHT))
        .add_schema(maptype="china")
        .add(
            "站点数",
            [list(z) for z in zip(cnCityData.keys().tolist(), cnCityData.values.tolist())],
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title="中国（含港澳台）热门网站服务器 IP 分布城市"),
                         visualmap_opts=opts.VisualMapOpts(max_=50))
    )
    pywebio.output.put_html(cnCityChart.render_notebook())

    asNumberCN = ", AS" + cnData[4].value_counts().head(20).keys().astype('str')
    asnNameCN = (cnData[4].value_counts().head(20).keys().astype('str').map(asName) + asNumberCN).tolist()
    asnValueCN = cnData[4].value_counts().head(20).values.tolist()

    asnChart1 = (
        Bar(init_opts=opts.InitOpts(width="1024px", height="500px", theme=ThemeType.LIGHT))
        .add_xaxis(asnNameCN)
        .add_yaxis("站点数", asnValueCN)
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title="中国（含港澳台）热门网站服务器网络所属 ASN"))
    )

    pywebio.output.put_html(asnChart1.render_notebook())

    asnCountryValue15 = data[4].astype('str').map(asCounty).value_counts().head(20).values.tolist()
    asnCountryName15 = data[4].astype('str').map(asCounty).value_counts().head(20).keys().tolist()

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
        .set_global_opts(title_opts=opts.TitleOpts(title="热门网站服务器网络 ASN 国家（地区）"))
    )

    pywebio.output.put_html(asnChart2.render_notebook())

    asCountyCount = pd.DataFrame.from_dict(asCounty, orient='index').value_counts()
    asCountyCountValue15 = asCountyCount.head(20).values.tolist()
    asCountyCountName15 = asCountyCount.head(20).keys().tolist()

    for n in range(len(asCountyCountName15)):
        if asCountyCountName15[n][0] != "ZZ":
            asCountyCountName15[n] = flag.flag(asCountyCountName15[n][0]) + " " + asCountyCountName15[n][0]
        else:
            asCountyCountName15[n] = "🌏 Global"

    asnChart3 = (
        Bar(init_opts=opts.InitOpts(width="850px",
                                    height="500px",
                                    theme=ThemeType.LIGHT))
        .add_xaxis(asCountyCountName15)
        .add_yaxis("自治系统数", asCountyCountValue15)
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title="全球网络 ASN 所属国家（地区）"))
    )

    pywebio.output.put_html(asnChart3.render_notebook())

    asCountyCountValue = asCountyCount.values.tolist()
    asCountyCountName = asCountyCount.keys().tolist()

    for index in range(len(asCountyCountName)):
        try:
            asCountyCountName[index] = country[asCountyCountName[index][0]]
        except:
            pass

    asnChart4 = (
        Map(init_opts=opts.InitOpts(width="850px",
                                    height="500px",
                                    theme=ThemeType.LIGHT))
        .add("自治系统数",
             [list(z) for z in zip(asCountyCountName, asCountyCountValue)]
             , "world")
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="全球 ASN 分布国家（地区）"),
            visualmap_opts=opts.VisualMapOpts(max_=10000),
        )
    )

    pywebio.output.put_html(asnChart4.render_notebook())

    tldValue20 = tlds.value_counts().head(20).values.tolist()
    tldName20 = tlds.value_counts().head(20).keys().tolist()

    for index in range(len(tldName20)):
        tldName20[index] = flag.flag(tldName20[index]) + " " + tldName20[index]

    tldChart = (
        Bar(init_opts=opts.InitOpts(width="850px",
                                    height="500px",
                                    theme=ThemeType.LIGHT))
        .add_xaxis(tldName20)
        .add_yaxis("站点数", tldValue20)
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title="热门网站域名后缀"))
    )

    pywebio.output.put_html(tldChart.render_notebook())

    tldCountryValue = tlds.map(country).value_counts().values.tolist()
    tldCountryName = tlds.map(country).value_counts().keys().tolist()

    tldCountryChart1 = (
        Map(init_opts=opts.InitOpts(width="850px",
                                    height="500px",
                                    theme=ThemeType.LIGHT))
        .add("站点数",
             [list(z) for z in zip(tldCountryName, tldCountryValue)]
             , "world")
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="热门网站域名后缀所属国家（地区）"),
            visualmap_opts=opts.VisualMapOpts(max_=10000),
        )
    )

    pywebio.output.put_html(tldCountryChart1.render_notebook())
