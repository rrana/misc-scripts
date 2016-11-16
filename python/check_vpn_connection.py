# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#!/usr/bin/python

# Run this with sudo privilege/as root. Otherwise refactor the code.


import os
import time
import netifaces
from subprocess import call
import urllib


def start_openvpn():
    print "Starting openvpn service"
    call(["sudo", "service", "openvpn", "start"])
    time.sleep(10)

    if not vpc_reachable():
        # wait 5 more seconds
        time.sleep(5)
    else:
        return True


def vpc_reachable():
    jenkins_response = urllib.urlopen("https://jenkins.newscred.com/").getcode()
    
    if jenkins_response == 403:
        print "VPN connected, VPC is reachable!"
        return True
    else:
        print "Something went wrong!"
        return


def running_as_root():
    if not os.geteuid() == 0:
        print "Please run this script as root"        
        return False    
    else:
        return True


if __name__ == "__main__":

	if running_as_root(): 
    
	    vpn_interface_name = "tun0"
	    
	    # check is remote vpn server is up
	    vpn_server_response = urllib.urlopen("https://vpn.newscred.com/").getcode()

		# if remote server responds with 403 it's okay because it's up. TODO: improve this check
	    if vpn_server_response == 403:
		    try:
		        netifaces.ifaddresses(vpn_interface_name)

		    except ValueError:
		        start_openvpn()
		    
		    else:
		    	jenkins_response = urllib.urlopen("https://jenkins.newscred.com/").getcode()
		    	if jenkins_response == 403:
		    		print "VPN connected, VPC is reachable!"
		    	else:
		    		print "Something went wrong! Internal service is not reachable."
