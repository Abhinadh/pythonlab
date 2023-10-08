n = input("Enter the list separated by commas: ")
n = list(map(int, n.split(",")))
d = set(n)  # Convert the list to a set to remove duplicates, then back to a list
print(d)
