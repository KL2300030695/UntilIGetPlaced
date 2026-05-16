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