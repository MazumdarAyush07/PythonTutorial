"""
@author: Ayush Mazumdar
This is a tutorial file
"""
friends = ["Kevin","Karen","Jim", "Jim", "Oscar","Toby"]

print(friends) #printing the list
print(friends[4])#accesing elements according to index
print(friends[1:3])#accessing a range of elements from list
friends[1] = "Pam" #changing an element in the list
print(friends[1])

lucky_numbers = [4,8,15,16,23,42]
friends.append("Creed") #adding an element to the end of the list
print(friends) #printing the list
friends.insert(1,"Kelly") #adding elements at a particular position
print(friends)
friends.remove("Oscar") #deleting a particular element
print(friends)
friends.pop() #pop an element from the list
print(friends)
print(friends.index("Kevin")) #checks the index of the given argument in the list
print(friends.count("Jim")) #count the number of arguments
friends.sort() #sorts the elements of the list
print(friends)
friends2 = friends.copy()
print(friends2)

friends.extend(lucky_numbers) #concatenating two lists
print(friends) #printing the list

friends.clear() #clear the entire list
print(friends)