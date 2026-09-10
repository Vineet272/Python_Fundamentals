# contains exercise based on variables, operators and inoput fuctions
#first lets understand input() function

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Your name: ", name)
print("your age: ", age)

#problem 1: finding remainder
print("Num1 must be graeter then Num2")
num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))
rem = float(num1/num2)
print(num1,"/",num2,"gives remainder: ",rem)

#problem 2: greatest number between find out
num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))
great = None

if num1 > num2:
    great = num1
else: great = num2
print("The greatest number is: ", great)

#problem 3: calculating square of a number
num2= int(input("Enter the number: "))
print("The square of",num2,"is: ",(num2*num2))