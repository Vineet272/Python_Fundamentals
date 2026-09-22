#sets are collection of unordered, unchangeable, and unindexed objects.

# way to create a set is similar to dictionary creation
# set1 = {2,3,4,"Vineet", True, 1.55, "hello", 33, 2.89}
# print(type(set1))
# print(set2) 

#example 
# set2 = {1,True,0,False} #it will only print 0 and 1 because 1 and True are same and 0 nad Flase are same and set doesnt support duplicate values
# print(set2)

#how to create an empty set.
# set3 = set()

# PROPERTIES OF SETS

# how to add and remove elements from a set
# set3.add(1)
# set3.add("hello")
# set3.add(2.11)
# print(set3)

# set3.remove(2.11)  #gives key eroor if element is not present
#set3.discard(2.11)  #similar to remove() but it will not return error and return the remaining set()

# set3.pop() delets any random object of set
# print(set3)

#len to return the length 
# print(len(s3))

#clear to empty the set
# s3.clear()
# print(s3)

#union returns all the values present in boths sets
s1 = {1,2,4}
s2 = {2,3,5,4}
# s3 = s1.union(s2)
# print(s3)

#intersection returns only the values which are present in both sets
# s3 = s1.intersection(s2)
# print(s3)

#difference jo set1 me hai but set2 me nhi hai.
# s3 = s1.difference(s2)
# s3 = s1-s2   #shortcut
# print(s3)

a= {1,2}
b= {1,4,2,3}
#issubset()  a ke sare elements b mein hai.
print(a.issubset(b))

#issuperset # does a contains all elements of b
print(a.issuperset(b))

#isdisjoint check dono sets me koi common element nhi hai
print(a.isdisjoint(b))

