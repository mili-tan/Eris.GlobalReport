import flag
import pandas as pd
import pywebio.output
from pyecharts import options as opts
from pyecharts.charts import Map, Bar, Geo
from pyecharts.globals import ThemeType

from pywebio.output import *
import MImports1m
import MContext


def app():
    clear()
    put_html(MContext.nav)
    put_html("<h1>全球 ASN（自治系统）</h1>")

    asCountyCount = pd.DataFrame.from_dict(MImports1m.asCounty, orient='index').value_counts()
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
            asCountyCountName[index] = MImports1m.country[asCountyCountName[index][0]]
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
    put_html("<hr>")