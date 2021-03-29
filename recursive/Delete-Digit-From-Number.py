
def delete_Digit_From_Number(number, digit):
    number = str(number)
    digit = str(digit)
    x = delete_Digit_From_Number2(number, digit)
    finelNumber = int(x)
    return finelNumber


def delete_Digit_From_Number2(number, digit):
    if number =="":
        return 0
    if number.find(digit) == -1:
        return number
    x = number.find(digit)
    number = number[:x]+number[x+1:]
    return delete_Digit_From_Number2(number, digit)


print(delete_Digit_From_Number(123,1))
print(delete_Digit_From_Number(123,4))
print(delete_Digit_From_Number(123,3))
print(delete_Digit_From_Number(123123,1))
print(delete_Digit_From_Number(121341451,1))
print(delete_Digit_From_Number(111,1))
