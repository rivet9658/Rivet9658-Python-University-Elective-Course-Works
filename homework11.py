def function(al,an,d):
    sum=0
    for i in range(al,an+1,d):
        sum=sum+i
        if i==an:
            print(i)
            break
        print(i,end=" ")
    print(sum)
def main():
    al,an,d=map(int,input().split())
    function(al,an,d)
main()
