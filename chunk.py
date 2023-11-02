""" Find the odd and
even number without using 
% (modulo) Operator """
number = int(input("Enter number  "))
answer = int(number/2)

if(answer*2 == number):
    print("Even")
else:
    print("Odd")


