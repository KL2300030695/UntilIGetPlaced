#Optimal Solution of Time Complexity O(n) and Space Complexity O(n)
s = input()
stack = []
balanced = True
for ch in s:
    if ch in "({[":
        stack.append(ch)
    else:
        if not stack:
            balanced = False
            break
        top = stack.pop()
        if (ch == ')' and top != '(') or \
           (ch == '}' and top != '{') or \
           (ch == ']' and top != '['):
            balanced = False
            break
if stack:
    balanced = False
if balanced:
    print(s, "- Balanced")
else:
    print(s, "- Not Balanced")

#Brute Force Solution of Time Complexity O(n^2) and Space Complexity O(n)
s = input()
while "()" in s or "{}" in s or "[]" in s:
    s = s.replace("()", "")
    s = s.replace("{}", "")
    s = s.replace("[]", "") 
if not s:
    print("Balanced")   
else:    print("Not Balanced")
