name = input("What's your name?")

match name:
    case "Harry" | "Hermoine" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slyverthine")
    case _:
        print("Who?")
