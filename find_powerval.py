#  Power x^n


def power(x,n):
    if x==1:
        return 1
    if x==0:
        return 0 
    if n==0:
        return 1
    return x*power(x,n-1)
x = int(input("base: "))
n = int(input("power: "))
print(power(x,n))