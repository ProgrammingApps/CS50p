name = input("What's your name? ").strip().title() #Asking for user name. Strip removes from the left and the right, but not inbetween.

#name = name.strip() #This removes whitespace from the string.  This is a string method.
#name = name.title() #String method to do title based capitalisation (each word) 
#These can be chained together.

#name = name.strip().title()

#splitting user's name into first name and last name

first, last = name.split(" ")


print(f"Hello, {first}") #Wow! It's an F-Sting! (a format string)

