Pandas
======

An R-like package for data analysis in python


```
sudo apt-get install python-pandas
```

<p>Example:</p>

```
import pandas as ps
d = {'one': ps.Series([1,2,3], index=['a', 'b', 'c']),
     'two': ps.Series([1,2,3,4], index=['a', 'b', 'c'])}

df = ps.DataFrame(d)

import numpy
df.apply(numpy.mean)

df['one'].map(lambda x: x>=1)

df.applymap(lambda x: x>=1)
```   

To read/write in CSV data:
```
import pandas
df = pandas.read_csv("datafile.csv")
df.to_csv("outpout.csv")
```


<p> <B> pandas + SQL </b> </p>
```
import pandas
import pandasql
df = pandas.read_csv('file.csv')
df.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)
dsel = pandasql.sqldf('SELECT * FROM df LIMIT 20')
```
