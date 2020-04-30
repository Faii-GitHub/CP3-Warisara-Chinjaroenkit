def Login():
    Username = ""
    Password = ""
    while Username != "admin" or Password != "1234":
        Username = input("Please Input UserName:")
        Password = input("Please Input Password:")
        if Username == "admin" and Password == "1234":
            print("----------------------------")
            return Username
        else:
            print(">> Wrong UserName/Password, Please try again <<")

def ShowMenu():
    print("----------------------------")
    print("The Menu:")
    print("1. VAT Calculator")
    print("2. Price Calculator")
    print("----------------------------")

def SelectMenu():
    UserSelected = 0
    while UserSelected != 1 and UserSelected != 2:
        UserSelected = int(input("Input the number of Menu>>"))
        if UserSelected == 1 or UserSelected == 2:
            return UserSelected
        else:
            ShowMenu()
            print("Please input the correct number (1 or 2)")

def vatCal(Price):
    VAT = 7/100
    return Price + (Price * VAT)

def priceCal(FirstPrice,SecondPrice):
    return vatCal(FirstPrice+SecondPrice)

Currency = "THB"
print(">> Log in success, Hello",Login())
ShowMenu()
Menu = SelectMenu()
if Menu == 1:
    Price = float(input("Input Price of Product:"))
    print("Total Price (Include VAT):",str(vatCal(Price)),Currency)
elif Menu == 2:
    FirstPrice = float(input("Input Price for x:"))
    SecondPrice = float(input("Input Price for y:"))
    print("Total Price of x+y (Include VAT):", str(priceCal(FirstPrice,SecondPrice)),Currency)
print("---------Thank You----------")