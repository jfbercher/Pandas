import sys
import logging

from util import reducer_logfile
logging.basicConfig(filename=reducer_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def reducer():
    '''
    Given the output of the mapper for this assignment, simply print
    0 and then the average number of riders per day for the month of 05/2011,
    separated by a tab.

    There are 31 days in 05/2011.

    Example output might look like this:
    0   10501050.0

    Since you are printing the actual output of your program, you
    can't print a debug statement without breaking the grader.
    Instead, you should use the logging module, which we've configured
    to log to a file which will be printed when you hit "Test Run".
    For example:
    logging.info("My debugging message")
    '''

    riders = 0
    old_key = None

    
    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data)!=2:
            continue
        this_key, ride_count = data
        if old_key and  (old_key != this_key):
            print ("{0}\t{1}".format(old_key, riders))
            riders = 0
        old_key = this_key
        riders += float(ride_count)
    if old_key != None:
        print("{0}\t{1}".format(old_key, riders/31.0))
        

reducer()

