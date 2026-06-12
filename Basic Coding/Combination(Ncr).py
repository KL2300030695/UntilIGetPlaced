#function
def fact(n):
  f=1
  for i in range(1,n+1):
    f*=i
  return f
n,r=map(int,input().split())
ncr=fact(n)//(fact(r)*fact(n-r))
print(ncr)