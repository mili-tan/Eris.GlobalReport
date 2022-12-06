from pywebio.output import *

import MContext


def index():
    """Index | Eris.Report"""

    clear()
    put_html(MContext.nav)
    put_html(MContext.card)