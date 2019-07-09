from aiohttp import web
import aiohttp_jinja2
import jinja2
import logging
from router import routes

logging.basicConfig(level=logging.INFO)

app = web.Application()
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('./src/templates'))

app.add_routes(routes)

web.run_app(app)
