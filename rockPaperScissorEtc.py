import random

# rock, paper, scissor, lizard, spock
pick = random.randrange(0,501)
try:
    inp = raw_input('Rock, Paper, Scissor, Lizard, Spock... What\'s your pick? ')
    inp = inp.capitalize()
    if inp != 'Rock' or inp != 'Paper' or inp != 'Scissor' or inp != 'Lizard' or inp != 'Spock':
        print ' Enter a valid response'

except:
    print 'You must select one of the five selections. You can\'t make up your own, silly.'
    quit()

if pick < 100:
    print 'I pick Rock'
    if inp == 'Rock':
        print 'Shoot again'
    elif inp == 'Paper':
        print 'Paper covers rock, I lose'
    elif inp == 'Scissor':
        print 'Rock crushes paper, you lose!'
    elif inp == 'Lizard':
        print 'Rock crushes lizard, you lose!'
    else:
        print 'Spock vaporizes Rock, I lose!'

elif pick < 200:
    print 'I pick paper'
    if inp == 'Rock':
        print 'Paper covers Rock, you lose!'
    elif inp == 'Paper':
        print 'Shoot again'
    elif inp == 'Scissor':
        print 'Scissor cuts paper, I lose!'
    elif inp == 'Lizard':
        print 'Lizard eats paper, I lose!'
    else:
        print 'Paper disproves Spock, You lose!'

elif pick < 300:
    print 'I pick scissor'
    if inp == 'Rock':
        print 'Rock, as it always has, crushes scissor. I lose!'
    elif inp == 'Paper':
        print 'Scissor cuts Paper, you lose!'
    elif inp == 'Scissor':
        print 'Shoot again'
    elif inp == 'Lizard':
        print 'Scissors decapitates Lizard, you lose!'
    else:
        print 'Spock smashes Scissors'
elif pick < 400:
    print 'I pick spock'
    if inp == 'Rock':
        print 'Spock Vaporizes Rock, you lose!'
    elif inp ==  'Paper':
        print 'Paper disproves Spock, I lose!'
    elif inp == 'Scissor':
        print 'Spock smashes Scissors, you lose!'
    elif inp == 'Lizard':
        print'Spock decapitates Lizard, you lose!'
        
    else:
        print 'Shoot again'
            

elif inp == 'Spock':
    print 'I pick lizard'
    if inp == 'Rock':
        print 'Rock crushes lizard, I lose!'
    elif inp ==  'Paper':
        print 'Lizard eats Paper, you lose!'
    elif inp == 'Scissor':
        print 'Scissor decapitates Lizard, I lose!'
    elif inp == 'Lizard':
        print 'Shoot again!'
    else:
        print 'Lizard poisons Spock, you lose!'


    


    
