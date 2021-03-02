def BMI(m,kg,bmi):
    if m<0.5 or m>2.5:
        print("Input Error 0.5~2.50")
    elif kg<20 or kg>300:
        print("Input Error 20~300")
    else:
        if bmi<18.5:
            print("BMI too low")
        elif bmi>24:
            print("BMI too hight")
        else:
            print(round(bmi,2))

def main():
    t=str(input())
    while t!="-1":
        mstr=t.split(" ",1)[0]
        kgstr=t.split(" ",1)[1]
        m=float(mstr)
        kg=float(kgstr)
        bmi=kg/(m*m)
        BMI(m,kg,bmi)
        t=str(input())
main()
