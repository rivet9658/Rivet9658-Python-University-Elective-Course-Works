def fruit(x,y,z):
    
    xprice=x*30
    if (x>=0 and x<=10):
        xprice=xprice
    elif(x>=11 and x<=15):
        xprice=xprice*0.95
    elif(x>=16 and x<=20):
        xprice=xprice*0.9
    else:
        xprice=xprice*0.8
    
    yprice=y*70
    if (y>=0 and y<=10):
        yprice=yprice
    elif(y>=11 and y<=15):
        yprice=yprice*0.9
    elif(y>=16 and y<=20):
        yprice=yprice*0.85
    else:
        yprice=yprice*0.75
        
    zprice=z*40
    if (z>=0 and z<=10):
        zprice=zprice
    elif(z>=11 and z<=15):
        zprice=zprice*0.85
    elif(z>=16 and z<=20):
        zprice=zprice*0.8
    else:
        zprice=zprice*0.8
    
    total=x+y+z
    totalprice=xprice+yprice+zprice
    if (total>=30):
        totalprice=totalprice*0.87
    return totalprice
n1=int(input())
n2=int(input())
n3=int(input())
price=fruit(n1,n2,n3)
print(int(price))
