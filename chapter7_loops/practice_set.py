#1 table of given number
# num = int(input("Enter the number: "))

# print(f"table of {num}: ")
# for i in range(1,11):
#     print(f"{num}X{i} = {num*i}")
# i=1
# while(i<=10):
#     print(f"{num}X{i} = {num*i}")
#     i+=1

#2 greet all the names with starting with S
# names = ["Vineet", "Sakhshi", "Sameer", "Harsh", "Shiva"]

# for i in names:
#     temp = i
#     if(temp[0] == "S"):
#         print(f"Hello {i}")

#3 prime number 
# num = int(input("Enter the number: "))

# if(num ==1 or num ==2 or num == 3):
#     print("It is a prime number")
# else:
#     i=2
#     prime = False
#     while(i<num):
#         if(num%i == 0):
#             prime = False
#             break
#         prime = True
#         i+=1

#     if(prime):
#         print(f"{num} is a prime number")
#     else:
#         print(f"{num} is not a prime number")

#pattern 
# n = int(input("Enter the value of n: "))
n=6

# 1st pattern
# i=1
# while(i<=n):
#     j=1
#     while(j<=i):
#         print("*", end="")
#         j+=1
#     print()
#     i+=1
# print()

# #2nd pattern 2*i+1
# i=0
# while(i<n): 
#     j=0
#     k=0
#     while(k<(n-(i+1))):
#         print(" ", end="")
#         k+=1

#     while(j< (2*i+1)):
#         print("*", end="")
#         j+=1
#     print()
#     i+=1

#3rd pattern
# i=0
# while(i<n):
#     j=0
#     if(i==0 or i == n-1):
#         while(j<n):
#             print("*", end="")
#             j+=1
#     else:
#         while(j<n):
#             if(j==0 or j== n-1):
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#             j+=1
#     i+=1
#     print()

for i in range(0,n):
    if(i==0 or i==n-1):
        print("*"*n,end="")
    else:
        print("*", end="")
        print(" "*(n-2),end="")
        print("*", end="")
    print()
    i+=1
    