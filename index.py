import os

from flask import Flask, json
from pywebio.platform.flask import webio_view
from werkzeug.exceptions import HTTPException

from MPage import IndexUI, TenThousandUI, OneMillionUI, GeoIPUI, AsnUI, DomainUI, CnGeoIPUI, GetUI

app = Flask(__name__)

app.add_url_rule('/', 'index', webio_view(IndexUI.index),
                 methods=['GET', 'POST', 'OPTIONS'])

app.add_url_rule('/get', 'get', webio_view(GetUI.index),
                 methods=['GET', 'POST', 'OPTIONS'])

app.add_url_rule('/ip', 'ip', webio_view(GeoIPUI.app),
                 methods=['GET', 'POST', 'OPTIONS'])

app.add_url_rule('/cn-ip', 'cn-ip', webio_view(CnGeoIPUI.app),
                 methods=['GET', 'POST', 'OPTIONS'])

app.add_url_rule('/asn', 'asn', webio_view(AsnUI.app),
                 methods=['GET', 'POST', 'OPTIONS'])

app.add_url_rule('/domain', 'domain', webio_view(DomainUI.app),
                 methods=['GET', 'POST', 'OPTIONS'])

app.add_url_rule('/1k', '1k', webio_view(TenThousandUI.app),
                 methods=['GET', 'POST', 'OPTIONS'])

app.add_url_rule('/1m', '1m', webio_view(OneMillionUI.app),
                 methods=['GET', 'POST', 'OPTIONS'])


@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


if __name__ == '__main__':
    print('Welcome to Eris.Report')
    HOST = os.environ.get('SERVER_HOST', '0.0.0.0')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '2025'))
    except ValueError:
        PORT = 2025

    app.run(HOST, PORT)
