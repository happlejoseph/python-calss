

# a = int(input('Entre a number: '))
# b= int(input('Entre a number: '))

# if a == 0 or b == 0:
#     print('enter a valied number')

# else:
#     c = a / b
#     print(c)




# try:

#     a = int(input('Enter a number: '))
#     b = int(input('Enter a number: '))
#     c = a /b 

# except:
#     print('Enter valid number')

# else: print(c)



# while True:

#     try:
#         a = int(input('Enter a number: '))
#         b = int(input('Enter a number: '))
#         c = a / b

#     except:
#         print('Enter a valied number!')

#     else:
#         print(c)
#         break




try:

    a = int(input())
    b = int(input())
    c = a / b
except ZeroDivisionError:
    print('division by zero')

except ValueError:
    print('Enter a valied number')

else:
    print(c)