import random

print('Welcome to Ludo game')

pick = {'toss','quit'}
while True:
  R1 = random.randint(1,6)
  R2 = random.randint(1,6)
  name=input("Enter toss / quit: ")
  if name not in pick:
    print("==Invalid input==")
  else:
    if name == "toss":
        print("You've tossed", R1, ":", R2)
    elif name == "quit":
        exit("Goodbye")
