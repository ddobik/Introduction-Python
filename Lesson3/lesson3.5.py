from random import randint
for i in range(3):
 x = int(input('Enter number from 1 to 10: '))
 y = randint(1, 10)
 print('Random number from 1 to 10:', y)
 if x != y:
     print('You lose!')
 else:
     print('You won!')
     break
