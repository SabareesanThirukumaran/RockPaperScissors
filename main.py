import random, os, time, colorama
from colorama import Fore, Back, Style
colorama.init(autoreset = True)
from replit import audio

#ellipsis
def ellipsis():
  y = 0
  t = "...\n"
  while y <= len(t):
    os.system("clear")
    print(t[:y])
    time.sleep(0.2)
    y = y + 1
  time.sleep(0.5)
    
#computer choices 
computer_choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(computer_choices)

#prizes
prizes = ["rickroll", "talking ben"]
prize = random.choice(prizes)

#victory
def victory():
  print(f'{"You Won" : >15}')
  print(Style.DIM + "Press 'enter' to view your reward...")
  reward = str(input())
  if reward == "":
    os.system("clear")
    time.sleep(0.3)
    print(Fore.GREEN + f"You won a {prize}")
    if prize == "rickroll":
      source = audio.play_file("Never-Gonna-Give-You-Up-Original.wav")
      while True:
        pass
    elif prize == "talking ben":
      ben = audio.play_file("Ben.wav")
      while True:
        pass
      
#lose
def lose():
  print(f"{'You lost!' : >15}")
  time.sleep(1)
  os.system("clear")
  print(Fore.RED + "Imagine losing, could never be me :(")
  print(" ")
  time.sleep(0.5)
  exit()

#tie
def tie():
  print(f"{'It was a tie...' : >15}")
  time.sleep(1)
  os.system("clear")
  print(Fore.GREEN + "Adios mis amigos!")
  print(" ")
  time.sleep(0.5)
  exit()
  
#rock function
def rock():
  ellipsis()
  os.system("clear")
  time.sleep(0.2)
  print(f"Computer picks {computer}")
  time.sleep(1)
  #decides whether you win or lose
  
  #lose
  if computer == "Paper":
    os.system("clear")
    ellipsis()
    time.sleep(0.5)
    os.system("clear")
    lose()
    
  #draw
  elif computer == "Rock":
    os.system("clear")
    ellipsis()
    time.sleep(0.5)
    os.system("clear")
    tie()
    
  #win
  elif computer == "Scissors":
    os.system("clear")
    ellipsis()
    time.sleep(0.5)
    os.system("clear")
    victory()

#paper function
def paper():
  ellipsis()
  os.system("clear")
  time.sleep(0.2)
  print(f"Computer picks {computer}")
  time.sleep(1)
  #decides whether you win or lose
  
  #tie
  if computer == "Paper":
    os.system("clear")
    ellipsis()
    time.sleep(0.5)
    os.system("clear")
    tie()
    
  #win
  elif computer == "Rock":
    os.system("clear")
    ellipsis()
    time.sleep(0.5)
    os.system("clear")
    victory()
    
  #lose
  elif computer == "Scissors":
    os.system("clear")
    ellipsis()
    time.sleep(0.5)
    os.system("clear")
    lose()

def scissors():
  ellipsis()
  os.system("clear")
  time.sleep(0.2)
  print(f"Computer picks {computer}")
  time.sleep(1)
  #decides whether you win or lose
  
  #win
  if computer == "Paper":
    os.system("clear")
    ellipsis()
    time.sleep(0.5)
    os.system("clear")
    victory()
    
  #lose
  elif computer == "Rock":
    os.system("clear")
    ellipsis()
    time.sleep(0.5)
    os.system("clear")
    lose()
    
  #tie
  elif computer == "Scissors":
    os.system("clear")
    ellipsis()
    time.sleep(0.5)
    os.system("clear")
    tie()

#game function
def game():
  os.system("clear")
  time.sleep(0.5)
  choice = str(input(Style.DIM + "Pick 'Rock', 'Paper' or 'Scissors' to start...: "))
  if choice.lower() == "rock":
    rock()
  elif choice.lower() == "paper":
    paper()
  elif choice.lower() == "scissors":
    scissors()

#player start
def start():
  print("---------------------------------")
  print(f"{'            - Play -             '}")
  print(f'{"            - Help -             "}')
  print(f'{"            - Quit -             "}')
  print(f'{" Copyright 2009-2022 © Aydd Inc  "}')
  print("---------------------------------")
  print(" ")
  Start = str(input(Style.DIM + "Choose 'Play' 'Help' or 'Quit', to get going: "))
  #start the rock paper scissors
  if Start.lower() == "play":
    game()
  #help menu
  elif Start.lower() == "help":
    os.system("clear")
    time.sleep(0.2)
    help()
  #turn repl offline
  elif Start.lower() == "quit":
    exit()
  #problem occured
  else:
    y = 0
    t = Fore.RED + "iT SEems ThERe IS a PRoblEM...\n"
    while y <= len(t):
      os.system("clear")
      print(t[:y])
      time.sleep(0.1)
      y += 1
    time.sleep(0.5)
    exit()

#recall start function
start()