from svc.llm_svc import ask_model

EXIT_KEYWORD = "bye"


def ask(user_input):
    for chunk in ask_model(user_input=user_input):
        yield chunk


def main():
    print("Eva: Hello! I am Eva, your chatbot :). Type 'bye' to exit.")
    while True:
        user_input = input("\n\nYou: ")
        if user_input.lower() == EXIT_KEYWORD:
            print("Chatbot: Goodbye! Have a great day!")
            break

        print("\nEva: ")
        for chunk in ask(user_input):
            print(chunk, end='', flush=True)


if __name__ == "__main__":
    main()
