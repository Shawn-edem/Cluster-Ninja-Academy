# Building a rule base chat bot


# We define the rule base system funtion that takes user input
def rule_base_chatbot(user_input: str) -> str:

    # check if user input has 'Hello' it means it contains greeting
    if "hello" in user_input.lower():
        return "Hi there, how can i assist you today?"
    elif "bye" in user_input.lower():
        return "Hey buddy goodbye, have a great day"

    else:
        return "i am still learning"
        pass

# while 1:
#     user_input = input("Please enter your query !\n")
#     if user_input=='quit':
#         break

while (user_input := str(input("Please enter your query !\n"))) !="end":

    chabot_response = rule_base_chatbot(user_input=user_input)
    print(chabot_response)
