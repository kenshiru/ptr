import aiohttp


class BinListNotFoundException(Exception):
    pass


class BinListBadRequest(Exception):
    pass


class BinListSDK:
    STATIC_HEADERS = {
        'Accept-Version': '3'
    }

    def __init__(self, base_url:str='https://lookup.binlist.net'):
        self._base_url = base_url

    async def get_bin_info(self, card_bin: int) -> dict:
        url = '%s/%s' % (self._base_url, card_bin)

        print(url)
        async with aiohttp.ClientSession() as client:
            async with client.get(url=url, headers=self.STATIC_HEADERS) as resp:
                if resp.status == 400:
                    raise BinListBadRequest('Trouble in request')
                elif resp.status == 404:
                    raise BinListNotFoundException('BIN info not found')

                return await resp.json(encoding='utf8')
