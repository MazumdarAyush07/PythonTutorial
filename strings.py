"""
@author: Ayush Mazumdar
This is a tutorial file
"""
print("Giraffe Academy")
print("Giraffe\nAcademy")
print("Giraffe\"Academy")
print("Giraffe\\Academy")
phrase = "Manchester United"

print(phrase + " is cool") #Concatenation
print(phrase.lower()) #convert to lower case
print(phrase.upper()) #convert to upper case
print(phrase.isupper()) #check if upper case
print(phrase.upper().isupper()) #consecutive functions
print(len(phrase)) #find the length of string
print(phrase[5]) #find the character at specific position
print(phrase.index("a")) #find the index of character in string 
print(phrase.replace("United","City")) #replace the first parameter with second