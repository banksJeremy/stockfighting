import abc
import logging
import os
import random

import requests


API_URL = 'https://api.stockfighter.io/ob/api/'


logger = logging.getLogger(__name__)

class Client(object):
    def __init__(self, key):
        assert isinstance(key, str)
        self._key = key

    def heartbeat(self):
        """Returns True iff we can get a heartbeat from the Stockfighter API.
        """
        try:
            assert self.request('heartbeat')['ok'] == True
            return True
        except Exception as ex:
            logger.info("Heartbeat failed: %r", ex)
            return False

    def venues(self):
        """Returns a list of Venue objects for all Venues.
        """
        return [
            Venue(self, data) for data in self.request('venues')['venues']
        ]


    def request(self, path, post_data=None):
        assert post_data is None, 'not implemented'
        response = requests.get(
            API_URL + '/' + path,
            headers={'X-Starfighter-Authorization': self._key},
        )
        logger.debug('Got response for %r: %r', path, response)
        response_data = response.json()
        return response_data


class ClientObject(object):
    def __init__(self, client, data=None):
        self._client = client
        self._data = data

    def _get_data_if_none(self):
        if self._data is None:
            self.update()

    def updated(self):
        self.update()
        return self
    
    def update(self):
        raise NotImplementedError("%r is not update()able" % self)

    def __repr__(self):
        return '%s(%s, data=%r)' % (self.__class__.__name__, self._client, self._data)


class Venue(ClientObject):
    @property
    def name(self):
        self._get_data_if_none()
        return self._data['venue']

    @property
    def state(self):
        self._get_data_if_none()
        return self._data['state']

    def heartbeat(self):
        """Returns True iff we can get a heartbeat for this Venue.
        """
        try:
            assert self._client.request('venues/%s/heartbeat' % (self.name))['ok'] == True
            return True
        except Exception as ex:
            logger.info("Heartbeat failed: %r", ex)
            return False

    def symbols(self):
        """Returns a list of Venue objects for all Venues.
        """
        return [
            VenueStock(self._client, data, self) for data in
            self._client.request('venues/%s/stocks' % (self.name))['symbols']
        ]


class VenueStock(ClientObject):
    def __init__(self, client, data=None, venue=None):
        assert venue is not None
        super().__init__(client, data=data)
        self._venue = venue

    @property
    def symbol(self):
        self._get_data_if_none()
        return self._data['symbol']

    def orders_data(self):
        return self._client.request(
            'venues/%s/stocks/%s' % (self._venue.name, self.symbol))

