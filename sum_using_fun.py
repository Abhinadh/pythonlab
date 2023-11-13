def sum_list(n):
    """sum of list"""
    sum=0
    for i in n:
        sum+=i
    return sum
s=input("enter a lsit of element")
n=list(map(int,s.split()))
print(sum_list(n))

    
