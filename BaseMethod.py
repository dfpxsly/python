#coding=utf-8

#生成随机数列
from random import randint

def getRandomArray(n,min,max):
    arr=[]
    arr=[randint(min,max) for x in range(n)]
    return arr

#生成基本有序的数列
def getArray(n,swapTimes):
    arr=[]
    for i in range(n):
        arr.append(i)
    for j in range(swapTimes):
        posx=randint(0,n-1)
        posy=randint(0,n-1)
        arr[posx],arr[posy]=arr[posy],arr[posx]
    return arr

#判断数列是否有序（算法是否正确）
def isSorted(alist):
    print(alist)
    for i in range(0,len(alist)-1):
        if alist[i] > alist[i+1]:
            return False
        return True

#测试算法
    
def testSort(func,alist):
    print(alist)
    assert isSorted(func(alist)), "排序算法错误"
