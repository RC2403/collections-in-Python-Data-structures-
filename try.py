# 1) summ of all the elements in a list
#2) multiply all the items in list- 20,50,60,80,90
#3) remove duplicates from the list  -10,10,10,45,67,80,100
#4)create a list of squares of all elements in a list
#5) reverse a list - [600,700,800,900,100]
#6) concatenate two list index - wise ['i', 'from']-1st index
#2nd index - ['am','chennai']- i am from chennai
#7) tuples -swap 2 tuples
#8)program to convert a list to tuple and vice versa
#9)tuples slicing [start,end,step size]
#10)sets - find common elements in 3 lists

#1 summ of all the elements in a list

num = [1,2,3,5,6,7,9]
total = sum(num)
print("The sum of numbers are :", total)

#2  multiply all the items in list- 20,50,60,80,90

list = [20,50,60,80,90]
product = 1
for i in list:
    product*= i
print("The product of numbers are :", product)


#3 remove duplicates from the list  -10,10,10,45,67,80,100

num = [-10,10,10,45,67,80,100]
remove_duplicate = set(num)
print("The number after removing duplicates are:",remove_duplicate)

#4 create a list of squares of all elements in a list

list = [1,2,3,4]
squares = [i**2 for i in list]
print("The square of numbers are:",squares)

#5 reverse a list - [600,700,800,900,100]

list = [600,700,800,900,100]
slicing = list [::-1]
print("the reverse numbers are:", slicing)


#6 concatenate two list index - wise ['i', 'from']-1st index
list1 = ['i', 'from']
list2 = ['am','chennai']
final = list1+list2
print("the concated string is:", final)
#7#7) tuples -swap 2 tuples

tuple1 = (1,2,3)
tuple2 = (4,5,6)
tuple1,tuple2 = tuple2,tuple1
print("the swapped tuples are:",tuple1)
print("the swapped tuples are:",tuple2)


#8)program to convert a list to tuple and vice versa

list = [1,2,3]
solution = tuple(list)

print("the tuple is:", solution)

#9)tuples slicing [start,end,step size]
tuple = (10,20,30,40,50,60,70,80,90,100)
slice_tuple = tuple[::4]
print("The sliced elements are:",slice_tuple)
#10)sets - find common elements in 3 lists
list1 = [1,2,3,4,5,6]
list2 = [4,5,6,8,9]
list3 = [5,6,7,8,4]
set1 = set(list1)
set2 = set(list2)
set3 = set(list3)
common = set1.intersection(set2,set3)
print("The common list are:",common)







