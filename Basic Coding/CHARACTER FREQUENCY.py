n,t=input().split()
c=0
for s in n:
  if s==t:
    c+=1
print(c)
#---------------#
# Read the single line of input and split it by the space
string_input, char_to_count = input().split()

# Count the occurrences using the built-in count function
result = string_input.count(char_to_count)

# Output the result
print(result)