#ways to create strings:
a = 'vineet'  #single quotes
b = "vinit"   #double quotes
c = '''veenit''' #triple quotes

# print(a)
# print(b)
# print(c)


#index always start from 0 and ends at (len-1).
#string slicing (taking parts of string)
str = "hello world" 
slice1 = str[6]
# print(slice1)

slice2 = str[:4]   #last index is excludes i.e., slice2 have 0-3 "hell"
# print(slice2)

slice3 = str[1:4]   #starting index is included i.e., slice3 have 1-3 "ell"
# print(slice3)

c = str[6:]  #c will hold everything from 6th index to last index
# print(c)

#slicing with skip value
word = "amazing"
str1 = word[1:6:2]
print(str1)

num = "0123456789"
str2 = num[1:8:3]
print(str2)

