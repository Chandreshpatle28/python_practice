#Python list
#list are used to store multiple data at once

#Create a List
ages = [24, 25, 38]
print(ages) #[24, 25, 38]
print(ages [1]) #25

#list with elements of different data types
list = [25, "Chandresh", 7.8]
#List can contain any type of variable
print(list) #[25, 'Chandresh', 7.8]

#Access List Elements
subject = ["Maths", "Histroy", "Chemistry"]
#create the subject list and assign values in it using square brackets
print(subject[1]) #History
print(subject[0]) #Maths

#Negative Indexing in python
#starts from -1 not zero
#print(subject[-1]) #Chemistry

#Slicing Lists
#syntax: my_list[start : end + 1 ]
new_list = ['a','b','c','d','e','f','g']
#print all items starting form index number 2 till last item
#print(new_list[2:]) #'c' , 'd' ,'e','f' ,'g'
#print all items starting form index number 1 to index number 4
#print(new_list[1:4]) #'b' , 'c' ,'d'

#Add Element of a list
#list are mutable {changeable}. We can add and remove elements from a list.

#using append() 
#append method adds an item at the end of the list.
#print("Before Append: ", ages) #[24, 25, 38]
ages.append(60)
#print("After Append: ", ages) #[24, 25, 38, 60]

#Using insert() Method
#insert an element at index 2 (third position)
ages.insert(2, 94)
#print('After Insert:', ages ) #After Insert: [24, 25, 94, 38, 60]

#using extend()
#extend is similar as append but we pass another list into this function which will be added after existing
new_ages = [7,9,4]
ages.extend(new_ages)
#print ("After Extend:", ages) #After Extend: [24, 25, 94, 38, 60, 7, 9, 4]

#Remove Item From A List Using Remove Function
#remove removes first matching value if there exists more than one match then only first matched value gets removed

#using del 
del subject[0]
#print(subject) #['Histroy', 'Chemistry']

#using remove()
ages.remove(9)
print(ages)


