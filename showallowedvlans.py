#!/bin/env python
import cisco
import sys

ifNames = sys.argv[1]

if ifNames == "--help":
  print "Use as: python showallowedvlans.py Eth100/1/1,Eth110/1/1"
  print "Where Eth100/1/1,Eth110/1/1 Your interested interfaces full name"
  print "Please enter interface name as showed in sh vlan output? Eth, Po e.t.c...."
else:
  ifn = ifNames.split(",")

  for intname in ifn:
    clicmd = "show int "+ intname +" switchport | inc \"Trunking VLANs Allowed\""
    output = cisco.CLI(clicmd, 0).get_output()
    print "interface ",intname," ",output[0]