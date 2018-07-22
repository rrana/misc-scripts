#!/usr/bin/env python

import sys
from urllib2 import urlopen


dhaka_office_general_public_ip = '103.248.13.242'
my_office_public_ip = '163.53.149.174'

def get_my_public_ip():
    my_ip = urlopen('http://ip.42.pl/raw').read()
    if my_ip == dhaka_office_general_public_ip:
    	print "Your public IP is: %s, and it's the office general public IP" % my_ip
    	sys.exit(0)
    if my_ip == my_office_public_ip:
    	print "Your public IP is: %s, and it's your own office public IP. BEAWARE when using it" % my_ip
    	sys.exit(0)
    else:
    	print "Your public IP is: %s. and it's not a regular IP that we know!" % my_ip
    	sys.exit(0)


if __name__ == '__main__':
    get_my_public_ip()

