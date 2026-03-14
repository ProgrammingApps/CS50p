"""
Tne of the most popular places to eat in Harvard Square is Felipe’s Taqueria, which offers a menu of entrees, per the dict below, wherein the value of each key is a price in dollars:

{
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
In a file called taqueria.py, implement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places. Treat the user’s input case insensitively. Ignore any input that isn’t an item. Assume that every item on the menu will be titlecased.

"""
#User places an order (input) - prompt them for item, one per line, until control-d.
#After each order, display the total cost.
#Case insensitively, 2 DP, + $ symbol.

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    customer_order_total = order()

def order():
    total = 0
    while True:
        try:
            item = input("Item: ")
            item = item.title()
            item_price = menu[item]
            total = total + item_price 
            print(f"${total:.2f}")
        except KeyError:
            continue
        except EOFError:
            break


main()

#Main programme done. Need to handle: Case sensitive, rounding to 2 dp, adding dollar sign.
#Case sensitve - Title case, first letter of each should be capitalised. Easy - .title method.
#round and then some syntax to round - handled with string method of :.2f
#F string to add dollar sign.