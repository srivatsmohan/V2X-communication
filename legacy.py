#!/bin/python

import subprocess
import time

def wrapper():
    print echo
def get_wlan_data():

    reg_data = subprocess.Popen(['iwconfig', 'wlan0'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    wlan_info = reg_data.communicate()[0]

    if "Access Point" in wlan_info.split('\n')[1] and "Signal level" in wlan_info.split('\n')[6]:
        cur_ap =str(wlan_info.split('\n')[1].split('Access Point: ')[1].split(' ')[0])
        cur_rssi =str(wlan_info.split('\n')[6].split('Signal level=')[1].split(' ')[0])

	if "18:D6:C7:51:BE:24"in cur_ap:
	    cur_ap1='Garden\t'+cur_rssi
	    cur_ap='\033[31m'+'Garden\t\t'+cur_rssi+'\033[37m'
        if "84:16:F9:9B:CE:46"in cur_ap:
	    cur_ap1='SP_building\t'+cur_rssi
            cur_ap='\033[34m'+'SP_building\t\t'+cur_rssi+'\033[37m'
	if "D4:6E:0E:F5:CF:2C"in cur_ap:
	    cur_ap1='ECE_building\t'+cur_rssi
	    cur_ap='\033[32m'+'ECE_building\t\t'+cur_rssi+'\033[37m'
    else:
	print 'wlan data not available'

    return cur_ap,cur_ap1

def get_ping():

    ping = subprocess.Popen(['ping', '-c','4', '192.168.0.1','-i','.20'],stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    ping_data = str(ping.communicate()[0].split('\n')[1].split("time=")[1].split(' ')[0])
    return ping_data

while True:
    cur_ap,cur_ap1= get_wlan_data()
    ping = get_ping()
    data= cur_ap+'\t'+ping
    data1=cur_ap1+'\t'+ping
    print data
    with open("legacy.csv",'a+') as f:
        f.writelines(data1)
        f.writelines('\n')
    f.close()
