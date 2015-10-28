#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import Adafruit_DHT
def Dome_1(pin):
  humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, pin)
  if humidity is not None and temperature is not None:
    return temperature, humidity
  else:
    return None, None
