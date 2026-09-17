#dictio0nary in python stores data in key value pair form
# we can't have duplicate keys not values
marks = {"maths":89,
         "english":95,
         "physics": 88,
         "chemistry": 92
         }

# print(type(marks))
# print(marks)
# print(marks["english"])   #we can also write the key directly it will return its value


# Methods of dictionary

#1st: print(marks.items()) # return all the items present (key + value)

#2nd: print(marks.keys())  # return all the keys

#3rd: print(marks.values()) # return all the values

#4th update() to updates existing value and if not present insert in end
# marks.update({"maths":91, "hindi":97})  
 
#5th: .get() returns the value of specified key, will not throw error if key is missing like marks["english"]
# print(marks.get("english"))
# print(marks.get("sanskrit"))  # no error, returns none

#6th: .copy() creates a shallow copy of dic.

#7th: .clear() empties the whole dictionary

#8th: .pop() remove key and return its value, error if key is missing
# marks.pop("physics")

#9th: .popitem()  removes and return last key-value pair as tuple
# print(marks.popitem())
print(marks)
