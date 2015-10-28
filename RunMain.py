#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import DemoSensor
import GetDevid
import GetJson
import urllib

def main():
  Devid = GetDevid.get_processor_name()
  if Devid == None:
    sys.exit(1)
  passwd = None
  mod = None
  retime = None
  senName = ""
  command = None
  i = 1
  while i<len(sys.argv)-1:
    if sys.argv[i] == "-m":
      if sys.argv[i + 1].find("-") != 0:
        mod = sys.argv[i+1]
      else:
        print "in Error"
        sys.exit(1)
    
    if sys.argv[i] == "-com":
      if sys.argv[i + 1].find("-") != 0:
        command = sys.argv[i+1]
      else:
        print "in Error"
        sys.exit(1)

    if sys.argv[i] == "-t":
      if sys.argv[i + 1].find("-") != 0:
        try:
          retime = int(sys.argv[i+1])
        except:
          print "in Error"
          sys.exit(1)
      else:
        print "in Error"
        sys.exit(1)

    if sys.argv[i] == "-SenName":
      if sys.argv[i + 1].find("-") == 0:
        print "in Error"
        sys.exit(1)
      while i<len(sys.argv)-1 and sys.argv[i + 1].find("-") != 0:
        i += 1
        if senName == "":
          senName += sys.argv[i]
        else:
          senName += "!@!" + sys.argv[i]

    i += 1
  #print passwd
  if retime == None:
    retime = 30
  if mod == None or mod == "down":
    url = "http://php-easyhome.rhcloud.com/gitphp/register.php?devid=%devid"
    url = url.replace("%devid",Devid)
    if senName == "":
      url = url + "&value_name=Temp!@!Humidity" 
    else:
      url = url + "&value_name=" + senName
    url = url + "&command=on"
    if "OK" == GetJson.get_json_url(url,"con"):
      DemoSensor.Demo(Devid,retime)
    else:
      print "register Error"
      sys.exit(1)
  if mod == "DHT22":
    print "test_DHT22"

if __name__ == "__main__":
  main()
