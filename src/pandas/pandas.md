<h1>Pandas Learning Notes</h1>

- [Numpy Basics](#numpy-basics)
- [Series](#series)
- [DataFrame](#dataframe)
  - [DataFrame info](#dataframe-info)
  - [create csv file](#create-csv-file)
  - [read\_csv()](#read_csv)
- [Sales Analysis project](#sales-analysis-project)
- [References](#references)
- [Data Analysis for Excel Users](#data-analysis-for-excel-users)

## Numpy Basics
[Numpy basics](../numpy/numpy.md)

## Series

```
class pandas.Series(data=None, index=None, dtype=None, name=None, copy=None, fastpath=False)
```
* [create a Series object from dict](createSeries01.py)
* []()



## DataFrame
DataFrame is a class defined in pandas module.

```
class pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=None)
```
* [Create DataFrame object from dict](create01.py)
* [Create DataFrame object from numpy array](create02.py)
* [Create DataFrame object from class](create03.py)
* [Create DataFrame object from Pandas Series](create04.py)
* [Create DataFrame object from existing DataFrame](create05.py)

* [pandas DataFrame basic](pandas.ipynb)
loc() syntax:
```
; return values
df.loc[index, column] 
```
### DataFrame info

### create csv file
* [create csv file from user inpput](createCSV.py)
* 
### read_csv()

* [simple curves](dataanalysis01.py)
* [Covid-19](dataanalysis02.py)
* [Create a instance of DataFrame](../src/pandas/pandas01.py)
  
## Sales Analysis project
* 👍😄[complete analysis code](SalesAnalysis.ipynb)
* 
## References
[Document website](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
[YouTube Onlinw](https://www.youtube.com/watch?v=PXMJ6FS7llk)
[Solving real world data science tasks with Python Pandas](https://www.youtube.com/watch?v=eMOA1pPVUc4)

## Data Analysis for Excel Users
* [Anaconda3](https://repo.anaconda.com/archive/) 
  👎😢File: Anaconda3-5.3.0-Windows-x86_64.exe
