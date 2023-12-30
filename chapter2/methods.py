name = "carlos bravo"
print(name.title())
print(name.lower())
print(name.upper())
first_name = "lucas"
last_name = "bravo"
#passing variables to message with f
print(f"{first_name} {last_name}")
full_name = f"Hello! {first_name.title()} {last_name.title()}"
print(full_name)
#another exmaple a bit more complex
karina_first_name = "karina"
karina_last_name = "alvarez"
karina_full_name = f"{karina_first_name} {karina_last_name}"
print(f"The mother of my children is {karina_full_name.title()}.")
#adding white space to string with tabs on new lines
#To add tab \t
print("python with no tab")
print("\tpython with tab")
#to add a new line \n
print("python with no new lines")
print("Python \nwith \nnew \nLines")
#Both at once
print("Operating systems\n\tWindows\n\tmacOS\n\tLinux")
#Removing white space
#you can remove white space with rstrip for example
favorite_language = "python "
print(f"My favorite language is {favorite_language}")
#with rstrip - cant see it because is not being ran on the terminal directly but as a program.
print(f"My favorite language is {favorite_language.rstrip()}")
#If you ask for the value of python again, it will come with white space.
#You need to assig the rstrip value to the same variable to replace it in code.
favorite_language = favorite_language.rstrip()
#now this will return without white space on the right lstrip for the left. :P

#Reflixes
the_url = "http://thewebsite.info"
print(the_url)
#Removing the prefix
the_url = the_url.removeprefix("http://")
print(the_url)