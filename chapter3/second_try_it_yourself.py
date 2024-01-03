#Make a list of 3 people and invite them to dinner
list_of_pople_for_dinner = ["Asmongold", "Thor", "Mr.Beast" ]

#Copy the list before any modification
new_list_for_dinner = list_of_pople_for_dinner.copy()

#invitations
first_invite = new_list_for_dinner.pop()
print(f"Hi,{first_invite}, Would you like to come to dinner?")
second_invite = new_list_for_dinner.pop()
print(f"Hi, {second_invite}, it would be an honor if you came to my dinner.")
third_invite = new_list_for_dinner.pop()
print(f"Hi, {third_invite}, I have invited a few close firends, inclding you to dinner. I would love it if you can join us")
#Announcing someone can't make it.
print(f"Unfortunately {first_invite}, is unable to make it.")
#Adding someone else to the list
#copy the original list first jst in case.
new_invite_list = list_of_pople_for_dinner.copy()

#remove mr beast
new_invite_list.remove("Mr.Beast")
#append moist
new_invite_list.append("Moistcritical")
#print invite for moist
print(f"Hi, {new_invite_list[2]}, You are officialy invited to out Stremers only dinner. ")
#got a bigger table announcement
print("We have been granted a bigger table and we will be inviting 3 aditional people.")

#inserting more people to invite for the dinner
#copy the list to modify it
aditional_people_list = new_invite_list.copy()
#adding people
aditional_people_list.insert(0,"FlatB")
aditional_people_list.insert(2, "BraveAce")
aditional_people_list.append("ch33zWhiiz")

#Sending new invites
#selecting 1st spot on the list
flatb_invite = aditional_people_list[0]
print(f"Hi, {flatb_invite}, i want to invite you to out streamer dinnder.")

#second spot invite
asmongold_invite = aditional_people_list[1]
print(f"Hi, {asmongold_invite}, you are invited to streamers dinner")

#thirdspot invite
braveace_invite = aditional_people_list[2]
print(f"Hi, {braveace_invite}, you are invited to the streamer dinner")

#No space for everyone at the table after all. need to remove 2.
#copy list before modifying
smaller_table_list = aditional_people_list.copy()
guest_one_gone = smaller_table_list.pop()
print(f"Sorry {guest_one_gone}, you are no longer invited to dinner, due to unfornseen issues.")
guest_two_gone = smaller_table_list.pop()
print(f"Sorry {guest_two_gone}, you can't go, we don't have space.")
print(smaller_table_list)
#use remove to take out one more person.
remove_flatb = "FlatB"
smaller_table_list.remove(remove_flatb)
print(smaller_table_list)
del smaller_table_list[0]
print(smaller_table_list)
#sorting
list_to_sort = ["cars", "trucks", "boats", "suv", "planes"]
print(list_to_sort)
list_to_sort.sort()
print(list_to_sort)
#lengh of something
print(len(list_to_sort))
