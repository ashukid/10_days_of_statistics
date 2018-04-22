import math

n = int(input())
arr = list(map(int,input().strip().split()))

mean = sum(arr)/n
std = math.sqrt(sum([(x-mean)*(x-mean) for x in arr])/n)


print("{:.1f}".format(std))
