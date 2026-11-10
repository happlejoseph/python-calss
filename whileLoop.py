

import time

# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1

# else: print('loop finished')



# Stars
rows = 5
i = 1

while i <= rows:
    space = rows - i
    stars = 2 * i - 1

    print(' ' * space + '*' * stars)

    time.sleep(1)

    i = i + 1