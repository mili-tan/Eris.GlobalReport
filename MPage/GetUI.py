import socket

import geoip2
import geoip2.database
import ipdb
import pandas as pd
from pywebio.output import *

import MContext


def index():
    """Index | Eris.Report"""

    clear()
    put_html(MContext.nav)
    with use_scope('scope1'):
        put_button("获取数据", onclick=getList, color='success', outline=True)


def getList():
    toast("正在获取数据，请稍等……")
    clear("scope1")
    with use_scope('scope2'):
        data = pd.read_csv(
            'https://ghproxy.com/raw.githubusercontent.com/NovaXNS/popularity/master/result/result-10k.csv',
            header=None).head(50)
        put_html(data.to_html(border=0, index=False, header=False))
    toast("完成！")

    with use_scope('scope1'):
        put_button("获取 IP 数据", onclick=getIps, color='success', outline=True)


def getIps():
    toast("正在获取IP数据，请稍等……")
    clear("scope2")
    clear("scope1")
    data = pd.read_csv('https://ghproxy.com/raw.githubusercontent.com/NovaXNS/popularity/master/result/result-10k.csv',
                       header=None).head(50)
    list = []
    cityReader = geoip2.database.Reader('GeoLite2-City.mmdb')
    asnReader = geoip2.database.Reader('GeoLite2-ASN.mmdb')
    db = ipdb.City("ipipfree.ipdb")

    for index, row in data.iterrows():
        try:
            ip = socket.gethostbyname(row[1])
            r = cityReader.city(ip)
            n = asnReader.asn(ip)
            row[-1] = ip
            list.append("<tr>"
                        "<td>" + str(row[0]) + "</td>"
                                               "<td>" + str(row[1]) + "</td>"
                                                                      "<td>" + str(ip) + "</td>"
                                                                      "<td>" + str(n.autonomous_system_number) + "</td>"
                                                                      "<td class=""small"">" + n.autonomous_system_organization + "</td>"
                                                                      "<td>" + r.country.iso_code + "</td>"
                                                                      "<td>" + str(db.find_info(addr=str(ip), language="CN").city_name) + "</td>"
                                                                                         "</tr>")
            with use_scope("scope2"):
                clear("scope2")
                put_html(
                    " <table> " + str.join(" ", list) + " </table> "
                )
        except Exception as e:
            toast(str(e))
    toast("完成！")
