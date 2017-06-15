# Bitcoin annual returns
This simple Python script shows the annual bitcoin price performance (yearly percentage change). 

The average price is determined each year. 
For the performance the average price of the current year is divided by the average price of the last year.
The last row shows the average percentage change per year (performance).

`python annulize_price.py` at 15 June 2017
Output:
```
** Bitcoin yearly performance **
year .. price end of year .. avg for year .. performance
2010    0.299999              0.167    0.0
2011    4.995000              6.054    35.242
2012    13.590000              8.472    0.399
2013    739.100000              188.786    21.284
2014    317.400000              525.33    1.783
2015    428.000000              271.828    -0.483
2016    952.156375              566.383    1.084
2017    2447.041563              1363.88    1.408
total days:  1247
first day:  2010-08-18
last day:  2017-06-14
average return per year:  867.38575 %
``


For a local copy: `git clone https://github.com/PlagScanian/bitcoin-annual-returns.git`

Daniel Gockel © daniel@gockel.co