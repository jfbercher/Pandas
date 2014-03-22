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
     'two': ps.Series([1,2,3,4], index=['a', 'b', 'c', 'd'])}

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

 Useful functions:
```
df.sum()  ==> Sum of each column, removes NAs by default
df.mean() 
df.dropna()  ! option: how='all'
df.fillna(val)
df.shift(1)  ==> shift some number of rows back/forth

time='08:23:45'
hour = pandas.to_datetime(time).hour
minute=pandas.to_datetime(time).minute
second=pandas.to_datetime(time).second

```

<p> <B> pandas + SQL </b> </p>
```
import pandas
import pandasql
df = pandas.read_csv('file.csv')
df.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)
dsel = pandasql.sqldf('SELECT * FROM df LIMIT 20')
```

Aggregate Query:
```
SELECT district,sum(aadhaar_generated) 
FROM aadhaar_data 
GROUP BY district;
```

JSON is similar to python dictionary, but not equivalent

To request data from API:
```
import json
import requests

if __name__ == "__main__":
   url = ''
   data = requests.get(url).text

   # next, convert text format data to python dictionary:
   data = json.loads(data)

   print type(data)
   print data

```

last.fm API: 
?methpd=..
?api_key=..

<p> Pandas describe function</p>

df.describe() ==> gives summary info for all columns
    info includes: count, mean, std, min, perc quantiles, max


<p> Dealing with missing values: </p>

<ol>
<li> partial deletion </li>
<li> imputation </li>
<ul>
<li> using mean </li>
<li> linear regression with other columns </li>
</ul>
</ol>

Two sample t-test:
t=(mu1 - mu2) / sqrt(var1/N1 + var2/N2)

nu = (var1/N1 + var2/N2) / (var1^2/(N1^2*nu1) + var2^2/(N2^2*nu2))

p-value: probablity of obtaiing a test statistic at <b>least</b> as
extreme as ours if null hypothesis was true

<b> Welch's t-test in Python: </b>
```
import scipy.stats
scipy.stats.ttest_ind(list1, list2, equal_var=False)

```
link: http://docs.scipy.org/doc/scipy/reference/stats.html

For a one-sided t-test:
symmetric distn.: one-sided p-value = half of 2-sided p-value

to check whether mu1 > mu2: p/2<p_critical, and t>0
and for mu1<m2: p/2 < p_critical, and t<0

<h4> Non Parametric u-test</h4>
A statistical test that does not assume our data is drawn from any particular probablity distn.

Mann-Whitney u-test: tests null hypothesis that two populations are the same

u,p = scipy.stats.Mannwhitneyu(X,Y)

<h4> Non-normal data </h4>
Shapiro-wilk test:
w,p = scipy.stats.shapiro(data)

<h4> Coefficient of Determination: R-Squared</h4>
R2 = 1 - Sum(yi-fi)^2 / Sum(yi - ymean)^2
