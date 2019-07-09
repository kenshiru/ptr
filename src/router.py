from aiohttp import web
import methods

routes = [
    web.get('/', methods.show_bin_info_form),
    web.post('/', methods.show_bin_info)
]
