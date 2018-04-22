n=int(input())
arr = list(map(int,input().strip().split()))
wgt = list(map(int,input().strip().split()))
answer = [x*w for x,w in zip(arr,wgt)]
mean = sum(answer)/sum(wgt)
print('{:.1f}'.format(mean))
