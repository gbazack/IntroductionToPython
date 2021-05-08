"""
This module contains functions
which generate prime numbers
and test if an input number is prime
"""
from math import gcd

def generator(n):
   pnList=[2,3]
   nlist=list(range(4,n+1))
   
   for x in nlist:
      y=[gcd(i,x) for i in nlist]      
      if(y.count(1)+y.count(x))==len(y):
         pnList.append(x)
   return pnList


def isprime(n):
   pnList=generator(999)
   if n in pnList:
      return True
   else:
      return False
