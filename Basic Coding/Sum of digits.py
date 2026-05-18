n = input()
sum_digits = 0
for digit in n:
    sum_digits += int(digit)
print(sum_digits)


#------# Alternative solution using list comprehension
n = input() 
sum_digits = sum(int(digit) for digit in n)
print(sum_digits)

#------# Alternative solution using map function
n = input()
sum_digits = sum(map(int, n))
print(sum_digits)

#------# Alternative solution using while loop
n = input() 
sum_digits = 0
i = 0
while i < len(n):
    sum_digits += int(n[i])
    i += 1
print(sum_digits)

#------# Alternative solution using recursion
def sum_of_digits(num):
    if num == 0:
        return 0
    else:
        return int(num % 10) + sum_of_digits(int(num / 10))

# Alternative solution using while loop and modulus operator`
num = int(input())
digit_sum = 0

while num > 0:
    digit_sum += num % 10
    num //= 10
print(digit_sum)