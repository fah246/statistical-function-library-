# -*- coding: utf-8 -*-

import math
# count
def count(a):
    cnt = 0;
    for i in a:
        cnt =cnt+1;
    return cnt;

#%%
# describe
def describe_count(b):
    cnt = 0;
    for i in b:
        cnt =cnt+1;
    return cnt
    
def describe_mean(b):
    sum = 0;
    for i in b:
        sum+=i;
    n = len(b)
    return sum/n;

def describe_std(b):
    n = len(b)
    
    sum = 0;
    for i in b:
        sum+=i;
    mean = sum/n;
    
    s = 0
    for i in b:
        s = s + ((i - mean)**2)
    std = math.sqrt(s / (n-1))
    return std

def describe_min(b):  
    min = 99999999
    for i in b:
        if(i <min):
            min = i
    return min
    
def describe_25percentile(b):
    n=len(b)
    b = b.tolist()
    b.sort()
    lower_quartile=int((n+1)/4)
    q25 = b[lower_quartile]
    return q25
 
def describe_50percentile(b):
    n=len(b)
    b = b.tolist()
    b.sort()
    middle_quartile=int((n+1)/2)
    q50 = b[middle_quartile]
    return q50
 
def describe_75percentile(b): 
    n=len(b)
    b = b.tolist()
    b.sort()
    upper_quartile=int((n+1)*0.75)
    q75 = b[upper_quartile]
    return q75

def describe_max(b):  
    max = -99999999
    for i in b:
        if(i >max):
            max = i
    return max
#%%
# min,max
def min(c):  
    min = 99999999
    for i in c:
        if(i <min):
            min = i
    return min
    
    
def max(c):  
    max = -99999999
    for i in c:
        if(i >max):
            max = i
    return max
    
#%%
# argmin,argmax  
def argmax(c):
    max = -99999999
    for index, c in enumerate(c):
        if(c >max):
            max = c
            idx = index
    return idx
        
def argmin(c):
   min = 99999999
   for index, c in enumerate(c):
       if(c < min):
           min = c
           idx = index
   return idx
 
#%%
# idxmin,idxmax  
def idxmax(c):
    max = -99999999
    for index, c in enumerate(c):
        if(c >max):
            max = c
            idx = index
    return idx
        
def idxmin(c):
   min = 99999999
   for index, c in enumerate(c):
       if(c < min):
           min = c
           idx = index
   return idx
                       
#%%
def sum(a):
     sum = 0;
     for i in a:
         sum= sum+i;
     return sum
     


     #%% mean


def mean(a):
     n = len(a)
     sum = 0
     for i in a:
         sum=sum+i
     return sum/n
     


    
     
        #%% median
def median(a):
    n = len(a)
    a= a.tolist()
    a.sort()
    if n % 2 == 0:
        median1 = a[n//2]
        median2 = a[n//2 - 1]
        median = (median1 + median2)/2
    else:
        median =a[n//2]
    return median



#%% mean absolute deviation

def mad(a):
    mean1 = mean(a)
    dev = 0
    for num in a:
        dev = dev + abs(num - mean1)
    mad = dev/len(a)
    return mad

#%%
def trimmedmean(a,p):
    n=len(a)
    a = a.tolist()
    a.sort()
    sumi =0
    for i in range(a[p],a[n-p]):
        sumi = sumi + i
    return sumi/n-2*p
#%%
def cov(a, b):
    a_mean = mean(a)
    b_mean = mean(b)
    sumi = 0
    for i in range(0, len(a)):
        sumi += ((a[i] - a_mean) * (b[i] - b_mean))

    return sumi/(len(a)-1)



#%%
def stdev(a):
    n = len(a)
    l= mean(a)
    deviation=0
    for i in a:
        deviation = deviation + (i - l)**2
    variance = deviation/n
    std_dev = variance**0.5
    return std_dev



def corr(a,b):
    correlaiton= cov(a, b)/(stdev(a)*stdev(b))
    return correlaiton

#%%
def lower_quartile(a):
    n=len(a)
    a = a.tolist()
    a.sort()
    lower_quartile=int((n+1)/4)
    l = a[lower_quartile]
    return l
    
        
        
        
 #   return l
#a=[1,2,3,4,5,6]
#print(lower_quartile(a))
#%%
def upper_quartile(b):
    n=len(b)
    b = b.tolist()
    b.sort()
    upper_quartile=int(3*(n+1)/4)
    u= b[upper_quartile]
    return u

#%%
def sort(a):
    for i in range(1,len(a)-1):
        min_idx = i
        for idx in range(i + 1, len(a)-1):
            if a[idx] < a[min_idx]:
                min_idx = idx
        a[i], a[min_idx] = a[min_idx], a[i]
    return a 



#%%
def prod(a):
    val=1
    for i in a:
        val *= i
    return val



#%%
def var(a):
    value =0
    x_bar = mean(a)
    n = len(a)
    for i in a:
        diff = (i-x_bar)
        p = pow(diff,2)
        value += p
    return value/(n-1)


#%%
def std(a):
    value = var(a)
    return math.sqrt(value)

#%%   
    
def skew(a):
    val=0
    x_bar = mean(a)
    n = len(a)
    std1 = pow(std(a),3)
    for i in a:
        diff = (i-x_bar)**3
        val += diff/((n-1)*std1)
    return val

#%%

def kurt(a):
    val =0
    x_bar = mean(a)
    n = len(a)
    std1 = pow(std(a),4)
    for i in a:
        dif = (i-x_bar)**4
        val += dif/((n-1)*std1)
    return val-3

#%%
# Cumsum
 
def cumsum(n):     
    c_sum = 0;     
    for i in n:         
        c_sum=c_sum+i;     
    return c_sum; 
    

#%%
#Cummax

def cummax(n):
    MAX=n[0]
    for i in n:
        if i>MAX:
            MAX=i
    return MAX;


#%%
#Cummin

def cummin(n):
    min=n[0]
    for i in n:
        if i<min:
            min=i
    return min;


#%%
# Cumprod

def cumprod(n):
    c_prod = 1
    for i in n:
        c_prod = c_prod*i
    return c_prod


#%%
# Difference
def diff(n):
    d=[]
    for i in range(1,len(n)):
       d = n[i]-n[i-1]
    return d


#%%
# Pct Change

def pct_change(n):
    list=[]
    for i in range(1,len(n)):
        list = (n[i]-n[i-1])/n[i-1]
    return list  



  
    
    
    