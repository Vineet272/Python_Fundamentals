#1 
# def greatest_num(num1, num2, num3):
#     if(num1>num2 and num1>num3):
#         return num1
#     elif(num2>num1 and num2>num3):
#         return num2
#     else:
#         return num3

# result = greatest_num(2,444,88)
# print(result)

#2
def sum_n(n):
    if(n==1):
        return 1
    return n+sum_n(n-1)

print(sum_n(48))