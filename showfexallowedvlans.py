#!/bin/env python
import cisco
import sys

ifNames = sys.argv[1]

if ifNames == "--help":
  print "Use as: python showfexallowedvlans.py Eth100/1,Eth110/1 16"
  print "Where Eth100/1,Eth110/1 Your interested interfaces full name of part name and 16 - is maimum number of interface - for example Eth100/1/16"
  print "Please enter interface name as showed in sh vlan output? Eth, Po e.t.c...."
else:
  bCount = sys.argv[2]

  ifn = ifNames.split(",")

  for intindex in range(1,int(bCount)+1):
    for intname in ifn:
      intnamefull = intname+"/"+str(intindex)
      clicmd = "show int "+ intnamefull + " switchport | inc \"Trunking VLANs Allowed\""
      output = cisco.CLI(clicmd, 0).get_output()
      print "interface ",intnamefull," ",output[0]