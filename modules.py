
# import the full modeule
# import function

# result = function.checkEven(7)
# print(result)

# to check the modeule
print(__name__)



# only impot the needed function
from function import checkEven

print (checkEven(8))


# changing the import file name

# import function as fun


# change the import function name

# from function import checkEven as chek


import platform
print(platform.system())