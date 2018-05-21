# def fact(n):
#     return 1 if n == 0 else n*fact(n-1)

# def comb(n, x):
#     return fact(n) / (fact(x) * fact(n-x))

# def b(x, n, p):
#     return comb(n, x) * p**x * (1-p)**(n-x)

# l, r = 1.09,1
# print(round(sum([b(i, 6, l / (l + r)) for i in range(3, 7)]), 3))

n,x,p,q=6,3,1.09,1
def factorial(y):
    if(y==0):
        return 1
    ans = 1
    while y:
        ans *= y
        y -= 1
    return ans

gbd = 0
while x!=n+1:
    bd = (factorial(n)/(factorial(n-x)*factorial(x)))*pow(p/(p+q),x)*pow(q/(p+q),n-x)
    gbd += bd
    x+=1
print("{:.3f}".format(gbd))