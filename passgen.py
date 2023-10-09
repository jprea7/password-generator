import random

print('Your password')
chars = 'qwertyuiopasdfghjklzxcvbnm1234567890'

password = ''

for x in range(8):
    result = random.choice(chars)
    password += result

print(password)
