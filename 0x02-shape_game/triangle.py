def triangle():
    try:
        angle = int(input("Please enter an odd number: "))
        if angle % 2 == 0:
            print("== Invalid, only odd numbers are allowed ==")
            triangle()
        else:
            space = 0
            for x in range(angle, 0, -2):
                print("  " * space + "* " * x)
                space = space + 1
    except ValueError:
        print("Only Odd integers are allowed")
        triangle()


triangle()
