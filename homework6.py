def test(x1,x2,x3,y1,y2,y3):
    
    if x1=="A":
        xx1=1
    elif x1=="J" or x1=="Q" or x1=="K":
        xx1=0.5
    else:
        xx1=int(x1)
        
    if x2=="A":
        xx2=1
    elif x2=="J" or x2=="Q" or x2=="K":
        xx2=0.5
    else:
        xx2=int(x2)
        
    if x3=="A":
        xx3=1
    elif x3=="J" or x3=="Q" or x3=="K":
        xx3=0.5
    else:
        xx3=int(x3)
    
    xtotal=xx1+xx2+xx3
    
    if y1=="A":
        yy1=1
    elif y1=="J" or y1=="Q" or y1=="K":
        yy1=0.5
    else:
        yy1=int(y1)
        
    if y2=="A":
        yy2=1
    elif y2=="J" or y2=="Q" or y2=="K":
        yy2=0.5
    else:
        yy2=int(y2)
        
    if y3=="A":
        yy3=1
    elif y3=="J" or y3=="Q" or y3=="K":
        yy3=0.5
    else:
        yy3=int(y3)
        
    ytotal=yy1+yy2+yy3
    
    if xtotal>10.5:
        xtotal=0
    if ytotal>10.5:
        ytotal=0
        
    if xtotal>ytotal:
        an="A贏"
    elif xtotal<ytotal:
        an="B贏"
    elif xtotal==ytotal:
        an="平手"
    
    return xtotal,ytotal,an
xa=str(input())
xb=str(input())
xc=str(input())
ya=str(input())
yb=str(input())
yc=str(input())
xx,yy,zz=test(xa,xb,xc,ya,yb,yc)
print(xx)
print(yy)
print(zz)
