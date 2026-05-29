# Faster solution (O(1))

# Observe:

# If n is even → answer = -n/2
# If n is odd → answer = (n+1)/2
n = int(input())

if n % 2 == 0:
    print(-n // 2)
else:
    print((n + 1) // 2)


#------------------------------------------
n = int(input())

s = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        s -= i
    else:
        s += i

print(s)