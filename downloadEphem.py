# -*- coding: utf-8 -*-
"""

get list of stations 
wget ftp://geodesy.noaa.gov/cors/rinex/2010/365/ -q -O - | grep Directory | awk '{split($0,a,">"); split(a[2],b,"/");print b[1]}' >> cors.list
"""
# Example file
'ftp://geodesy.noaa.gov/cors/rinex/2010/002/brdc0020.10n.gz'
import os
for x in range(1,366):
    dayStr = str(x).zfill(3)
    wgetCmd = 'wget ftp://geodesy.noaa.gov/cors/rinex/2010/%s/brdc%s0.10n.gz' % (dayStr,dayStr)
    os.system(wgetCmd)
    eph = 'brdc%s0.10n.gz' % dayStr
    gzipCmd = 'gunzip %s' % eph
    os.system(gzipCmd)
