#!/usr/bin/env python3
import sys
import logging

#logging.basicConfig(filename='/tmp/peripage.log', level=logging.DEBUG)

#logging.debug('called peripage filter')


def save_test_data(rdata):
    if not rdata:
        raise ValueError('No data received')
    
    f = open('/tmp/test_data.raster', 'wb')
    f.write(rdata)
    f.close()


    return True

pages = save_test_data(sys.stdin.buffer.read())