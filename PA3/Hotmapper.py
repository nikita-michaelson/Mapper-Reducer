#!/usr/bin/env python

from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)

import sys

#get the input from standard input
for theInput in sys.stdin:
        #clean up whitespace
        theInput = theInput.strip()
        #split input by columns
        array = theInput.split(',')
        array = [index.strip() for index in array]
        #extract the information
        if array:
            print "timeofday:", array[1], "systemID:", array[4], "actualTemp:", array[3]
                                        
