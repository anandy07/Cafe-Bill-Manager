# Cafe Menu

menu = {
    'Pizza': 120,
    'Pasta': 50,
    'Burger': 80,
    'Salad': 40,
    'Coffee': 25,
    'Andy' : 0.2,  # Discount coupon
    
}





# Welcome
print("🍽️ Welcome to our Restaurant! Here is our menu:\n")




# Menu List 

for item,price in menu.items():
    if item != "Andy" :  # Exclude Coupon
        print(f"{item} : ${price}")




# Order System

order_list = []
total_bill = 0

while True:
    order = input("\nWhat would you like to order? ").strip().title()

    if order in menu:
        order_list.append(order)
        total_bill+=menu[order]
    else:
        print("⚠️ Item not found! Please choose from the menu.")   
        continue

    more = input("Would you like to order more? (Yes/No) ").strip().lower()

    if more == 'no' :
        break




# Restriction: User cannot order just Coffee

if order_list == ["Coffee"]:
    print("⚠️ Sorry, you cannot order only Coffee. Please add another item.")

else:
    # Apply Coupon Discount
    coupon_code = input("\nDo you have a coupon code? (Enter code or 'No') ").strip().title()
    if coupon_code == "Andy":
        discount = total_bill * menu['Andy']
        total_bill -= discount
        print(f"✅ Coupon applied! You saved ${discount}")




# Display Bill Summary

print("\n🧾 Order Summary:")

for item in order_list:
    print(f"- {item}: ${menu[item]}")


print(f"\n💰 Total Bill: ${total_bill}")
print("\n✅ Thank you for ordering! Have a great day! 😊")











