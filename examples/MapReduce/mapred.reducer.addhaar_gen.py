import sys
import logging

from util import reducer_logfile
logging.basicConfig(filename=reducer_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def reducer():

    aadhaar_generated = 0
    old_key = None

    #Cycle through the list of key-value pairs emitted
    #by your mapper, and print out each key once,
    #along with the total number of Aadhaar generated,
    #separated by a tab.  Assume that the list of key-
    #value pairs will be ordered by key.  Make sure
    #each key-value pair is formatted correctly!
    #Here's a sample final key-value pair: "Gujarat\t5.0"

    #Since you are printing the actual output of your program, you
    #can't print a debug statement without breaking the grader.
    #Instead, you should use the logging module, which we've configured
    #to log to a file which will be printed when you hit "Test Run".
    #For example:
    #logging.info("My debugging message")

    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data)!=2:
            continue
            
        this_key, count = data
        if old_key and old_key!=this_key:
            print ("{0}\t{1}".format(old_key, aadhaar_generated))
            aadhaar_generated = 0
            
        old_key = this_key
        aadhaar_generated += float(count)
        
        if old_key != None:
            print ("{0}\t{1}".format(old_key, aadhaar_generated))
reducer()

