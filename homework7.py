def ed1(n):
    sum1=0
    for i in range(1,n+1,2):
        sum1=sum1+i
    return sum1
def ed2(n):
    sum2=1
    for i in range(1,n+1,3):
        sum2=sum2*i
    return sum2
n=int(input())
print(ed1(n))
print(ed2(n))
