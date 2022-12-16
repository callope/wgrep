#!/usr/bin/env python
from parser import args
from saver import save

lnk = args.target
out = args.output
fmt = args.format

try:
    save(lnk, out, fmt)
except Exception as e: # print unhandled exceptions that can appear
    print(e)
