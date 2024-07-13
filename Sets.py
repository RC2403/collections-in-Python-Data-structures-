#set -{}
#unordered elemets
#no duplicate allowed

rand_num = {23,55,66,88,90,90}
print(rand_num)

locations = {"india","us","uk","germany","london","india"}
print(locations)


#add elements in Sets - add()
rand_num = {30,60,90,120,150}
rand_num.add(180)
print(rand_num)

#remove elements in set - discard()

rand_num.discard(30)
print(rand_num)

#update elements in set -  update() - other collection types - (lists, tuples,sets)
set1 = {"tcs","wipro","zoho","infosys"}
fang = {"apple","google","microsoft"}

set1.update(fang)
print(set1)

#len
print(len(fang))

#set mathemetics concepts - union - '&' and intersections '|'
 
set1 ={1,2,3,4,5}
set2 = {200,300,500,2}
print(set1.union(set2))
print(set1.intersection(set2))

print("using intersection symbol", set1&set2)
print("using union symbol", set1|set2)

#max() and min()
maximum = max(set1)
minimum = min(set1)
print(maximum)
print(minimum)
