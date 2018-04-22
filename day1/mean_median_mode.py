n = int(input())
arr = list(map(int,input().strip().split()))

# mean
mean = sum(arr)/len(arr)
print('{:.1f}'.format(mean))

# median
arr = sorted(arr)
if(len(arr)%2 == 0):
    n=len(arr)//2
    median = (arr[n-1]+arr[n])/2
else:
    n = (len(arr)+1)//2
    median = arr[n-1]
print('{:.1f}'.format(median))

# mode
from collections import Counter
from operator import itemgetter
temp = Counter(arr)
mode = sorted(temp.items(),key = itemgetter(1),reverse=True)
max_value = mode[0][1]
all_keys = [x[0] for x in mode if x[1]==max_value]
mode = min(all_keys)
print(mode)


    

