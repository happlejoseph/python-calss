

# Map
# num_list = [1, 2, -3, -6, 8]

# print(list(map(abs, num_list)))

num_list = [1, 2, -3, -6, 8]

print(list(map(lambda x: x + 1, num_list)))


# filter
def positive(num):
    return True if num > 0 else False

print(list(filter(positive, [1, 2, 3, -4, -5, 6])))




print(list(filter(lambda x: x.isupper(), 'AppLe')))