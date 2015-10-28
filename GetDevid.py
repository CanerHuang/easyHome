#!/usr/bin/python
import os, platform, subprocess, re



def get_processor_name():
  if platform.system() == "Windows":
    return platform.processor()
  elif platform.system() == "Darwin":
    os.environ['PATH'] = os.environ['PATH'] + os.pathsep + '/usr/sbin'
    command ="sysctl -n machdep.cpu.brand_string"
    return subprocess.check_output(command).strip()
  elif platform.system() == "Linux":
    command = "cat /proc/cpuinfo"
    all_info = subprocess.check_output(command, shell=True).strip()
    for line in all_info.split("\n"):
      if "Serial" in line:
        return re.sub( ".*Serial.*: ", "", line,1)
  return ""
