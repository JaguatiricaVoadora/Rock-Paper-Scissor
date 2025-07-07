import time
import random

Plays = ["Rock", "Paper", "Scissor"]
Counters = {
    "Rock": "Paper",
    "Paper": "Scissor",
    "Scissor": "Rock"
}
Nums =  ["0","1","2","3","4","5","6","7","8","9"]

def InfiniteMode(IsScore, Inf, Per):
  GameScore = 0
  YourScore = 0
  I = 1
  if Inf and not Per:
    Inf = float('inf')
  elif not Inf and not Per:
    Inf = 10
    
  while I <= Inf:
    I+=1
    UserChoice = input(f"Type your Choice between {Plays}").capitalize()
    GameChoice = random.choice(Plays)
    
    if UserChoice not in Plays:
      print("Wrong Choice")
      InfiniteMode(IsScore, Inf, Per)
  
    print("The game is thinking....")
    time.sleep(2)
    print(f"Game choice: {GameChoice}")
    time.sleep(1)
    print(f"Your choice: {UserChoice}")
    time.sleep(1)
  
    if UserChoice == GameChoice:
      print("Tie")
      GameScore += 1 if IsScore else GameScore
      YourScore += 1 if IsScore else YourScore
    elif UserChoice in Counters[GameChoice]:
      print("You Win")
      YourScore += 1 if IsScore else YourScore
    else:
      print("You Lose")
      GameScore += 1 if IsScore else GameScore
      
    print(f"Your Score: {YourScore}" if IsScore else "")
    print(f"Game Score: {GameScore}" if IsScore else "")
      
def Main():
  print("Welcome to the Rock Paper Scissor Game")
  time.sleep(1)
  print("What mode do you want to play?")
  print("1. Infinite Mode without score system")
  print("2. Infinite Mode with score system")
  print("3. 10 rounds without scoring")
  print("4. 10 rounds with scoring")
  print("5. Customized Mode")
  Choice = int(input("Your Choice: "))
  if Choice == 1:
    InfiniteMode(False, True, False)
  elif Choice == 2:
    InfiniteMode(True, True, False)
  elif Choice == 3:
    InfiniteMode(False, False, False)
  elif Choice == 4:
    InfiniteMode(True, False, False)
  elif Choice == 5:
    Score = False
    rounds = 0
    print("How many rounds do you want?")
    print("You can say infinity to infinity rounds")
    time.sleep(1)
    Escolha = input("Here: ")
    if str(Escolha).lower() == "infinity":
      rounds = float('inf')
    elif "infinity" not in Escolha.lower() and not any(num in Escolha for num in Nums):
        print("Wrong Choice")
        Main()
    else:
      rounds = int(Escolha)
    time.sleep(1)
    print("Do you want score system?")
    time.sleep(1)
    print("1. Yes")
    time.sleep(1)
    print("2. No")
    Escolha = input("Here: ")
    if int(Escolha) == 1:
      Score = True
    
    InfiniteMode(Score, rounds, True)
  else:
    print("Invalid Choice")
    Main()
    
if __name__ == '__main__':
    # Chama a interface gráfica
    import pythongui
    pythongui.run_gui()
#TODO: SEGURANÇA NOS INPUTS