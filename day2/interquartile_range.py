n = int(input())
a = list(map(int,input().strip().split()))
w = list(map(int,input().strip().split()))
arr=[]
for i in range(n):
    temp = [a[i]]*w[i]
    arr += temp
    
arr = sorted(arr)
n = len(arr)
def median(arr,l):
    if(l%2 == 0):
        med = (arr[(l//2)-1]+arr[l//2])/2
    else:
        med = arr[(l-1)//2]
    return med

if(n%2 == 0):
    q1 = median(arr[:n//2],len(arr[:n//2]))
    q3 = median(arr[n//2:],len(arr[n//2:]))
else:
    q1 = median(arr[:(n-1)//2],len(arr[:(n-1)//2]))
    q3 = median(arr[(n+1)//2:],len(arr[(n+1)//2:]))

print("{:.1f}".format(q3-q1))

