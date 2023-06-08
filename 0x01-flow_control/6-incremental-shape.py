while True:

    try:

        num = int(input("Type a number: "))

    except ValueError:

        print("Only integer character is allowed, try again")

        continue

    break

for k in range(num):

    print("*" * space * (k+1))
