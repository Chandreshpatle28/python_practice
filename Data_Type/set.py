#set is a collection of unique data. Elements of a set cannot be duplicate

#Duplicate items in a set
num = {3,5,6,7,8,9,3,5,1}
print(num) #{1, 3, 5, 6, 7, 8, 9}

#add and update set items
#using add() method
num.add(24)
print(num)

#using update() method
ages = [99,55,66,22]
num.update(ages)
#adds all the elements from list to num
print(num)