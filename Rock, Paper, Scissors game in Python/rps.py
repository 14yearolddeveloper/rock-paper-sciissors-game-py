n1 = input("Player1 enter your name: ")
n2 = input("Player2 enter your name: ")

print(n1, end=' choose your action: ')
p1 = input()

print('\n' * 1000)

print(n2, end=' choose your action: ')
p2 = input()

if (p1 == "rock" and p2 == "paper"):
  print(n2, "wins")

elif (p1 == "paper" and p2 == "scissors"):
  print(n2, "wins")

elif (p1 == "scissors" and p2 == "rock"):
  print(n2, "wins")

if (p2 == "rock" and p1 == "paper"):
  print(n1, "wins")

elif (p2 == "paper" and p1 == "scissors"):
  print(n1, "wins")

elif (p2 == "scissors" and p1 == "rock"):
  print(n1, "wins")

elif (p1 == "rock"):
  print()
elif (p2 == "rock"):
  print("It's a draw")

elif (p1 == "paper"):
  print()
elif (p2 == "paper"):
  print("It's a draw")

elif (p1 == "scissors"):
  print()
elif (p2 == "scissors"):

  print("It's a draw")

else:
  print("Action is not valid")