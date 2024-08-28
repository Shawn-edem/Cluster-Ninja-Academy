
### Assignment 1: Basic Rule-Based Chatbot
**Objective:** Implement a simple rule-based chatbot that handles basic greetings and farewells.

**Instructions:**
- Modify the chatbot to handle additional greetings like "hi" and "hey."
- Add a rule to handle questions about the time (e.g., "What time is it?").
- Expand the chatbot's responses for each new rule.

**Example Code Snippet:**
```python
def rule_base_chatbot(user_input: str) -> str:
    if "hello" in user_input.lower() or "hi" in user_input.lower() or "hey" in user_input.lower():
        return "Hello! How can I help you today?"
    elif "bye" in user_input.lower():
        return "Goodbye! Have a great day!"
    elif "time" in user_input.lower():
        return "I'm sorry, I can't tell time yet!"
    else:
        return "I'm still learning. Please ask something else."

while (user_input := str(input("Please enter your query!\n"))) != "end":
    chatbot_response = rule_base_chatbot(user_input=user_input)
    print(chatbot_response)
```

### Assignment 2: Adding More Rules
**Objective:** Enhance the chatbot to handle more specific queries and include error handling.

**Instructions:**
- Add rules for common questions like "How are you?" and "What's your name?"
- Implement error handling to ensure the chatbot does not crash with unexpected input (e.g., numbers or special characters).
- Provide feedback to the user if the input is not understood.

**Example Code Snippet:**
```python
def rule_base_chatbot(user_input: str) -> str:
    try:
        if "hello" in user_input.lower():
            return "Hi there! How can I assist you today?"
        elif "bye" in user_input.lower():
            return "Goodbye! Have a wonderful day!"
        elif "how are you" in user_input.lower():
            return "I'm a bot, so I don't have feelings, but I'm here to help!"
        elif "name" in user_input.lower():
            return "I don't have a name yet, but you can call me 'ChatBot'."
        else:
            return "Sorry, I don't understand that. Can you try asking in a different way?"
    except Exception as e:
        return f"Oops! Something went wrong: {str(e)}"

while (user_input := str(input("Please enter your query!\n"))) != "end":
    chatbot_response = rule_base_chatbot(user_input=user_input)
    print(chatbot_response)
```

### Assignment 3: Expanding Responses with Variability
**Objective:** Make the chatbot responses more dynamic by including variability in the responses.

**Instructions:**
- Modify the chatbot to provide different responses for the same type of query (e.g., different ways of saying "hello").
- Implement a simple random choice function to select a response from a list of possible responses for each rule.

**Example Code Snippet:**
```python
import random

def rule_base_chatbot(user_input: str) -> str:
    greetings = ["Hi there!", "Hello!", "Hey! How can I help?"]
    farewells = ["Goodbye!", "See you later!", "Take care!"]

    if "hello" in user_input.lower():
        return random.choice(greetings)
    elif "bye" in user_input.lower():
        return random.choice(farewells)
    elif "how are you" in user_input.lower():
        return "I'm just a bot, but I'm here to help!"
    elif "name" in user_input.lower():
        return "I'm ChatBot, your virtual assistant."
    else:
        return "I don't know that one yet, but I'm learning!"

while (user_input := str(input("Please enter your query!\n"))) != "end":
    chatbot_response = rule_base_chatbot(user_input=user_input)
    print(chatbot_response)
```

### Assignment 4: Basic Memory - Tracking Conversation Context
**Objective:** Implement a basic memory system where the chatbot remembers the user's name during the conversation.

**Instructions:**
- Modify the chatbot to ask the user's name if it hasn't been provided.
- Store the user's name in a variable and use it to personalize responses throughout the conversation.
- Allow the user to reset the chatbot's memory by typing "reset."

**Example Code Snippet:**
```python
user_name = None

def rule_base_chatbot(user_input: str) -> str:
    global user_name
    if user_input.lower() == "reset":
        user_name = None
        return "Memory reset! What's your name?"
    
    if user_name is None:
        if "name" in user_input.lower():
            user_name = user_input.split()[-1]  # Assumes the last word is the user's name
            return f"Nice to meet you, {user_name}!"
        else:
            return "I don't know your name yet. What's your name?"
    
    if "hello" in user_input.lower():
        return f"Hello, {user_name}! How can I help you today?"
    elif "bye" in user_input.lower():
        return f"Goodbye, {user_name}! Have a great day!"
    else:
        return f"I'm still learning, {user_name}. Please ask something else."

while (user_input := str(input("Please enter your query!\n"))) != "end":
    chatbot_response = rule_base_chatbot(user_input=user_input)
    print(chatbot_response)
```

### Assignment 5: Advanced - Auto Learning from User Input
**Objective:** Create an advanced chatbot that learns new responses from user input and stores them in a text file for future use.

**Instructions:**
- Modify the chatbot to save new user inputs and responses to a text file (e.g., `chatbot_memory.txt`).
- If the user input is not recognized, prompt the user to provide a suitable response.
- Store the new user input-response pair in the file and use it in future conversations.
- Implement the ability to load the memory from the text file when the chatbot starts.

**Example Code Snippet:**
```python
import os

# Load existing memory from the file
def load_memory():
    memory = {}
    if os.path.exists("chatbot_memory.txt"):
        with open("chatbot_memory.txt", "r") as file:
            for line in file:
                user_input, response = line.strip().split("|")
                memory[user_input.lower()] = response
    return memory

# Save new memory to the file
def save_memory(user_input, response):
    with open("chatbot_memory.txt", "a") as file:
        file.write(f"{user_input.lower()}|{response}\n")

# Initialize memory
chatbot_memory = load_memory()

def rule_base_chatbot(user_input: str) -> str:
    if user_input.lower() in chatbot_memory:
        return chatbot_memory[user_input.lower()]
    else:
        # Prompt user to provide a response for unrecognized input
        new_response = input("I don't know how to respond to that. How should I respond?\n")
        save_memory(user_input, new_response)
        chatbot_memory[user_input.lower()] = new_response
        return f"Got it! I'll remember to respond with: {new_response}"

while (user_input := str(input("Please enter your query!\n"))) != "end":
    chatbot_response = rule_base_chatbot(user_input=user_input)
    print(chatbot_response)
```

### How it works:
- **Assignment 5:** When the chatbot encounters an unknown input, it asks the user for a suitable response and stores this in a text file (`chatbot_memory.txt`). The next time the same input is provided, the chatbot responds based on the stored information.

**Testing:**
- Start with basic user inputs like "hello" or "bye" and observe how the chatbot behaves.
- Test with inputs that the chatbot doesn't recognize and provide new responses to see if it learns.

