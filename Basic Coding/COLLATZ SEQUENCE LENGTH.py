# # Description
# # Write a program that takes a positive integer N. Apply the Collatz rules: if even divide by 2; if odd multiply by 3 and add 1. Count and print the number of steps it takes to reach 1.
# # Examples
# # Example 1

# # Input: 3 Output: 7
# # Explanation:
# # 3->10->5->16->8->4->2->1 (7 steps)
# # Sample Test Cases
# # Case 1
# # Input: 3 Output: 7
# # Case 2
# # Input: 1 Output: 0
# # Case 3
# # Input:4 Output: 2
# Code
n=int(input())
c=0
while(n!=1):
  if n%2!=0:
    n=n*3+1
    c+=1
  else:
    n=n//2
    c+=1
print(c)
