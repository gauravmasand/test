import random

greetings = ["hello", "hi", "hey", "howdy",]
responses = ["Hello!", "Hi there!", "Hey!", "How can I help you today?"]

def get_response(user_input):
    user_input = user_input.lower()
    for word in greetings:
        if word in user_input:
            return random.choice(responses)
    return "I'm not sure how to respond to that."

print("Chatbot: Hello! How can I assist you today? t(type 'exit' to quit)")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)
