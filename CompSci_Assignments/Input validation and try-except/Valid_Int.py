while True:
    num = input("Enter an int value. ")
    try:
        print("Final answer:", int(num))
        break
    except:
        try:
            float(num)
            print("This is a float value, not an int value.")
        except:
            print("Not a valid number.")
