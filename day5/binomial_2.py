p,n = list(map(int,input().strip().split()))
p /= 100

def fact(x):
    return 1 if x==0 else x*fact(x-1)

def combination(n,r):
    return fact(n)/(fact(r)*fact(n-r))

def binomial(n,p,x):
    return (combination(n,x))* (p**x) * ((1-p)**(n-x))

# no more than 2 reject - maximum 2 rejects
ans_1 = 0
for i in range(0,3):
    ans_1 += binomial(n,p,i)

# at least 2 rejects
ans_2 = 1-ans_1+binomial(n,p,2)

print("{:.3f}\n{:.3f}".format(ans_1,ans_2))