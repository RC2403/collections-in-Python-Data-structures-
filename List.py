#python- collections
"""
List -[], Tuples - (), Sets- {}, Dictionary {Key : value}
"""

#list -[] Any type of data can be given
#ordered elements
# allows duplicates
#Mutable 

places = ["chennai","mumbai","Bangalore",123, True]
print(places)
print(type(places))

#element access
print(places[2])

#how to change values in list
places[1] = "Delhi"
print(places)

#adding a new  element in list - append() method

places. append("mumbai")
print(places)

#remove an element in the list - remove
numbers = [100,200,300,400]

"""
numbers.remove(400)
print(numbers)"""

#pop() - removes last element
# can remove the element by specifying the element position
"""numbers.pop()
print(numbers)

numbers.pop(2)
print(numbers)
"""

# finding list length - len (built -in function)
print(len(numbers))

#iterating thorugh a list

languages = ["python","Java","ruby"]
for i in languages:
    print(i)

#extend () - add another list - at the end of fifrst list

userid1 = [100,200,300,400,500]
userid2 = [600,700,800,900,1000]
userid1.extend(userid2)
print(userid1)

#insert()
medium = ["linkedin","quora","Instagram"]
medium.insert(1, "twitter")
print(medium)

#reverse()
language = ["tamil","english","Malayalam"]
language.reverse()
print(language)
#print(language[::-1])#negative values gives reverse (slicing)

# count() # cannot be printed directly, temporarily variable is need to find the the count
places = ["chennai","mumbai","Bangalore","chennai"]
total = places.count("chennai")
print(total)

'''
#sort # default is ascending order
places =  ["chennai","mumbai","Bangalore","chennai"]
places.sort()
print(places)

places =  ["chennai","mumbai","Bangalore","chennai"]
places.sort(reverse= True)
print(places)
'''

#copy() - returns a shallow copy of the list
product_id = [1001,2002,4004,5000]
print("original data", product_id)
sample = product_id.copy()
print("copy data",sample)

#clear() - removes all itmes from list
product_id.clear()
print(product_id)






    

