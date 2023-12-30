cheeses = [
    "Cheddar",
    "Gouda",
    "Brie",
    "Camembert",
    "Mozzarella",
    "Parmesan",
    "Blue Cheese",
    "Feta",
    "Swiss",
    "Provolone"
    ]
print(cheeses)
print(cheeses[3])
#you can make sentences using parts of the list.
print(f"My favorite cheese is {cheeses[1].title()}")

#Modifying, adding and removing
#modifying
original_list = ["Apple", "Samsung", "Microsoft", "Amazon", "Meta"]
print(original_list)
original_list[4] = 'Facebook'
print(original_list)
#Appedig - This goes at the end of the list
appending_list = original_list
appending_list.append("Netflix")
print(appending_list)
#inserting
inserting_list = appending_list
inserting_list.insert(1,"Google")
print(inserting_list)
#Removing
removing_from_list = inserting_list.copy()
print(removing_from_list)
del removing_from_list[1]
print(removing_from_list)
#pop - This also removes from the list
poped_list = removing_from_list.copy()
new_poped_list = poped_list.pop()
print(new_poped_list)
selected_pop_list = poped_list.pop(2)
print(selected_pop_list)
#remove - You can use this when you know the value but not the position of what you want removed
removed_from_list = poped_list.copy()
take_out_with_remove = removed_from_list
i_want_out = "Facebook"
take_out_with_remove.remove(i_want_out)
print(f"I don't like {i_want_out} so i took it out.")
