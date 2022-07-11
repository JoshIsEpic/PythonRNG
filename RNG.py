import random

while True:
    num2 = input ('Enter RNG for ending number: ')
    
    try:
        int(num2)
        it_is = random.randint(0,int(num2))
    except ValueError:
        it_is = 'Enter an integer and try again!'
    
    print(it_is)    

