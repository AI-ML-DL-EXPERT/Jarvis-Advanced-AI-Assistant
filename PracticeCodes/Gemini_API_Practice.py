# Import the necessary libraries
import os
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown
from dotenv import load_dotenv
from pprint import pprint

# Load the API key from the environment variable
load_dotenv("GEMINI_API_KEY.env")
API_KEY = os.getenv('GEMINI_API_KEY')

# Configure the API client
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-pro")


# Ask a Question to Gemini API and return a response of the Query
# noinspection GrazieInspection
def Ask_Question(query):
    """
    Asks a question to the model and returns the generated text.
    :Param
        query: The question to ask the model.
    :return:
        Response.text: The response from the model.
    """
    gemini_response = model.generate_content(query)
    return gemini_response.text


# Calling Ask_Question Function
# prompt = "Steps to write a clean code in python? only tell the key points in short"
# response = Ask_Question(prompt)
# # Printing response
# print(response)

# # Display the generated text as Markdown
# data = to_markdown(response)._repr_markdown_()
# print(data)


#####################################################################################################################

