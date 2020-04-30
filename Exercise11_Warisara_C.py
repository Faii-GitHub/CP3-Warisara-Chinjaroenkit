InputNum = int(input("Please Input Number:"))
for x in range(InputNum):
    print((" "*(InputNum-(x+1)))+("*"*((x*2)+1)))