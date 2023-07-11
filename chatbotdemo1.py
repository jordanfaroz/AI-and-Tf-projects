import random

# Define a dictionary of possible chatbot responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hi, how are you?"],
    "how are you": ["I'm good, thanks for asking!", "I'm doing well, and you?", "I'm great, thanks!"],
    "bye": ["Goodbye!", "See you later!", "Bye!"],
    "default": ["I'm not sure what you mean, can you please clarify?", "I didn't understand, could you please rephrase that?"]
}

# Define a function to generate a response to a user message
def generate_response(message):
    # Convert the message to lowercase and remove any punctuation
    message = message.lower().strip(".,!?")
    # Check if the message matches one of the predefined responses
    if message in responses:
        # Return a random response from the list of responses for that message
        return random.choice(responses[message])
    else:
        # If the message doesn't match any predefined responses, return a default response
        return random.choice(responses["default"])

# Define a loop to receive and respond to user input
while True:
    # Get the user input
    user_input = input("You: ")
    # Generate a response based on the user input
    bot_response = generate_response(user_input)
    # Print the bot's response
    print("Bot:", bot_response)