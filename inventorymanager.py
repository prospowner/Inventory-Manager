#getting started

inventory = {}
print('---Welcome to the Inventory Manager---')

#item1

item1_name = input('Enter the name of the first item: ')
item1_qty = int(input(f'How many {item1_name} do you have? '))

inventory[item1_name] = item1_qty

#item2

item2_name = input('Enter the name of the second item: ')
item2_qty = int(input(f'How many {item2_name} do you have? '))

inventory[item2_name] = item2_qty

print('/n Items sucessfully added!')

#system for user asking for an item quantity

item_to_check = input('What item do you want to check?')

if item_to_check in inventory:
 quantity = inventory[item_to_check]
 print(f"We have {quantity} of {item_to_check} in stock.")
else:
 print('Item not present in the inventory unfortunately!')

 
#quit check or remove or quit 

print("\nWhat would you like to do next?")
print("1. Check an item quantity")
print("2. Remove an item")
print("3. Exit")

choice = input("Enter the number of your choice (1, 2, or 3): ")

if choice == "1":
    item_to_check = input('What item do you want to check? ')
    if item_to_check in inventory:
        quantity = inventory[item_to_check]
        print(f"We have {quantity} of {item_to_check} in stock.")
    else:
        print('Item is not present in the inventory sadly!')

elif choice == "2":
    item_to_remove = input('\nWhat item do you want to remove from the inventory? ')
    if item_to_remove in inventory:
        removed_qty = inventory.pop(item_to_remove) 
        print('Successful. The item has been removed enjoy.')
    else:
        print('Error. The item is not in the inventory.')
    print(f'\nUpdated Inventory : {inventory}')

elif choice == "3":
    print("Bye!")
    exit()

else:
    print("Invalid choice! Please run the program again and select 1, 2, or 3.")

