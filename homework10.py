def function(m,n):
    sum=0
    for i in range(m,n+1):
        if i%2==0:
            sum=sum+i
    return sum
def main():
    m=int(input())
    n=int(input())
    print(function(m,n))
main()
