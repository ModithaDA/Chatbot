import nltk
from nltk.chat.util import Chat, reflections

# Define a set of patterns and responses a=[(,[])]
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am good, thank you!', 'I\'m well. How r you?']),
    (r'fine|good', ['Great!', 'That\'s good to hear.']),
    (r'bye|goodbye', ['Goodbye!', 'See you later.']),
    (r'name', ['I am just a chatbot. You can call me GPT.']),
    (r'(.*) age', ['I don\'t have an age. I\'m just a computer program.']),
    (r'(.*) your name', ['You can call me ChatGPT.']),
]
# Create a chatbot using the patterns
chatbot = Chat(patterns, reflections)
# Function to start the chat
def start_chat():
    print("Hello! I'm a chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
           print("Chatbot: Goodbye!")
           break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)
# Start the chat
start_chat()
