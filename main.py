#!/usr/bin/env python3.5
import json
import logging
import os
import random
import sys

import coloredlogs
import requests


API_URL = 'https://api.stockfighter.io'


logger = logging.getLogger(__name__)


def main():
  key = os.environ['STOCKFIGHTER_API_KEY']
  auth_headers = {'X-Starfighter-Authorization': key}

  assert requests.get(
    API_URL + '/ob/api/heartbeat',
    headers=auth_headers,
  ).json()['ok'] == True, "API is down"

  venues_data = requests.get(
    API_URL + '/ob/api/venues',
    headers=auth_headers,
  ).json()

  venue = random.choice(
    [v['venue'] for v in venues_data['venues'] if v['state'] ==  'open'])

  logger.info("Randomly chose venue %r.", venue)

  assert requests.get(
    API_URL + '/ob/api/venues/' + venue + '/heartbeat' ,
    headers=auth_headers,
  ).json()['ok'] == True, "Venue is down"

  stocks = requests.get(
    API_URL + '/ob/api/venues/' + venue + '/stocks' ,
    headers=auth_headers,
  ).json()['symbols']

  logger.info("Stocks on %s exchange: %s", venue, ", ".join(
    ('%(symbol)s (%(name)s)' % s) for s in stocks))


if __name__ == '__main__':
  coloredlogs.install(
    level=logging.DEBUG,
    fmt='%(asctime)s %(name)s[%(process)d] %(levelname)s %(message)s',)
  sys.exit(main(*sys.argv[1:]))
