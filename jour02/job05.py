def calcule(num1,operator,num2):
    if operator == "+":
        return num1+num2
    elif operator == "-":
        return num1-num2
    elif operator == "*":
        return num1*num2
    elif operator == "/":
        return num1/num2
    elif operator == "%":
        return num1%num2
    else :
        return ("error")
print(calcule(2,"*",3))
print(calcule(7,"/",4))
print(calcule(6,"+",4))
print(calcule(9,"-",4))
print(calcule(5,"%",4))