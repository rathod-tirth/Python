# Food bill task: create a food menu with functions

'''
    - create a food menu
    - ask user for order
    - ask user for no. of order
    - calcutate the total amount
    - ask user for another order
    - repeat the above process untill user say so
    - provide user with total bill
'''

status=True

menu={1:{"name":"Pizza", "price":100},
      2:{"name":"Burger", "price":80},
      3:{"name":"Pani-Puri", "price":20},
      4:{"name":"Dosa", "price":40}}

total=0

def subtotal(total,quantity):
    total=total+(quantity*menu[order]['price'])

    return total

while(status):
    print(f"""\n\n========== Fast-Food Menu ==========

        No.	Food		Price
    
        1	{menu[1]['name']}		{menu[1]['price']}/-
        2	{menu[2]['name']}		{menu[2]['price']}/-
        3	{menu[3]['name']}	{menu[3]['price']}/-
        4	{menu[4]['name']}		{menu[4]['price']}/-
                
    """)

    order=int(input("Enter your order no: "))
    quantity=int(input("Enter how many? "))

    if (order<=len(menu)):
        print(f"\nYour order: {quantity} x {menu[order]['name']}")
        
        total=subtotal(total,quantity)
        print("Your Total Bill:",total)

    else:
        print("\n-- Incorrect Order no --")
        continue

    more=input("\nDo you want anything else? [y/n]: ")

    if(more=='y' or more=='Y'):
        status=True
    else:
        status=False
        print("\nThank you for visiting")
        print("Your Total Bill:",total)




'''
    Explanation
'''




















