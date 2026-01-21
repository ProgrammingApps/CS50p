def main():
    response = input("Hey, how're you doing today?")
    convert(response)


def convert(user_input):
    converted_text = user_input.replace(":)", "🙂")
    converted_text = converted_text.replace(":(", "🙁")
    print(converted_text)

main()