n=input("enter some words")
n.split()
alpha={}

for i in n:
    alpha[i]=alpha.get(i,0)+1
    del alpha[" "]
print(alpha)    
