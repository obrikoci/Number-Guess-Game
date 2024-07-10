#Number Guessing Game Objectives:

from random import randint
from art import logo
EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5
answer = randint(1, 100)

def check_lives(attempts):
  if attempts == 0:
    print(f"You're out of guesses. The answer was {answer}.")
    exit()
  else:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    check_answer(guess, answer, attempts)

def check_answer(guess, answer, attempts):
  if guess > answer:
    print(f"Too high.")
    check_lives(attempts - 1)
    return attempts - 1
  elif guess < answer:
    print(f"Too low.")
    check_lives(attempts - 1)
    return attempts - 1
  elif guess == answer:
    print(f"You got it! The answer was {answer}.")
    exit()
    
def level_difficulty():
  choice = input("Choose a difficulty. Type 'easy' or 'hard':\n")
  if choice == "easy":
    return EASY_ATTEMPTS
  elif choice == "hard":
    return HARD_ATTEMPTS

def game():
  print(logo)
  print("Welcome to Guess the Number Game!\nI'm thinking of a number between 1 and 100. Try and guess which one it is.")
  attempts = level_difficulty()
  guess = 0
  while guess != answer:
    print(f"You have {attempts} attempts in total to guess the number.")
    guess = int(input("Make a guess: "))
    check_answer(guess, answer, attempts)

game()
  