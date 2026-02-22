#coke costs 50 cents.
#Amount Due:
#Insert Coin:
#25, 10, 5 amounts.


# Starts with 50 cents, then decreases for each 25, 10 and 5. Once it reaches the amount, say how much change.

def main():
    amount_remaining = 50
    print("Amount Due: " + str(amount_remaining))
    while amount_remaining > 0:
            coin_inserted = int(input("Insert Coin: "))
            if coin_inserted in [5,10,25]:
                amount_remaining = amount_remaining - coin_inserted
                if amount_remaining > 0:
                     print("Amount Due: " + str(amount_remaining))
            else:
                 print("Invalid coin")
                 print("Amount Due: " + str(amount_remaining))
         
    if amount_remaining <= 0:
        print("Change Owed: " + str(abs(amount_remaining)))

main()