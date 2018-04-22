n = int(input())
arr = list(map(int,input().strip().split()))
arr = sorted(arr)
def median(arr,l):
    if(l%2 == 0):
        med = (arr[(l//2)-1]+arr[l//2])//2
    else:
        med = arr[(l-1)//2]
    return med

q2 = median(arr,n)
if(n%2 == 0):
    q1 = median(arr[:n//2],len(arr[:n//2]))
    q3 = median(arr[n//2:],len(arr[n//2:]))
else:
    q1 = median(arr[:(n-1)//2],len(arr[:(n-1)//2]))
    q3 = median(arr[(n+1)//2:],len(arr[(n+1)//2:]))

print("{}\n{}\n{}".format(q1,q2,q3))

