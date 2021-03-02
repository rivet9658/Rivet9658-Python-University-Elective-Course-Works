def function(x1,y1,x2,y2,x3,y3):
    i=1
    while True:
        if i % x1 == y1:
            if i % x2 == y2:
                if i % x3 ==y3:
                    return i
                    break
                else:
                    i=i+1
            else:
                i=i+1
        else:
            i=i+1
def main():
    x1,y1,x2,y2,x3,y3=map(int,input().split())
    print(function(x1,y1,x2,y2,x3,y3))
    
main()
