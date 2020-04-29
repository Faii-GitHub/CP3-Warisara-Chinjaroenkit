PorkPrice = 75
EggsPrice = 43
OrangeJuicePrice = 52
Username = input("Please Input UserName:")
Password = input("Please Input Password:")
if Username == "admin" and Password == "1234":
    print("Log in Success!!")
    print("-------------------------------------------")
    print("        Welcome to FF Supermarket ")
    print(" This is a program for price Calculating ")
    print("-------------------------------------------")
    print("The Goods List:")
    print("1. Minced Pork Pack 200 g. | Price",PorkPrice,"THB")
    print("2. Dozen of Eggs           | Price",EggsPrice,"THB")
    print("3. Orange Juice            | Price",OrangeJuicePrice,"THB")
    print("-------------------------------------------")
    UserSelected = int(input("Select Goods (1,2,3)>>"))
    if UserSelected == 1:
        print("Goods: Minced Pork Pack 200 g.")
        NumberOfGoods = int(input("How many pieces do you want (1,2,3,...)>>"))
        print("-------------------------------------------")
        print("Total Price is",PorkPrice*NumberOfGoods,"THB")
        print("-------------------------------------------")
    elif UserSelected == 2:
        print("Goods: Dozen of Eggs")
        NumberOfGoods = int(input("How many pieces do you want (1,2,3,...)>>"))
        print("-------------------------------------------")
        print("Total Price is", EggsPrice * NumberOfGoods, "THB")
        print("-------------------------------------------")
    elif UserSelected == 3:
        print("Goods: Orange Juice")
        NumberOfGoods = int(input("How many pieces do you want (1,2,3,...)>>"))
        print("-------------------------------------------")
        print("Total Price is", OrangeJuicePrice * NumberOfGoods, "THB")
        print("-------------------------------------------")
    else:
        print("Wrong Input The Goods List Number")
else:
    print("Error: Wrong UserName/Password!!")