#!/usr/bin/env python3

import logging
import random
import time

while True:

    number = random.randrange(0, 4)

    if number == 0:
        logging.info('Hello there!!')
    elif number == 1:
        logging.warning('What a.... something strange')
    elif number == 2:
        logging.error('OMG!!!!!!')
    elif number == 3:
        logging.exception(Exception('this is exception'))

    time.sleep(1)
