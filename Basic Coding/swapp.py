n=int(input("Enter a number: "))
a=list(map(int,input("Enter the numbers: ").split()))
for i in range(n):
    for j in range(i+1,n):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i] 
print("Sorted list: ",a)
