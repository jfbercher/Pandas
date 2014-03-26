import sys
import string
import logging

from util import mapper_logfile
logging.basicConfig(filename=mapper_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def mapper():
    '''
    In this exercise, we want to sum up all the values in the ENTRIEsn_hourly column in the
    turnstile_weather.csv. You can check out the csv file and its structure below:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv

    Each line of input will look like a row from our final Subway-MTA dataset, in csv format.

    This mapper should
    1) return 0 as the key and
    2) the number in the ENTRIEsn_hourly column as the value
    3)  The key and the count should be separated by a tab
        for example: 0\t12345

    Example output to the reducer would look like this:
    0   10501050105010.0

    Since you are printing the actual output of your program, you
    can't print a debug statement without breaking the grader.
    Instead, you should use the logging module, which we've configured
    to log to a file which will be printed when you hit "Test Run".
    For example:
    logging.info("My debugging message")
    '''
    for line in sys.stdin:
        data = line.strip().split(" ")
        print(data)
    	#print("{0}\t{1}".format(0, ))

mapper()

