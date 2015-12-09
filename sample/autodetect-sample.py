#!/usr/bin/env python

# I2C implementation of ADXL345 expect two parameters: alternate and port
# This sample tries to autodetect these parameters

import sys
import os
from adxl345.i2c import ADXL345

def main():
  # Find all available I2C devices
  i2c_devs = [int(d[-1]) for d in os.listdir("/dev/") if "i2c-" in d]

  if len(i2c_devs) == 0:
    print("No I2C device detected. Try modprobe i2c-dev")
    return
  else:
    print("I2C available devices: " + str(i2c_devs))

  for port in i2c_devs:
    for alternate in [ False, True ]:
      sys.stdout.write("Trying port " + str(port) + " with alternate=" + str(alternate) + "... ")
      try:
        adxl = ADXL345(alternate=alternate, port=port)
        deviceId = adxl.get_device_id()
        print("success (id=" + str(deviceId) + ")")
      except:
        print("failure")

main()
