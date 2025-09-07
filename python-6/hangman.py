import random
guesses = ''
turns = 5
player=input("your nicname: ")
print(f"hangman game.\nyou have 5 turns {player}!")

words = ["sushi","fairy","laser","pixel","dance","flute","ghost","jelly","knife","pearl"]

rnd_word =words[random.randint(0,len(words)-1)] 

print("guess the letters.")

while turns>0:
    failed=0
    for letter in rnd_word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
            failed+=1

    guess = input("\nguess a letter: ").lower()

    if guess in guesses:
        print("you've already guessed that letter!")
        continue

    if guess not in rnd_word and ('a' <= guess <= 'z') and len(guess) == 1 :
        turns -= 1
        print("wrong!\nyou have", turns, "more guesses")

    if failed==0:
        print(f"you win!{player}, the word is {rnd_word}")
        break
    
    if turns == 0:
        print(f"you Lose. the word was: {rnd_word}")
    
    if len(guess) != 1 or not ('a' <= guess <= 'z'):
        print("wrong input! write a single letter!")
        continue

    guesses += guess