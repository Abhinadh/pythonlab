n=input("enter newfile")
word={}
for i in n.split(" "):
    word[i]=word.get(i,0)+1
print(word)    
