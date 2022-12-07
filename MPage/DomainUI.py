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
    tldValue20 = MImports10k.tlds.value_counts().head(20).values.tolist()
    tldName20 = MImports10k.tlds.value_counts().head(20).keys().tolist()

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

    tldCountryValue = MImports10k.tlds.map(MImports10k.country).value_counts().values.tolist()
    tldCountryName = MImports10k.tlds.map(MImports10k.country).value_counts().keys().tolist()

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
            visualmap_opts=opts.VisualMapOpts(max_=500),
        )
    )

    pywebio.output.put_html(tldCountryChart1.render_notebook())
    put_html("<hr>")

    put_html("<h1>前一百万</h1>")
    tldValue20 = MImports1m.tlds.value_counts().head(20).values.tolist()
    tldName20 = MImports1m.tlds.value_counts().head(20).keys().tolist()

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

    tldCountryValue = MImports1m.tlds.map(MImports1m.country).value_counts().values.tolist()
    tldCountryName = MImports1m.tlds.map(MImports1m.country).value_counts().keys().tolist()

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
    put_html("<hr>")
