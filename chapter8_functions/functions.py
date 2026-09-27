#function is a group of statements to performa specific task

#function definition it always start with keyword def keyword
# def avg():
#     n1 = int(input("Enter 1st number: "))
#     n2 = int(input("Enter 2nd number: "))
#     n3 = int(input("Enter 3rd number: "))

#     result = round((n1+n2+n3)/3, 2)        #round() it is for limiting the digits after decimal place in theis it is 2 digits
#     print(f"The average is {result}")
# avg()


#functions with arguments
# def greet(name):
#     print(f"Good afternoon, {name}")
# naam = input("Enter your name: ")
# greet(naam)


#With defualt arguments:
# def greet(name="user"):
#     print(f"Good afternoon, {name}")
# greet()

#functions with return value
def avg():
    n1 = int(input("Enter 1st number: "))
    n2 = int(input("Enter 2nd number: "))
    n3 = int(input("Enter 3rd number: "))

    result = round((n1+n2+n3)/3, 2)        #round() it is for limiting the digits after decimal place in theis it is 2 digits
    return result

avrg = avg()
print(avrg)