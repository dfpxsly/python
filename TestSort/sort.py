#coding=utf-8
from BaseMethod import testSort
from BaseMethod import getRandomArray
import timeit

#getRandomArray(10,0,20)

#冒泡排序 O(n^2)
def bubbleSort(alist):
    n=len(alist)
    for i in range(0,n-1):
        for j in range(0,n-1):
            if alist[j]>alist[j+1]:
                alist[j],alist[j+1]=alist[j+1],alist[j]
    return alist

#选择排序 O(n^2)
def selectSort(alist):
    n=len(alist)
    for i in range(0,n):
        min_index=i
        for j in range(i+1,n):
            if alist[j]<alist[min_index]:
                min_index=j
        alist[i],alist[min_index]=alist[min_index],alist[i]
    return alist

#插入排序 O(n^2)
def insertSort(alist):
    n=len(alist)
    for i in range(1,n):
        tmp=alist[i]
        j=i-1
        while j>=0 and alist[j]>tmp:
            alist[j+1]=alist[j]
            j=j-1          
        alist[j+1]=tmp
    return alist
#希尔排序
                
                

arr = [11, 7, 15, 17, 12, 17, 18, 15, 6, 15] 
t1 = timeit.Timer('testSort(bubbleSort, arr)', 'from __main__ import testSort, bubbleSort, arr')
print('bubbleSort：%s s' %t1.timeit(number=1))

arr = [11, 7, 15, 17, 12, 17, 18, 15, 6, 15] 
t1 = timeit.Timer('testSort(selectSort, arr)', 'from __main__ import testSort, selectSort, arr')
print('selectSort：%s s' %t1.timeit(number=1))

arr = [11, 7, 15, 17, 12, 17, 18, 15, 6, 15] 
t1 = timeit.Timer('testSort(insertSort, arr)', 'from __main__ import testSort, insertSort, arr')
print('insertSort：%s s' %t1.timeit(number=1))
