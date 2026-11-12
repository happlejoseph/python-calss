

# add = lambda x: x + 1
# print(add(5))


# add = lambda x, y: x + y
# print(add(5, 5)) 



# Even od Odd
check = lambda num: 'Even' if num % 2 == 0 else 'Odd'
print(check(5))


# sorting
mark = [('Jone', '90'), ('Diya', '88'), ('Jeff', '75')]

mark.sort(key = lambda x: x[1])
print(mark)