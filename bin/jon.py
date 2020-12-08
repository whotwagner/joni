#!/usr/bin/env python3

import sys
from joni import joni
import argparse
import logging

loglevel = logging.INFO

parser = argparse.ArgumentParser(description='Joni Joni, Yes Papa...')
parser.add_argument('-c','--cfgfile',type=str, help="Set config file",default="docs/config.yml")
parser.add_argument('-L','--logfile',type=str, help="Set logfile")
parser.add_argument('-d','--debug',action='store_true', help="Enable debugging(verbose logfile)")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--list', help="List music-database",action='store_true')
group.add_argument('--start',type=str, help="Runs a playlist")
group.add_argument('--stop', help="Stops the player",action='store_true')
args = parser.parse_args()

if args.start and args.stop:
    print("Error: use only one of '--start ID' or '--stop'")
    sys.exit(1)

if args.debug:
    loglevel = logging.DEBUG

if args.logfile:
    logging.basicConfig(filename=args.logfile,  level=loglevel)

yespapa = joni.Joni(args.cfgfile)

if args.start:
    yespapa.start(args.start)
elif args.stop:
    yespapa.stop()
elif args.list:
    yespapa.list()
else:
    print("Error: use either '--start ID' or '--stop'")
    sys.exit(1)

sys.exit(0)
