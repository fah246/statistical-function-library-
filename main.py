# -*- coding: utf-8 -*-


#%%
import group3
import pandas as pd
df = pd.read_csv('german.csv')
df1 = pd.read_csv('german.csv')
print(df.head())
df1.columns=['existingacc','duration','credithist','purpose','creditamount','savingsaccount','durationofemployence','installmentrate','personal_sexandstatus','debt_guarantor','residencesince','property','age','otherinstallment','housing','no_ofcredit','job','no_maintenance_provider','telephone','foreign_worker','cost_matrix']
age1 = df1['age']
duration= df1['duration']
df.head()
df1.head()

#%%
series1 = df['Duration_in_month']
print("Module Output: count =", "%d"%group3.count(series1))
print("Pandas Output: count =", df[['Duration_in_month']].count())

#%%
series2 = df['Credit_amount']

print("Module Output:")
print("count    ", "%.4f"%group3.describe_count(series2))
print("mean     ", "%.4f"%group3.describe_mean(series2))
print("std      ", "%.4f"%group3.describe_std(series2))
print("min      ", "%.4f"%group3.describe_min(series2))
print("25%      ", "%.4f"%group3.describe_25percentile(series2))
print("50%      ", "%.4f"%group3.describe_50percentile(series2))
print("75%      ", "%.4f"%group3.describe_75percentile(series2))
print("max      ", "%.4f"%group3.describe_max(series2))
print("Pandas Output:", df[['Credit_amount']].describe())

#%%
series3 = df['Age_in_years']
print("Module Output: min = ", "%d"%group3.min(series3))
print("Pandas Output: min = ", df[['Age_in_years']].min())

print("Module Output: max = ", "%d"%group3.max(series3))
print("Pandas Output: max = ", df[['Age_in_years']].max())

#%%
series4 = df['Credit_amount']
print("Module Output: argmax =  = ", "%d"%group3.argmax(series4))
print("Pandas Output:argmax = ", df['Credit_amount'].argmax())

print("Module Output: argmin =  = ", "%d"%group3.argmin(series4))
print("Pandas Output:argmin = ", df['Credit_amount'].argmin())

#%%
series4 = df['Credit_amount']
print("Module Output: idxmin =  = ", "%d"%group3.idxmin(series4))
print("Pandas Output:idxmin = ", df[['Credit_amount']].idxmin())

print("Module Output: idxmax =  = ", "%d"%group3.idxmax(series4))
print("Pandas Output:idxmax = ", df[['Credit_amount']].idxmax())

#%% sum


print("using module sum is =",group3.sum(age1))
print("using pandas module", age1.sum())
#%% mean

print("using module mean is =",group3.mean(age1))
print("using pandas function mean is",age1.mean())
#%%median

print("using module median is=",group3.median(duration))
print("using pandas function median is",duration.median())
#%% mean absolute deviation

print("using module absolute deviation=",group3.mad(age1))
print("using pandas function absolute deviation is",age1.mad())
#%% covariance
print("using module covarience is",group3.cov(age1, duration))
print("using pandas function covarience is",duration.cov(age1))
print("using pandas function covarience is",age1.cov(duration))

#%% correlation
print("using module correlation is",group3.corr(age1, duration))
print("using pandas function correlation is",duration.corr(age1))
print("using pandas function correlation is",age1.corr(duration))


#%% quartiles
print("using module lower quartile(Q1)",group3.lower_quartile(age1))
print("using module second quartile",group3.median(age1))
print("using module upper quartile(Q3)",group3.upper_quartile(age1))

print("using pandas function lower quartile (Q1) is",age1.quantile(0.25))
print("using pandas function median quartile  is",age1.quantile(0.5))
print("uisng pandas function upper quartile (Q3) is",age1.quantile(0.75))


#%% trimmed mean
print("trimmed mean is",group3.trimmedmean(age1,1)) # if we eleminate 1 extreme value from both side
print("trimmed mean is",group3.trimmedmean(duration,1))



#%% sort
print("sorted",group3.sort(age1))




#%%
series11 = df["Present_residence_since"]
print("Product(pandas): ",series11.prod())
print("Product(module): ",group3.prod(series11))

#%% Variance
series12 = df["Duration_in_month"]
print("Varience(pandas): ",series12.var())
print("Varience(module): ",group3.var(series12))

#%% Standard Deviation
series13 = df["Duration_in_month"]
print("Standard Deviation(pandas): ",series13.std())
print("Standard Deviation(module): ",group3.std(series13))

#%% Skewness
series14 = df["Credit_amount"]
print("Skew(pandas): ",series14.skew())
print("Skew(module): ",group3.skew(series14))

#%% Kurtosis
series15 = df["Credit_amount"]
print("Kurt(pandas): ",series15.kurt())
print("Kurt(module): ",group3.kurt(series15))




#%%
# Cumsum
series16 = df['Age_in_years'] 
print("Module Output: cumulatve =", "%d"%group3.cumsum(series16))
print("Pandas Output: cumulative sum =", df[['Age_in_years']].cumsum())

#%%
#Cummax
series17 = df['Age_in_years'] 
print("Module Output: cumulatve max =", "%d"%group3.cummax(series17))
print("Pandas Output: cumulative max =", df[['Age_in_years']].cummax())

#%%
#Cummin
series18 = df['Age_in_years'] 
print("Module Output: cumulatve min =", "%d"%group3.cummin(series18))
print("Pandas Output: cumulative min =", df[['Age_in_years']].cummin())

#%%
# Cumprod
series19 = df['Age_in_years'] 
print("Module Output: Cumulative prod =", "%d"%group3.cumprod(series19))
print("Pandas Output: Cumulative prod =", df[['Age_in_years']].cumprod())

    
#%%
# Difference   
series20 = df['Duration_in_month'] 
print("Module Output: Difference =", "%d"%group3.diff(series20))
print("Pandas Output: Difference =", df[['Duration_in_month']].diff())
    
#%%
# Pct Change
series21 = df['Duration_in_month'] 

print("Module Output: Percent Changes =","%d"%group3.pct_change(series21))
print("Pandas Output: Percent Changes =", df[['Duration_in_month']].pct_change())  











