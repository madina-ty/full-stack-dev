import datetime 

loyaltyMembers = [
    'madina',
    'anuar'
]
def apply_basic_discount(price):
    return price * 0.50

def apply_loyalty_discount(price):
    return price * 0.70

def apply_basic_tax(price):
    return price * 0.20

def apply_wildcard_tax(price):
    time_min = datetime.datetime.now().minute 
    if time_min % 2 != 0:
        return price * 0.05
    return 0

def calculate_final_price(client, price): 
    final_price =  apply_basic_discount(price)
    if client in loyaltyMembers:
        final_price = apply_loyalty_discount(price)

    final_price += apply_basic_tax(final_price)

    final_price += apply_wildcard_tax(final_price)

    return final_price


client = input("enter your name :  ")
price = float(input("enter your price :  ")) 
final_price = calculate_final_price(client, price)
print(f"{client} your final price is {final_price}")


