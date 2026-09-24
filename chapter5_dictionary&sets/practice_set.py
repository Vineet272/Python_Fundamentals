#1 dictionary with hindi words and ther meaning.
# dic = {"khelna":"play",
#        "sona":"sleep",
#        "nahana":"bathing"}

# word = input("Enter your word:")
# print(dic[word]) 

#2 take 8 numbers from user and display all uniqe numbers
# numset = set()
# num1 = int(input("Enter number:"))
# numset.add(num1)
# num2 = int(input("Enter number:"))
# numset.add(num2)
# num3 = int(input("Enter number:"))
# numset.add(num3)
# num4 = int(input("Enter number:"))
# numset.add(num4)
# num5 = int(input("Enter number:"))
# numset.add(num5)
# num6 = int(input("Enter number:"))
# numset.add(num6)
# num7= int(input("Enter number:"))
# numset.add(num7)
# num8 = int(input("Enter number:"))
# numset.add(num8)

# print(numset)

#empty dictionary with user input key and values
fav_lang = {}
name = input("Enter name:")
lang = input("Enter favourite language:")
fav_lang.update({name:lang})
name = input("Enter name:")
lang = input("Enter favourite language:")
fav_lang.update({name:lang})
print(fav_lang)