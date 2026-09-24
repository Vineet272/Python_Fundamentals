#if else agr if cond. true to wo execute nhi to else block

age = int(input("Enter your age: "))

# if(age>=18):
#     print("You can drive")

# else:
#     print("You cannot drive")

# if we have muiltiple conditions we can use ELIF

if(age<18):
    print("driving before 18 is prohibit")

elif(age>=18 and age<=65):
    print("You can drive")

elif(age>=66 and age<=100):
    print("Your age is not fit for driving")

else:
    print("please enter a valid age")


