###dictionary
"""
1)create a dictionary with information about a person(name,age,city) and print it
2)add a new key value pair for the person's job and print the updated dictionary
3)update the person's age and print the updated dictionary
4)remove the person's city from the dictionary and print the updated dictionary
5)loop through the dictionary and print each key and value 

"""


dict = {"name":"AKA","age":20,"city":"chennai"}
print(dict)


dict["job"] = "teacher"
print(dict)

dict["age"] = 25
print(dict)

del dict["city"]
print(dict)

for key,value in dict.items():
    print(key,value)
