#python - tuples
#ordered elements(display in i/p and o/p)
#allows duplicate
#immutable data- #tuples cannot be modified

"""
important_data = ("chennai","mumbai","kolkata",123)
print(important_data)
important_data[1] = "usa"
perint(important_data) # immutable
"""

"""
rand_num = (100,200,300,400)
print(rand_num)
print(type(rand_num))
"""

##access tuples elements
"""
print(important_data[2])
"""
#len() - bulit in function
important_data = ("chennai","mumbai","kolkata",123)
print(len(important_data))

#iterate through a tuples
for i in important_data:
    print(i)

#tuple method - count()  and index()

total = important_data.count("chennai")
print(total)

index = important_data.index("kolkata")
print(index)

important_data.reverse()
print(important_data)
