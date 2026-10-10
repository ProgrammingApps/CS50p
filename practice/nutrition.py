'''
Goal: the user types a fruit name, and your program tells them how many calories it has.

Steps:

Ask the user for a fruit. The prompt should say Item: .
Make it case-insensitive. APPLE, apple and Apple should all work the same.
Look the fruit up. You need somewhere to store each fruit alongside its calorie count.
If it's a real fruit, print Calories: 130 (with the right number).
If it isn't, print nothing at all.

Examples:

Apple → Calories: 130
sweet cherries → Calories: 100
Tomato → nothing

Data:

apple 130, avocado 50, banana 110, cantaloupe 50, grapefruit 60,
grapes 90, honeydew melon 50, kiwifruit 90, lemon 15, lime 20,
nectarine 60, orange 80, peach 60, pear 100, pineapple 50,
plums 70, strawberries 50, sweet cherries 100, tangerine 50, watermelon 80


Implement a program that prompts the user to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, 
per the FDA's poster for fruits. Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry). 
Ignore any input that isn't a fruit.

'''

fruit = input("Item:")