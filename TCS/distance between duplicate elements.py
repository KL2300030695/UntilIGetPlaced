#Brute Force Approach
#Time Complexity-O(n^2)
n = int(input())
arr = list(map(int, input().split()))
k = int(input())
found = False
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] == arr[j] and abs(i - j) <= k:
            found = True
            break
    if found:
        break
if found:
    print("Yes")
else:
    print("No")
    

#Optimal Approach
#Time Complexity-O(n)   
n = int(input())
arr = list(map(int, input().split()))       
k = int(input())
index_map = {}
found = False
for i in range(n):
    if arr[i] in index_map and abs(i - index_map[arr[i]]) <= k:
        found = True
        break
    index_map[arr[i]] = i
if found:
    print("Yes")        
else:
    print("No")
