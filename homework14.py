def function(n):#點數計算
    k=0
    if n=="A":
        k=1
    elif n=="J" or n=="Q" or n=="K":
        k=0.5
    else:
        k=int(n)
    return k
   
def Atest()#判斷A的點數是否超過21
    global Atotal
    checkA=0
    if Atotal>21:
        Atotal=0
        checkA=1
    return checkA

def Btest():#判斷B的點數是否超過21
    global Btotal
    checkB=0
    if Btotal>21:
        Btotal=0
        checkB=1
    return checkB

def main():
    global Atotal
    global Btotal
    Acard=0
    Bcard=0
    
    a1,b1=map(str,input().split())
    Acard+=1
    Atotal+=function(a1)
    Bcard+=1
    Btotal+=function(b1)
    
    while True:
        if Acard==5 or Bcard==5:
            break
        else:
            t=str(input())
            if t.split()[0]=="0": #A不拿牌
                if t.split()[1]=="0": #A、B不拿牌
                    break
                elif t.split()[1]=="1": #A不拿牌 B拿牌
                    Bcard+=1
                    Btotal+=function(t.split()[2])
                    if Atest()==1 or Btest()==1:
                        break
            elif t.split()[0]=="1": #A拿牌
                if Acard>5 or Bcard>5:
                    break
                else:
                    Acard+=1
                    Atotal+=function(t.split()[1])
                    if t.split()[2]=="0": #A拿牌 B不拿牌
                        if Atest()==1 or Btest()==1:
                            break
                    elif t.split()[2]=="1": #A、B拿牌
                        Bcard+=1
                        Btotal+=function(t.split()[3])
                        if Atest()==1 or Btest()==1:
                            break
            
    if Atotal>Btotal:
        print("Player X is Winner")
    elif Atotal<Btotal:
        print("Player Y is Winner")
    
    if Atotal==0:
        print("Player X $ Bang!")
    else:
        print("Player X $",Atotal)
  
    if Btotal==0:
        print("Player Y $ Bang!")
    else:
        print("Player Y $",Btotal)



Atotal=0
Btotal=0       
main()
