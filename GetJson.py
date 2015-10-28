#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib2,json
def get_json_array(num, Json_String, v1):
  try:
    test_data = eval(Json_String)
    data_string = json.dumps(test_data, sort_keys=True, indent=2)
    decoded = json.loads(data_string)
    return decoded[num][v1]
  except:
    return None

def get_json(Json_String,v1):
  try:
    test_data = eval(Json_String)
    data_string = json.dumps(test_data, sort_keys=True, indent=2)
    decoded = json.loads(data_string)
    return decoded[v1]
  except:
    return None
def get_json_url_array(num,url,v1):
#  print url
  try:
    url = url.encode('UTF-8')
    testdata = eval(urllib2.urlopen(url).read())
    data_string = json.dumps(testdata, sort_keys=True, indent=2)
    decoded = json.loads(data_string)
    return decoded[num][v1]
  except:
    return None

def get_json_url(url,v1):
#  print url
  try:
    url = url.encode('UTF-8')
    testdata = eval(urllib2.urlopen(url, timeout=1).read())
    data_string = json.dumps(testdata, sort_keys=True, indent=2)
    decoded = json.loads(data_string)
    return decoded[v1]
  except:
    return None


