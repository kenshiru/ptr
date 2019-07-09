import aiohttp_jinja2
from aiohttp import web


@aiohttp_jinja2.template('bin-info.jinja2')
async def show_bin_info_form(request: web.Request):
    """
    Show form has BIN input
    :param request: aiohttp request
    :return: ...
    :rtype: dict
    """
    return {
        'error': None,
        'bin_info': None
    }
