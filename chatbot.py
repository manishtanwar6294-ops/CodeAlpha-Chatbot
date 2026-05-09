def get_reply(message):
    message = message.lower()

    if message == "hello" or message == "hi" or message == "hey" or message == "hii":
        return "Hii!"
    elif message == "how are you":
        return "I'm fine, What about you!"
    elif message == "what is your name":
        return "I don't have a name, but you can call me Chatbot."
    elif message == "what can you do":
        return "I can chat with you and answer only these questions which are programmed in me."
    elif message == "bye" or message == "goodbye":
        return "Goodbye! See you later!"
    elif message == "what is your favorite color":
        return " I think all colors are beautiful!"
    elif message == "ok,see you later":
        return "ok ji see you later!"
    else:
        return "Sorry, I don't understand that."


def run_chatbot():
    print(" Welcome to the Chatbot! Type 'bye' or 'goodbye' to exit the chat")
    print("##--------------------------------------##")

    while True:
        user_input = input("You: ").strip()
        reply = get_reply(user_input)
        print("ChatBot:", reply)

        if user_input.lower() == "bye" or user_input.lower() == "goodbye":
            break


run_chatbot()