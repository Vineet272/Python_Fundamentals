#in this we are seeing different inbuilt functions of strings
# imp : all of these functions are case-sensitive.

# 1.len() find the length
str = "Hello world"
# length = len(str)
# print(length)

# # 2. startswith() verify if the string starts with given keyword or not
# start = str.startswith("He")
# print(start)

# # 3. endswith()
# end = str.endswith("world")
# print(end)

# # 4. count() to find occurence of any character in a string
# occurence = str.count("c")
# print(occurence)

# # 5. find() returns the indedx of any character in a string
# index = str.find("llo")
# print(index)

# # 6. replace()
# str = str.replace("llo", "olo")
# print(str)

#strip() to remove whitespaces
str2 = " hello "
new_str2 = str2.strip()
print(new_str2)

#split() convert to list
words = str.split()
print(words)

#join() opposite of split
words1 = ['an', 'apple', 'a', 'day']
result_str = "-".join(words1)           # "-" is the delimiter
print(result_str)



# problems for later practice
# s = "  Python Programming is Awesome  "

# Practice:

# Find length
# Remove spaces
# Convert to lowercase
# Convert to uppercase
# Count "o"
# Find "Programming"
# Check whether "Python" exists
# Replace "Awesome" with "Powerful"
# Split into words
# Join the words with -
# Check whether it starts with "Python"
# Check whether it ends with "Awesome"
# Reverse the string
# Extract "Python" using slicing
# Check whether a given string is a palindrome
