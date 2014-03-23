
import sys
import string

def mapper():
   for line in sys.stdin:
     
     data = line.strip().split(" ")
     for w in data:
        # clean the data
        w_clean = w.translate(string.maketrans("", ""), string.punctuation).lower()
        # emit a key-value pair
        print ("{k}\t{v}".format(k=w_clean, v=1))

mapper()
