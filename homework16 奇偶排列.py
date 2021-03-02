n=int(input()) #輸入幾個數
oddnumber=[] #奇數串列
evennumber=[] #偶數串列

for i in range(n):
    k=int(input()) #輸入數值
    if k%2==0:
        evennumber.append(k) #如果是偶數放入偶數串列
    else:
        oddnumber.append(k) #如果是奇數放入奇數串列

oddnumber.sort() #由小到大排列奇數串列
evennumber.sort() #由小到大排列偶數串列
evennumber.reverse() #由大到小排列偶數串列
out=oddnumber+evennumber #將奇數和偶數串列合在一起
print(out)
