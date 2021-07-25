import sys
import random

# to tun this prog type in terminal: python 8_modules/random_game.py val1(degits) val2
sys.argv  # after python keyword in terminal will be stored in sys.argv as list that includes path so we have use from index 1 nstead of 0

rand = random.randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    val = int(input(f"Enter your guess of {sys.argv[1]}~{sys.argv[2]}: "))
    if val == rand:
        print('You are Genius')
        break
    else:
        continue
