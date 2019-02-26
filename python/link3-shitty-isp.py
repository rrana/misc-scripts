#!/usr/bin/env python

import subprocess


def evaluate_results(ping_value, download_speed, upload_speed):
    if ping_value > 200:
        print "High ping (%s ms) towards US routes!" % ping_value
    else:
        print "Ping (%s ms) value looks good so far!" % ping_value

    if download_speed < 10:
        print "Bad download speed. Only %s Mbit/s." % download_speed
    elif upload_speed < 5:
        print "Bad upload speed. Only %s Mbit/s." % upload_speed
    else:
        print "Speed seems acceptable. Download %s Mbit/s and Upload %s Mbit/s" % (download_speed, upload_speed)


def run_speedtest():
    speedtest_command = '/home/ubuntu/python-env/configuration-management/bin/speedtest-cli --server 911 --simple'
    ping, download, upload, _ = subprocess.Popen(speedtest_command,
                                                             shell=True,
                                                             stdout=subprocess.PIPE
                                                 ).stdout.read().split('\n')
    ping_value = int(float(ping.split(' ')[1]))
    download_speed = int(float(download.split(' ')[1]))
    upload_speed = int(float(upload.split(' ')[1]))
    evaluate_results(ping_value, download_speed, upload_speed)


if __name__ == '__main__':
    run_speedtest()
