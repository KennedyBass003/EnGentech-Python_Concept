import random

print('Welcome to Ludo game')

pick = {'toss','quit'}
while True:
  R1 = random.randint(0,7)
  R2 = random.randint(0,7)
  name=input("Enter toss/quit: \t")
  if name not in pick:
    print("Invalid input")
  else:
    if name == "toss":
        print(R1, ":", R2)
    elif name == "quit":
        exit("Goodbye")
