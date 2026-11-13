

name = 'happle'

print(name[1])

program = ['python', 'js', 'java', 'c++']
# MUTABLE
program [2] = 'typeScript'

# print(len(program))
# print(program[1])
# print(program)

# total = program + name

# appending
# program.append(name)
# program.append(input('enter a value: '))

# romoveing
# program.remove('js')
print(program)

# removing using pop
program.pop(2)
print(program)



# looping through list
# num_list = [1.2, 3.4, 5, 6.7]
# sum = 0

# for x in num_list:
#     sum = sum+1

# print('the sum: ',sum)



# list extenction
list_one = [1, 2, 3,]
list_two = [4, 5, 6]

list_one.extend(list_two)
print('extended: ', list_one)