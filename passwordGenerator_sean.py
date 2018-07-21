#password generator in python
#genrate a password of at least eight characters, and one capital
#one lower, number

import random

#letters = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@#$%^*&()_+=-{}][":\|;?><,./~`'

password = ' '

print  ('use letters listed = %s' %letters)

length = int(input('Enter the length of your password: '))

while len(password) != length:
    password = password + random.choice(letters)
    if len(password) == length:
        print ('password = %s' %letters)
