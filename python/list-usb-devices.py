#!/usr/bin/env python

import re
import subprocess
import json


def list_usb_devices():
	device_re = re.compile("Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
	df = subprocess.check_output("lsusb")
	devices = []
	for i in df.split('\n'):
	    if i:
	        info = device_re.match(i)
	        if info:
	            dinfo = info.groupdict()
	            dinfo['device'] = '/dev/bus/usb/%s/%s' % (dinfo.pop('bus'), dinfo.pop('device'))
	            devices.append(dinfo)
	print json.dumps(devices, indent=4, sort_keys=True)


if __name__ == '__main__':
	list_usb_devices()
