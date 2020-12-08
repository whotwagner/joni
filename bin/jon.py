#!/usr/bin/env python3

import sys
from joni import joni
import argparse

parser = argparse.ArgumentParser(description='Joni Joni, Yes Papa...')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--list', help="List music-database",action='store_true')
group.add_argument('--start',type=str, help="Runs a playlist")
group.add_argument('--stop', help="Stops the player",action='store_true')
args = parser.parse_args()

print(vars(args))

if args.start and args.stop:
    print("Error: use only one of '--start ID' or '--stop'")
    sys.exit(1)


yespapa = joni.Joni("docs/config.yml")

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

