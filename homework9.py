def function(n):
    check1=n
    check2=n
    for k in range(0,n):
        for i in range(1,check1+1):
            print("#",end="")
        for j in range(check2,0,-1):
            if j==1:
                print(j,end="\n")
                break
            print(j,end="")
        check1=check1+1
        check2=check2-1
def main():
    n=int(input())
    function(n)

main()
