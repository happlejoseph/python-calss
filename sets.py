

set_one = {1, 2, 3, 4}
# print(set_one, type(set_one))

# set function
set_two = set([1, 2, 3])
print(set_two, type(set_two))


# Create an empty set
set_three = set()
print(set_three, type(set_three))

print(len(set_one))



# adding element to set
set_one.add(5)
print(set_one)


# adding multiple element to set
set_one.update((6,7,8))
print(set_one)


name_set = {'happle'}
print(name_set)

name_set.update('joseph')
print(name_set)


# Convert a string to a set of unique characters
letters = set('helo')
print(letters)


# Convert a list to a set
fruits = set(['apple', 'orange', 'banana'])
print(fruits)



# remove element in set
num = set([1, 2, 3, 4])
print(num)

num.remove(3)
print(num)



# set union
# def set_union(s1, s2):
#     return s1.union(s2)

# s_one = {1, 2, 3, 4, 5, 6}
# s_two = {5, 6, 7, 8, 9, 10}

# print('union', set_union(s_one, s_two))


# set intersation

def set_intersection(s1, s2):
    return s1.intersection(s2)


s_one = {1, 2, 3, 4, 5, 6}
s_two = {5, 6, 7, 8, 9, 10}

print('intersection', set_intersection(set_one, set_two))
