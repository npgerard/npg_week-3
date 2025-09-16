# necessary imports
import seaborn as sns
import pandas as pd
import numpy as np



# update/add code below ...
print("apputil.py loaded")

# exercise 1: Fibonacci function
# the following 2 lines are an optimization for the Fibonacci function
from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n):
    '''returns the fibonacci number at position n'''
    # if n is 0 or 1, return n because there is no sequence to add
    if n <= 1: return n
    # for any other number, return the sum of the previous 2 Fibonacci numbers
    # by recursively calling fib()
    else: return fib(n-1) + fib(n-2)

def fibonacci(n):
    '''returns the fibonacci number at position n'''
    # if n is 0 or 1, return n because there is no sequence to add
    if n <= 1: return n
    # for any other number, return the sum of the previous 2 Fibonacci numbers
    # by recursively calling fib()
    else: return fib(n-1) + fib(n-2)


print(fib(50))



# exercise 2: convert integer to binary using recursion
def to_binary(n: int) -> str:
    '''returns the binary representation of n'''
    # binary of n <= 1 is n
    if n <= 1: return n
    else: return (
        # when we divide by 2, we either have a remainder of 0 or 1, which is 
        # the last digit in binary; 
        # to get that remainder, we just modulo by 2;returns the remainder 
        # of n divided by 2, e.g. 5%2 = 1, 4%2 = 0; 
        to_binary(n%2)  
        # for any other number, get the floor of n/2 and pass it back to_binary()
        # and multiply the result by 10 to shift left in binary
        + 10*to_binary(n//2) 
    )

# testing 
print(to_binary(255))


# exercise 3: pandas dataframe manipulation
url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'

df_bellevue = pd.read_csv(url)

# for two of the tasks below, we need to fix the gender; this function is
# designed to do that without having to re-create the same code.
def fix_gender():
    '''returns the dataframe of bellevue with corrected gender markers (replaces anything ^m or ^w with NaN)'''
    # first, fix the gender column to set the invalid values to NaN
    df_fixedgender = df_bellevue.copy()
    df_fixedgender['gender'] = df_fixedgender['gender'].where(df_fixedgender['gender'].isin(['m', 'w']), np.nan)
    return df_fixedgender


#1. Return a list of all column names, *sorted* such that 
# the first column has the *least* missing values, 
# and the last column has the *most* missing values (use the raw column names).
def task_1():
    '''returns column list sorted by number of missing values ascending'''
    # get a dataframe with the fixed genders from the fix_gender function
    df_fixedgender = fix_gender()

    # return the list of column names sorted by number of missing values
    return df_fixedgender.isnull().sum().sort_values(ascending=True).index.tolist()


# testing task_1()
print(task_1())



#2. Return a **data frame** with two columns:
#   - the year (for each year in the data), `year`
#   - the total number of entries (immigrant admissions) for each year, `total_admissions`
def task_2():
    '''returns a dataframe with year and total_admissions columns'''
    #add a new column 'year' extracted from the 'admission_date' column
    df_bellevue['year'] = pd.to_datetime(df_bellevue['date_in'], errors='coerce').dt.year

    # group by year and count the number of entries for each year
    df_yearly = df_bellevue.groupby('year').size().reset_index(name='total_admissions')
    return df_yearly
 

# testing task_2()
print(task_2())


# 3. Return a **series** with:
#   - Index: gender (for each gender in the data)
#   - Values: the average age for the indexed gender.

def task_3():
    '''returns a series with average age per gender'''

    # first, get the gender-adjusted dataframe from fix_gender() function
    df_fixedgender = fix_gender()
    # first group by, then calculate the mean age for each, and return the series
    return df_fixedgender.groupby('gender')['age'].mean()



# testing task_3()
print(task_3())


# 4. Return a list of the 5 most common professions *in order of prevalence* (so, the most common is first).
def task_4():
    '''returns a list of the 5 most common professions in order of prevalence'''
    # group by profession, count the occurrences, sort descending, get the top 5, and return as a list
    return df_bellevue.groupby('profession').size().sort_values(ascending=False).head(5).index.tolist()

# testing task_4()
print(task_4())