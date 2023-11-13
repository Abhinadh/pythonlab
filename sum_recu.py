def sum_list(n):
    """sum of list"""
    if len(n)==1:
        return n[0]
    else:
        return n[0]+ sum(n[1:])
        
  
s=input("enter a lsit of element")
n=list(map(int,s.split()))
print(sum_list(n))
