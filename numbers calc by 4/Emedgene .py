def calc():
    sum = 0
    for i in range(101):
        if i%4 == 0:
            sum = sum + i
    
    return sum

x= calc()
print(x)

