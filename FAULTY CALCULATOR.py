# DESIGN A CALCULATOR WHICH WILL SOLVE ALL THE CALCULATIONS CORRECTLY EXCEPT THE FOLLOWING 3 CALCULATION
# 45*5 = 555 , 56+9 = 77, 56/6=4
# PROGRAM SHOULD TAKE OPERATOR AND THE TWO NUMBERS AS INPUT FROM THE USER AND THEN RETURN THE RESULT
print("Enter operator of the task")
operator = input()
print("Enter first number")
n1 = int(input())
print("Enter second number")
n2 = int(input())
print("your task is")
if n1 == 56 or n1 ==9 and n2 == 9 or n2==56 and operator == "+":
    print("the sum is 77")
elif operator== "+":
    print("YOUR answer is", int(n1) + int(n2))
elif n1==45 or n1 == 5 and n2== 5 or n2==45 and operator == "*":
    print("THE PRODUCT IS 555")
elif operator =="*":
    print("THE PRODUCT IS", int(n1) * int(n2))
elif n1 == 56 and n2 == 6 and operator == "/":
    print("The quotient is 4")
else:
    print("THE QU0TIENT IS",int(n1) / int(n2))