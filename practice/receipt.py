'''
Receipt  (Weeks 0–1: input, types, functions, return values, f-strings, conditionals)

Goal: a tiny till. The user enters a price and a quantity; you print the total.

Steps:

Prompt for a price with "Price: " (e.g. 4.50 or £4.50, so the £ is optional).
Prompt for a quantity with "Quantity: " (a whole number).
If the subtotal is £50 or more, take 10% off.
Print the total as "Total: £X.XX", always with exactly two decimal places.

Structure it like this. main does the input and output, and the other functions only calculate:

    def main(): ...
    def parse_price(text): ...      # "£4.50" -> 4.5   (returns a float)
    def total(price, quantity): ... # applies the discount rule, returns a float

Examples:

Price: 4.50   Quantity: 3  → Total: £13.50
Price: £12.99 Quantity: 4  → Total: £46.76
Price: 50     Quantity: 1  → Total: £45.00

Before you run it: predict what happens if the user types "four" for the price.
(You don't need to handle it yet. That's Week 3. Just predict, then check.)

Reflect: why should total() *return* a value rather than print it?
Reflect: So it can pass the value to main() instead of just printing it to terminal
'''

def main():
    price = parse_price(input("Price: "))
    quantity = int(input("Quantity: "))
    print(f"Total: £{total(price, quantity):.2f}")

def parse_price(text):
    text = text.strip("£")
    return float(text)

def total(price, quantity):
    subtotal = price * quantity
    if subtotal >= 50:
        return subtotal * 0.9
    else:
        return subtotal

if __name__ == "__main__":
    main()