# List comprehensions with filters
mylist = list(range(100))
filteredlist = [item for item in mylist if item % 10 == 0]
print(filteredlist)