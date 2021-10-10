
def compute_gcd(x,y):
    while(y):
        x,y=y,x%y
        return x
def compute_lcm(x,y):
    lcm=(x*y)//compute_gcd(x,y)
    return lcm
num1=(int)(input("enter"))
num2=(int)(input("enter"))
print("lcm",compute_lcm(num1,num2))
print("gcd",compute_gcd(num1,num2))
