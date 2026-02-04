# Part 1 - Learning about Lists
Tallest_Mountains = ["Mt. Everest", "K2", "Kangchenjunga", "Lhotse", "Makalu", "Cho Oyu"]
print (Tallest_Mountains)
ns1 = Tallest_Mountains[0:2]   
print (ns1)
ns2 = Tallest_Mountains[2:4]
print (ns2)
ns3 = Tallest_Mountains[4:6]
print (ns3)
print ("Finished")

# Part 2 - Learning about Tuples
Limited_Menu = ("Braised Short Rib", "Seared Tuna", "Wagyu Beef", "French Onion Soup", "Fig Salad", "Crème Brûlée")
print(Limited_Menu)
# Removing Items from List
menu_list = list(Limited_Menu)
menu_list.remove("Wagyu Beef")
menu_list.remove("Fig Salad")
Updated_Limited_Menu = tuple(menu_list)
print(Updated_Limited_Menu)
# Adding Items to List
updated_list = ["Duck Breast", "Lobster Tail"] + menu_list
Final_Limited_Menu = tuple(updated_list)
print(Final_Limited_Menu)