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
    client = stockfighter.Client(key=key)
    
    assert client.heartbeat(), "API is down"

    venues = client.venues()

    venue = random.choice([v for v in venues if v.state ==  'open'])

    logger.info("Randomly chose venue %r.", venue)

    assert venue.heartbeat(), "Venue is down"

    symbols = venue.symbols()

    logger.info("Stocks on %s exchange: %s", venue, symbols)

    symbol = random.choice(symbols)

    orders_data = symbol.orders_data()

    pp(orders_data)


if __name__ == '__main__':
    coloredlogs.install(
        level=logging.DEBUG,
        fmt='%(asctime)s %(name)s[%(process)d] %(levelname)s %(message)s',)
    sys.exit(main(*sys.argv[1:]))
