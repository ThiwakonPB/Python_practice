print('Hello and welcome to the world of Goblin slaying')
print('What is your name?')
name = input()
def naming(name):
    print('You entered "DipShit" Is this correct?')
    print('1:Yes 2:No')
    answer = input()
    try:
        answer = int(answer)
        if answer is 1 :
            print(name + ' Is officially called DipShit from now on')
            name = 'Dipshit'
        elif answer is 2: 
            print('Alright DipShit, Welcome to the world of Goblin Slaying')
    except ValueError:
            print('You Dipshit, I said enter 1 for yes and 2 for no. Try Again!!')
            return naming(name)
naming(name)
print(name + ' Starts off in a town know as The Helmlet, You decided to get room for the night at the tavern')
print('Arriving at the town')
print('Stap, press any to exit')


class human : 
    def stats(self,atk,deff,spd,matk)
