

# for x in range(10):
#     num = int(input('Enter a number: '))

#     if num == 0:
#         break
#     print(num)

# print('Thank you!')


# for x in range(10):
#     num = int(input('Enter a number: '))

#     if num == 0:
#         continue
#     print(num)

# print('Thank you')





num = int(input('Enter a number: '))


for x in range(2,num):
    if num % x == 0:
        print('not a prime number')
        break

else: print('Prime number')