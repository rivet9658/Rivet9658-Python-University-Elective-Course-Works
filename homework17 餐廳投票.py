#!/usr/bin/env python
# coding: utf-8

# In[9]:

def restaurant(n): #輸入餐廳
    re=[]
    for i in range(n):
        re.append(str(input()))
    return re #傳回餐廳串列

def vote(m,n): #輸入投票數
    vo=[]
    vonumber=[]
    
    for i in range(m): #個別投了誰
        vo.append(int(input()))
        
    for j in range(1,n+1): #計算票數
        vonumber.append(vo.count(j))
    return vonumber #傳回計算票數串列

def main():
    n=int(input())
    mainrestaurant=restaurant(n) #餐廳串列
    m=int(input())
    mainvote=vote(m,n) #計算票數串列
    k=max(mainvote) #找出票數串列最大的值
    c=mainvote.index(k) #票數串列最大的值是在串列裡是第幾個
    print(mainrestaurant[c],k) #印出票數最大的餐廳和票數
    
main()


# In[7]:




