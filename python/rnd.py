import random
print("game: you have to guess between numbers 1-100. you have 5 chances. ")
player=input("username: ")
rnd=random.randint(1,100)
chances=1
choose_num=0
while chances<=5:
    choose_num=int(input(f"{player}, choose number: "))
    chances+=1
    if choose_num>rnd:
        print("too high.")
    elif choose_num<rnd:
        print("too low.")
    else:
        print(f"match!")
        break
print(f"the random number was: {rnd}, your number:{choose_num}")
