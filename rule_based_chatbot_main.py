import random
import re  # Add this line to import the 're' module

patterns = {
    r"\b(hi|hey|hy)\b": ["Hello!", "Hi there!", "Hey!", "Hi! How can I help you?"],
    r"\b(how are u|how are you|how are u\?|how are you\?)\b": ["I'm doing well, thank you!",
                                                               "I'm good, thanks for asking.",
                                                               "I'm fine, how about you?"],
    r"\b(what's your name|what is your name|your name|what's your name\?|what is  your name\?|your name\?)\b": [
        "I'm a chatbot.", "I'm a bot designed to chat.", "You can call me a chatbot."],
    r"\b(bye|bye bye)\b": ["Goodbye!", "Bye!", "See you later!", "Have a great day!"],
    "tell me a joke": ["Why don't skeletons fight each other? They don't have the guts!",
                       "What do you call an alligator in a vest? An investigator!"],
    r"\b(what are you doing|what are u doing\?|what r u doing\?|what r u doing|what r you doing\?)\b": [
        "Just chatting with you!", "Answering your questions!", "Being a helpful bot!"],
    r"\b(where are you from|where are u from\?|where r u from|where r u from\?)\b": ["I exist in the digital world!",
                                                                                     "I don't have a physical location, I'm a program!"],
    r"\b(do you like music|do u like  music\?)\b": ["I can't listen to music, but I know a lot about it!",
                                                    "I don't have ears, but music is fascinating!"],
    r"\b(how old are you|how old r u\?|how old are you\?|how old are u\?)\b": [
        "I don't have an age, I'm here to assist!"],
    r"\b(what is the meaning of life)\b": ["That's a big question! The answer may vary for everyone."],
    r"\b(do you dream)\b": ["I don't sleep, so I don't dream!"],
    r"\b(who created you)\b": ["I was created by a team of developers.", "I'm a product of coding and creativity!"],
    r"\b(thanks)\b": ["You're welcome!", "No problem!", "Glad I could help!"],
    r"\b(help)\b": ["Sure, what do you need help with?", "How can I assist you?"],
    r"\b(can you learn|can u learn\?|can you learn\?|can u learn)\b": [
        "I don't learn like humans do, but I can provide information based on programmed knowledge!"],
    r"\b(what can you do|wat can u do|what can u do\?|what can you do\?)\b": [
        "I can chat, provide information, tell jokes, and more!"],
    r"\b(I'm bored|i m bored talk to me)\b": ["Let's chat! Ask me something.",
                                              "I can entertain you with a joke or some information."],
    r"\b(what's up|whatsup|whats up)\b": ["Not much, just here to chat!", "Just hanging out in the digital world!"],
    r"\b(I love you)\b": ["That's very kind, but I'm just a bot!"]
}   #could be added more
def respond(user_input):
    user_input = user_input.lower()
    for pattern, responses in patterns.items():
        if re.match(pattern, user_input):       #if pattern matces then respond accordingly otherwise return statement  "I'm not sure how to respond to that."
            return random.choice(responses)
    return "I'm not sure how to respond to that."

print("Welcome! Let's chat. Type 'bye' to exit.")
while True:
    user_query = input("You: ")
    if user_query.lower() == 'bye':
        print(respond(user_query))
        break
    else:
        print("Bot:", respond(user_query))