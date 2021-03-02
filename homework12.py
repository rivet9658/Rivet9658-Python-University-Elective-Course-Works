def function1(n):
    m=0
    check=1
    for c in range(1,n,2):
        m+=1
        
    for i in range (0,n-m):
        for j in range (1,check+1):
            print("*",end="")
        check+=1
        print()
        
    for l in range(0,m):
        for k in range (check-2,0,-1):
            print("*",end="")
        check-=1
        print()

def function2(n):
    m=0
    check=1
    for c in range(1,n,2):
        m+=1
    check2=n-m-1
    
    for i in range (0,n-m):
        for d in range(0,check2):
            print(".",end="")
        for j in range (1,check+1):
            print("*",end="")
        check+=1
        check2-=1
        print()
        
    check2+=1   
    
    for l in range(0,m):
        check2+=1
        for d in range(0,check2):
            print(".",end="")
        for k in range (check-2,0,-1):
            print("*",end="")
        check-=1 
        print()

def function3(n):
    m=0
    check=1
    for c in range(1,n,2):
        m+=1
    point=n-m-1
    
    for i in range(0,n-m):
        for p in range(0,point):
            print(".",end="")
        for j in range(1,check+1):
            print("*",end="")
        check+=2
        point-=1
        print()
    
    point+=1
    check-=2
    
    for i in range(0,m):
        point+=1
        for p in range(0,point):
            print(".",end="")
        for j in range(check-2,0,-1):
            print("*",end="")
        check-=2
        print()
        
def main():
    m=int(input())
    n=int(input())
    if m==1:
        function1(n)
    elif m==2:
        function2(n)
    elif m==3:
        function3(n)
    
main()
