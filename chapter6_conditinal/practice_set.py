#1. to find the greatest number among 4 numbers entered by users.
# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
# num3 = int(input("Enter 3rd number: "))
# num4 = int(input("Enter 4th number: "))

# if(num1>num2 and num1>num3 and num1>num4):
#     print("1st number is greatest")
# elif(num2>num1 and num2>num3 and num2>num4):
#     print("2nd number is greatest")
# elif(num3>num1 and num3>num2 and num3>num4):
#     print("3rd number is greatest")
# else:
#     print("4th number is greatest")

#2nd problem pass/fail min 33% in each subject and 40% total
# sub1 = int(input("Enter maths marks out of 100: "))
# sub2 = int(input("Enter physics marks out of 100: "))
# sub3 = int(input("Enter chemistry mark sout of 100: "))
# total = sub1+sub2+sub3

# if(sub1>=33 and sub2>=33 and sub3>=33 and total>=40):
#     print("PASS")
# else:
#     print("FAIL")

#3rd spam filter
# keyword = input("enter key word: ")

# if(keyword == "buy now" or keyword == "win money"):
#     print("SPAM alert")

# else:
#     print("Not a spam")

#4th valid username length or not
# username = input("Enter username: ")
# name_len = len(username)

# if(name_len<= 0):
#     print("Username length cannot be zero or negative")
# elif(name_len>0 and name_len<=10):
#     print("Valid username length")
# else:
#     print("Username length cannot be more than 10 characters")

#5th name present in list or not?
namelist = ["vineet", "kanak", "harsh", "prakhar"]
name = input("Enter name: ")

if name in namelist:
    print("present")
else:
    print("not present")