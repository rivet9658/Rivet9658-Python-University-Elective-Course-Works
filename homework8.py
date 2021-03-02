def BMI(name,kg,m):
    bmi=kg/(m*m)
    if bmi>24:
        text="Hi %s, Your BMI: %f too HIGH."%(name,bmi)
    elif bmi<18.5:
        text="Hi %s, Your BMI: %f too LOW."%(name,bmi)
    else:
        text="Hi %s, Your BMI: %f Normal."%(name,bmi)
    return text
name=str(input())
kg=float(input())
m=float(input())
print(BMI(name,kg,m))
