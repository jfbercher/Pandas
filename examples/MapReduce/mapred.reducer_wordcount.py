import sys

def reducer():
   
   word_count = 0
   old_key = None

   for line in sys.stdin:
      data = line.strip().split("\t")
      #print(data)

      if len(data) != 2:
         continue

      this_key, count = data

      if old_key and old_key != this_key:
         print("{k}\t{v}".format(k=old_key, v=word_count))
         word_count = 0

      old_key = this_key
      word_count += float(count)

      if old_key != None:
          print("{k}\t{v}".format(k=old_key, v=word_count))


reducer()
