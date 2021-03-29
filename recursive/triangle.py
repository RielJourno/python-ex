def printPartten(n, k):
    if (n < 0):  # stop condition
        return

    printPartten(n - 1, k + 1)  # recursive call

    for i in range(0, k):  # makes spaces
        print(" ", end="")
    for i in range(0, n):  # for print *
        print("* ", end="")
    print("\n", end="")  # for next line



n = (int)(input("enter size of triangle: "))
printPartten(n, 0) # recursive call

ans = input("do you want again? (yes/no)\n")

while(ans == "yes"):
    n = (int)(input("enter size of triangle: "))
    printPartten(n, 0) # recursive call
    ans = input("do you want again? (yes/no)\n")
