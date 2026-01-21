def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    #this should convert the $50.00 to 50.0
    d = d.replace("$", "")
    return float(d)



def percent_to_float(p):
    #this should convert the 10% to 0.1
    p = float(p.replace("%", ""))
    return p / 100



main()