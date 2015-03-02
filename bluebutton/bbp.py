#!/usr/bin/env python

# An Bluebutton parser command line utility.
# Alan Viars, Videntity 2011

import os, sys
#from bluebutton.parse import *
from parse import *

if __name__ == "__main__":
    """
    Accept a singe VA bluebutton file and convert it into json.  Return the
    whole parsed file (all), or just a subset (i.e. bp)
    """
    try:
        outtype=sys.argv[1]
        infile=sys.argv[2]
        outfile=sys.argv[3]
        if(len(sys.argv)==5):
            level=int(sys.argv[4])
    except(IndexError):
        print "You must supply an an infile and an outfile."
        print "Example: bbp.py [all|bp|wt|mds|green|segments] bluebutton_infile.txt bluebutton_outfile.json [level]"
        exit(1)

    try:
        items = simple_parse(infile)

        if outtype=="green":
            green_parse(infile, outfile, level)

        if outtype=="all":
            print tojson(items)

        if outtype=="bp":
            bpdictlist = build_bp_readings(items)
            print tojson(bpdictlist)

        if outtype=="wt":
            wtdictlist = build_wt_readings(items)
            print tojson(wtdictlist)

        if outtype=="mds":
            mdsdictlist = build_mds_readings(items)
            print tojson(mdsdictlist)

        if outtype=="d":
            demodict = build_simple_demographics_readings(items)
            print tojson(demodict)

        if outtype=="segments":
            demodict = section_parse(infile)
            #print tojson(demodict)
            result = write_file(demodict,outfile)


    except():
        print "An unexpected error occurred. Here is the post-mortem:"
        print sys.exc_info()