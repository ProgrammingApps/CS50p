

answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")

match answer:
    case "42" | "forty-two" | "Forty Two":
        print("Yes")
    case _:
        print("No")



