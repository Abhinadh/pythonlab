a1=input("enter integers")
b1=input("enter integers")
a=set(map(int,a1.split(",")))
b=set(map(int,b1.split(",")))
print("they are in same length:",bool(len(a)==len(b)))
print("sum to the same value:",bool(sum(a)==sum(b)))


print("value occure in both:", len(a & b))
