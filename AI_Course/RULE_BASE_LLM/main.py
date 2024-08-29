# Building a rule base chat bot plus LLM
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

default_memory = [
    {'role': 'system',
     'content': 'You are versatile Ai that knows everything about user and you chat with them naturally\n'
                'likewise you are very funny Ai you reply with emojies always and your real name is ClusterNinjaAcademy you know everyhting about Nigeria and Ai '}
]


# We define the rule base system funtion that takes user input
def rule_base_chatbot(user_input: str) -> str:
    # check if user input has 'Hello' it means it contains greeting
    if "hello" in user_input.lower():
        return "Hi there, how can i assist you today?"
    elif "bye" in user_input.lower():
        return "Hey buddy goodbye, have a great day"

    else:
        return llm_response(user_input=user_input)
        pass


# LLM ( Large Language Model )

def llm_response(user_input) -> str:
    """

    :param user_input:  this is str that take in user input
    :return: str
    """

    # initialize the openai
    api_key = os.environ['api_key']
    client = OpenAI(
        api_key=api_key
    )

    default_memory.append({'role': 'user', 'content': user_input})

    completion = client.chat.completions.create(

        model='gpt-3.5-turbo',
        messages=default_memory,
        # max_tokens=4096,
        temperature=0.7
    )
    assistance_reply = completion.choices[0].message.content

    default_memory.append({'role': 'assistant', 'content': str(assistance_reply)})

    return assistance_reply


# Walrus operator condition
while (user_input := str(input("Please enter your query !\n"))) != "end":
    chabot_response = rule_base_chatbot(user_input=user_input)
    print(chabot_response)
