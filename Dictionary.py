#Dictionary  - {key:value}
#create a dictionary

my_data = {"user_id":1001, "product":"laptop","city":"chennai","user_id":1001}
print(my_data)

#elementt access
print(my_data["user_id"])
print(my_data["product"])

#add 
my_data["day"] = "sunday"
print(my_data)

#in list
"""
index(position) u can add new element in list
insert(1,"data")
list method- my_data.append()
my_data- "data"
"""

#remove dictionary elements - "del"
del my_data["city"]
print(my_data)

#update a element
my_data["user_id"] = 1005
print(my_data)

#update a product

my_data["product"] = "mobile phone"
print(my_data)
#loop iteration in dictionary
for key,value in my_data.items():
    print(key,value)
#find dictionary length

print(len(my_data))

#dictionary methods
#pop()
"""
my_data.pop('day')
print(my_data)
"""
new_data = my_data.pop('day')
print("element remove:",new_data)
print(my_data)

#clear()- removes all elements in the dictionary
"""my_data.clear()
print(my_data)"""

dictkeys = my_data.keys()
print(dictkeys)

dictvalues = my_data.values()
print(dictvalues)

#copy() - returns a shallow copy

copydatas = my_data.copy()
print("original data", my_data)
print("copydatas", my_data)

#memebership operator -  in and not in
languages=["tamil","malayalam","english"]
print("hindi" in languages)


format ={".txt" : "text format",
         ".mp3"  :"audio format",
         ".mp4":"video format"}
print(".txt" in format)
# identity operators - is and is not
"""
x = 10
y=10
print(id(x))
print(id(y))
print(x is y)
"""
"""
list1=[1,2,3]
list2=[1,2,3]
print(id(list1))
print(id(list2))
print(list1 is list2)
"""
#list
"""
1) create a list of movies and print the list
2)add a new movie to the list and print
3)remove the first movie from the list and print the updated list 
4)sort the list of movies in alphabetical order and print it
5) count the number of movies in the list
"""

movies = ["harrypotter","up","nemo","narnia","minions"]
print(movies)

movies.append("avengers")
print(movies)

movies.pop(0)
print(movies)

movies.sort()
print(movies)

movies.sort(reverse=False)
print(movies)

print(len(movies))

###tuples
"""
1)craete a tuple with some colors and print it
2)access and print 1st and last element in the tuple
3)try changing one of the elements in the tuple and observe what happens
4)convert the tuple to a list, add a new color, and convert it back to tuple
"""

colors = ("red","blue","green","lila")
print(colors)
print(type(colors))

print(colors[0])
print(colors[-1])

"""colors[1]="black"
print(colors)
"""

colors_update = list(colors)
colors_update.append("grey")
colors = tuple(colors_update)
print(colors)


###sets:

"""
1)create a set of fruits and print it
2)add a new fruit to the set and print the update set
3)remove a fruit from the set and print the updated set
4)check if specific fruit is in the set
5)create a another set of fruit and find the union and interesction of both
"""

set = {"apple", "banana","orange","grapes"}
print(set)
print(type(set))

set.add("watermelon")
print(set)

set.discard("orange")
print(set)

print("apple" in set)

print("fruit data:",set)
fruits={"apple","mango","grapes","banana"}
print("another fruit data:",fruits)
print(set.union(fruits))
print(set.intersection(fruits))












