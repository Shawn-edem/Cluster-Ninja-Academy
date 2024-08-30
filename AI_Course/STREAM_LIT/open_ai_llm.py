import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
def llm_response(user_input, memory) -> str:
    """

    :param user_input:  this is str that take in user input
    :return: str
    """

    # initialize the openai
    api_key = os.environ['api_key']
    client = OpenAI(
        api_key=api_key
    )



    completion = client.chat.completions.create(

        model='gpt-3.5-turbo',
        messages=memory,
        # max_tokens=4096,
        temperature=0.7
    )
    assistance_reply = completion.choices[0].message.content

    return assistance_reply

