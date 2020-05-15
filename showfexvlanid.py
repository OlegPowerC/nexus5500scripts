#!/bin/env python
import cisco
import sys

ifNames = sys.argv[1] 

if ifNames == "--help":
  print "Use as: python showfexvlanid.py Eth100/1,Eth110/1 10"
  print "Where Eth100/1,Eth110/1 Your interested FEXs and 10 is VLAN ID"
  print "Please enter interface name as showed in sh vlan output? Eth, Po e.t.c...."
else:
  vlanid = sys.argv[2]
  ifn = ifNames.split(",")
  print "VLAN ID ",vlanid,"allowed on interfaces:"
  for intname in ifn:
    clicmd = "show vlan id "+ vlanid + " | inc \"" + intname + "\""
    output = cisco.CLI(clicmd, 0).get_output()
    for str1 in output:
      str2 = str1.strip()
      str3 = str2.split(",")
      for str4 in str3:
        str5 = str4.strip()
        if str5.find(intname) != -1:
          print str5