#Message
#Use a variable to represent a person's name and print a message like "Hi, Lucas would you like to learn python today?"
message_name = "lucas"
print(f"Hi, {message_name.title()}, would you like to learn some python today?")

#Name cases
#Print a name in upper, lower and title
cases_name = "carlos"
print(cases_name.upper())
print(cases_name.lower())
print(cases_name.title())

#Famous quotes
#Find a quote and print it and the author: "This person once said this, this and that."
print('Carlos Once said "I never argue. I just explain why you are wrong."')

#Quotes 2-represent the famous person name in a variable called famous_person. 
#Compose message and represent in a variable called message and print it.
famous_person = "Dude"
famouse_person_quote = "I never argue. I just explain why you are wrong."
print(f'{famous_person} once said "{famouse_person_quote}"')

#Stip names
#user variable for someones name, include white space at the begining and the end and use \t and \n to show the space
#then remove it with rstrip, lstrip and strip
someones_name_left = " Thisdudeleft"
print(someones_name_left)
someones_name_left = someones_name_left.lstrip()
print(someones_name_left)
someones_name_right ="This dude right "
print(someones_name_right)
someones_name_right = someones_name_right.rstrip()
print(someones_name_right)

#File extension
#make a variable and assig it python.txt and use removesuffix() to remove the extension and display just the file name.
file_extension = "python.txt"
print(file_extension)
file_extension_no_sufflix = file_extension.removesuffix(".txt")
print(file_extension_no_sufflix)