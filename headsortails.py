import random

flip = random.randrange(0,1001)

if flip < 500:
    print 'You got heads'
else:
    print 'you got tails'

print flip 
