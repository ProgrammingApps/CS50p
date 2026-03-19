"""
In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY), otherwise known as middle-endian order, which is arguably bad design. 
Dates in that format can’t be easily sorted because the date’s year comes last instead of first. 
Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet). 
Dates in that format are also ambiguous. Harvard was founded on September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!

Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates should be formatted in year-month-day (YYYY-MM-DD) order, 
no matter the country, formatting years with four digits, months with two digits, and days with two digits, “padding” each with leading zeroes as needed.

In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, 
formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:

[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
Then output that same date in YYYY-MM-DD format. 
If the user’s input is not a valid date in either format, prompt the user again. 
Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.
"""

#Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods, including split.
#Recall that a list comes with quite a few methods, per docs.python.org/3/tutorial/datastructures.html#more-on-lists, among which is index.
#Note that you can format an int with leading zeroes with code like
#print(f"{n:02}")

#psudo logic:
"""
input will be x/x/xxxx where x are numbers.
Needs to output YYYY-MM-DD, where y is years, m is months and d is days.

Ask for the input date
Split this input date into days, months and years.
Checks if the month is alphabetical.
If it is, convert the month into a number
otherwise, 
make sure the list is indexed + 1.
then we can re-order it into YYYY-MM-DD



"""

def main():
    final_date = outdated()
    print(final_date)
    

def outdated():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    while True:
        try:
            user_input = input("Date: ").strip() #This will get us a string like MM/DD/YYYY
            if "," in user_input: #Convert something like September 8, 1636 into Month, Day, year.
                user_input = user_input.replace(",", "")
                month, day, year = user_input.split(" ")
                month = months.index(month) + 1
                day = int(day)
                if not (1 <= month <= 12 and 1 <= day <= 31):
                    continue
                return(f"{year}-{month:02}-{day:02}")
            else:
                month, day, year = user_input.split("/") #So you'll get the month, day and year numbers.
                month = int(month)
                day = int(day)
                if not (1 <= month <= 12 and 1<= day <= 31):
                    continue
                return(f"{year}-{month:02}-{day:02}")
        except ValueError:
            print("Unknown value, try again")
            continue

main()




