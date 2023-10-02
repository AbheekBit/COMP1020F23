from ChatBot import *


def main():
    open("MyBot.txt")

    print("Hello there! I am TalkGPT")
    response_from_user = True

    bot = ChatBot("Hello there! I am TalkPPT", "MyBot.txt", "Sorry I am not able to answer that.")

    while response_from_user:
        user_input = input()

        if user_input == "stop":
            print("Goodbye")
            response_from_user = False
            break
        print(bot.respond(user_input))


if __name__ == "__main__":
    main()
