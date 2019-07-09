import aiohttp_jinja2
import logging
from aiohttp import web
from multidict import MultiDictProxy
from lib.bin_list_sdk import BinListSDK


def get_card_bin_from_request(request_params: MultiDictProxy) -> int:
    """
    Get BIN from request params
    :param request_params: parsed request body
    :type request_params: MultiDictProxy
    :return: card BIN
    :rtype int
    """
    card_bin = request_params.get('bin')
    try:
        return int(card_bin)
    except ValueError:
        raise ValueError('Invalid card BIN')


async def get_request_params(request: web.Request) -> MultiDictProxy:
    """
    Get parsed request body
    :param request: aiohttp request
    :type request: web.Request
    :return: parsed body
    :rtype MultiDictProxy
    """
    request_params = await request.post()

    if type(request_params) is not MultiDictProxy:
        raise Exception('Unexpected type of request params')

    return request_params


@aiohttp_jinja2.template('bin-info.jinja2')
async def show_bin_info(request: web.Request):
    """
    Handler for / POST request. Using for search card info using BIN
    :param request: aiohttp request
    :type request: web.Request
    :return: params for template
    :rtype dict
    """
    request_params = await get_request_params(request)

    try:
        card_bin = get_card_bin_from_request(request_params)

        bin_sdk = BinListSDK()
        bin_info = await bin_sdk.get_bin_info(int(card_bin))
        logging.info('BIN=%s was found: %s' % (card_bin, bin_info))

        return {
            'error': False,
            'bin_info': bin_info,
            'card_bin': card_bin
        }

    except Exception as error:
        return {
            'error': error,
            'bin_info': None,
            'card_bin': None
        }
