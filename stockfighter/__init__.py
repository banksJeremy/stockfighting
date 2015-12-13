import logging
import os
import random

import requests


API_URL = 'https://api.stockfighter.io'


logger = logging.getLogger(__name__)


class Stockfighter(object):
    def __init__(self, key):
        assert isinstance(key, str)
        self._key = key

    def request(self, path, post_data=None):
        assert post_data is None, 'not implemented'
        response = requests.get(
            API_URL + '/' + path,
            headers={'X-Starfighter-Authorization': self._key},
        )
        logger.debug('Got response for %r: %r', path, response)
        response_data = response.json()
        return response_data
