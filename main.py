#!/usr/bin/env python3.5
import logging
import os
import random
import sys

import coloredlogs
import pp

import stockfighter


logger = logging.getLogger(__name__)


def main():
    key = os.environ['STOCKFIGHTER_API_KEY']
    api = stockfighter.Stockfighter(key=key)
    
    assert api.request('/ob/api/heartbeat')['ok'] == True, "API is down"

    venues_data = api.request('ob/api/venues')

    venue = random.choice(
        [v['venue'] for v in venues_data['venues'] if v['state'] ==  'open'])

    logger.info("Randomly chose venue %r.", venue)

    assert api.request('ob/api/venues/%s/heartbeat' % (venue))['ok'] == True, "Venue is down"

    symbols = api.request('ob/api/venues/%s/stocks' % (venue))['symbols']

    logger.info("Stocks on %s exchange: %s", venue, ", ".join(
        ('%(symbol)s (%(name)s)' % s) for s in symbols))

    symbol = random.choice([s['symbol'] for s in symbols])

    orders_data = api.request('ob/api/venues/%s/stocks/%s' % (venue, symbol))

    pp(orders_data)


if __name__ == '__main__':
    coloredlogs.install(
        level=logging.DEBUG,
        fmt='%(asctime)s %(name)s[%(process)d] %(levelname)s %(message)s',)
    sys.exit(main(*sys.argv[1:]))
