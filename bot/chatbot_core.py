import openai
# import secret
import os
from dotenv import load_dotenv

# Chatbot initialize
INITIAL_PROMPT = "I'm Cookiesier. What would you like to cook today?"
_conversation_history = INITIAL_PROMPT + "\n"
_AI_NAME = "Cookiesier"
_USER_NAME = "User"

# Set up your OpenAI API credentials
# openai.api_key = secret.OPENAI_API_KEY
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

################################################################################
# Define a function to get the chatbot response from OpenAI
def get_chatbot_response(input_text):
    
    response = openai.Completion.create(
        engine = "text-davinci-003",
        #engine="davinci:ft-personal-2023-03-07-14-28-06",
        prompt= INITIAL_PROMPT + input_text,
        temperature=0.3,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].text.strip()
################################################################################
def handle_input(
               input_str : str,
    conversation_history = _conversation_history,
                 AI_NAME = _AI_NAME,
                 USER_NAME = _USER_NAME
                 ):
    """Updates the conversation history and generates a response using GPT-3."""
    # Update the conversation history
    conversation_history += f"{USER_NAME}: {input_str}\n"
   
    # Generate a response using GPT-3
    message = get_chatbot_response(conversation_history)

    # Update the conversation history
    conversation_history += f"{AI_NAME}: {message}\n"
    print(len(conversation_history))

    # Update conversation memory
    if len(conversation_history) >= 2000:
        for character in range(500):
            conversation_history.replace(character + len(INITIAL_PROMPT), '')
    

    # Print the response
    print(f'{AI_NAME}: {message}')
    
    return message
