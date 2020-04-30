def vatCal(Price):
    TotalPrice = Price+(Price*7/100)
    return TotalPrice

Price = float(input("Input Product Price:"))
print(vatCal(Price))