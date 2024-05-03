# -*- coding: utf-8 -*-
"""
Created on Fri May  3 11:00:07 2024

@author: Madhu
"""
def Insertion_sort(list1):
    n=len(list1)
    for i in range(1,n):
        v=list1[i]
        j=i-1
        while j>=0 and list1[j]>v:
            list1[j+1]=list1[j]
            j=j-1
            list1[j+1]=v
    return list1



l=[2,4,1,4,6,7,3,1,0,2]
print("elements before sort",l)
Insertion_sort(l) 
print("elements after sort ",l)