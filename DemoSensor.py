#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import DHT22
import time
import GetJson
import thread
import Command
def read_sw(devid,retime):
  start_url = "http://php-easyhome.rhcloud.com/gitphp/devindata.php?devid=@devid&devtime=@devtime&values=@values"
  print "Devid Name:%s"%devid
  
  while True:
    timemas = int(time.strftime('%S',time.localtime(time.time())))
    devtime = time.strftime('%Y-%m-%d%%20%H:%M:%S',time.localtime(time.time()))
    devtime2 = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    while timemas % retime != 0 :
      timemas = int(time.strftime('%S',time.localtime(time.time())))
      devtime = time.strftime('%Y-%m-%d%%20%H:%M:%S',time.localtime(time.time()))
      devtime2 = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
      time.sleep(0.2)
    tStart = time.time()
    hum, tem = DHT22.Dome_1(4)
    sensor_string = "{0:0.1f}!@!{1:0.1f}".format(hum,tem)    
    url = start_url.replace("@devid",devid)
    url = url.replace("@devtime",devtime)
    url = url.replace("@values",sensor_string)
    thread.start_new_thread(GetJson.get_json_url,(url,"con"))

    
    tStop = time.time()
    print "Execution time:%s"%devtime2
    print "Waiting time:%f s"%(tStop - tStart)
    print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(hum,tem)
    time.sleep(1)

def command_sw(devid):
  command_url = "http://php-easyhome.rhcloud.com/gitphp/showcomdata.php?devid=@devid".replace("@devid",devid)
  command_start = ""
  while True:
    command_re = GetJson.get_json_url_array(0,command_url,"com")
    #print command_re
    if None == command_re:
      sys.exit(1)
    else:
      if command_start != command_re:
        command_start = command_re
        if command_start == "on":
          Command.blink(8,True)
        else:
          Command.blink(8,False)
        time.sleep(1)
    time.sleep(0.5)



def Demo(devid,retime):
  devid1 = devid
  thread.start_new_thread(read_sw,(devid,retime,))
  thread.start_new_thread(command_sw,(devid1,))
  while True:
    pass


