import sys
import string
import logging

from util import mapper_logfile
logging.basicConfig(filename=mapper_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def mapper():
    """
    The input to this mapper will be the final Subway-MTA dataset, the same as
    in the previous exercise.  You can check out the csv and its structure below:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv

    For each line of input, the mapper output should
    1) return the UNIT as the key
    2) return the number of ENTRIESn_hourly as the value
    3) Separate the key and the value by a tab, for example:
       R002\t105105.0

    Since you are printing the actual output of your program, you
    can't print a debug statement without breaking the grader.
    Instead, you should use the logging module, which we've configured
    to log to a file which will be printed when you hit "Test Run".
    For example:
    logging.info("My debugging message")
    """

    n=0
    for line in sys.stdin:
        if n==0:
            n=1
            continue
        data = line.strip().split(",")
        print("{0}\t{1}".format(data[1], data[6]))


mapper()

