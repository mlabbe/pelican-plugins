'''
Copyright (C) 2013 Frogtoss Games, Inc.
http://www.frogtoss.com

RM Tempfiles
------------

Delete temp files from output directory.
'''

import os
import glob
import logging

from pelican import signals

logger = logging.getLogger(__name__)

# A list of temp file wildcards
TEMPFILES = [
    '*~',
    '\#*#',
]

def remove( delete_list ):
    for path in delete_list:
        logger.debug( 'Removing: %s' % path )
        os.remove( path )
        


def delete_tempfiles( pelican ):
    for dirpath, _, _ in os.walk( pelican.settings['OUTPUT_PATH'] ):
        for wildcard in TEMPFILES:
            globpath = dirpath + os.sep + wildcard
            delete_list = glob.glob( globpath )
            remove( delete_list )

def register():
    print "Hello"
    signals.finalized.connect(delete_tempfiles)
