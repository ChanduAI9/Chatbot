import nltk
from nltk.chat.util import Chat, reflections


reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

# pairs of responses for the chatbot
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?", "Hi there %1, nice to meet you!"]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot and I'm a simple chatbot.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about you?", "I'm fine, thank you!"]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "It's OK, never mind"]
    ],
    [
        r"(.*)(good|great|fine)",
        ["Nice to hear that", "Alright :)"]
    ],
    [
        r"(.*) age?",
        ["I'm just a computer program, I don't have an age."]
    ],
    [
        r"what (.*) want ?",
        ["I want to help you.", "I'm here to assist you."]
    ],
    [
        r"(.*) created ?",
        ["I was created by a Python programmer.", "I was made by someone who loves coding."]
    ],
    [
        r"bye",
        ["Bye, take care. See you soon :)", "It was nice talking to you. Goodbye!"]
    ],
    [
        r"(.*)(hello|hi|hey)",
        ["Hello!", "Hi there!", "Hey!"]
    ],
    [
        r"(.*)(thank you|thanks)",
        ["You're welcome!", "No problem!"]
    ],
    [
        r"(.*)(tell me a joke)",
        ["Why don't scientists trust atoms? Because they make up everything!"]
    ],
    [
        r"(.*) (love|like) you",
        ["Aw, thanks! I'm here to assist you whenever you need."]
    ],
    [
        r"(.*) weather (.*)",
        ["I'm just a chatbot, I don't have access to weather information."]
    ],
]

chatbot = Chat(pairs, reflections)

def chat():
    print("Hi, I'm Chatbot! How can I help you today?")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("Chatbot:", response)
        if user_input == "bye":
            break
if __name__ == "__main__":
    chat()
