from openai import OpenAI
from pydantic import BaseModel
import os

client = OpenAI()

# Define data structure models using Pydantic
class InitialResponse(BaseModel):
    answer: str
    topic_name: str
    sub_topics: list[str]

class SingleDrillResponse(BaseModel):
    answer: str
    sub_topics: list[str]

class GeneralFollowupResponse(BaseModel):
    answer: str

class MultiDrillResponse(BaseModel):
    combined_topic_name: str
    answer: str
    sub_topics: list[str]

def call_openai_api(prompt, response_format, temperature=0.5, max_tokens=300):
    """
    Function to call the OpenAI API using the given prompt and returns the response in JSON format.
    
    Args:
        prompt (list): The prompt to send to the API, composed of 2 values, the system prompt and the user input
        temperature (float): Sampling temperature, higher values mean more random output. Default is 0.5.
        top_p (float): Controls the diversity of the response. Default is 1.0.
        max_tokens (int): The maximum number of tokens in the output. Default is 300.
    
    Returns:
        dict: The response from GPT in JSON format.
    """
    try:
        completion = client.beta.chat.completions.parse(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are part of a learning interface, helping users understand topics more thoroughly by exploring sub topics and relationships."},
                {"role": "user", "content": prompt}
            ],
            response_format=response_format,
            temperature=temperature
        )

        return completion.choices[0].message.parsed
    
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return None

# Specialized functions for different types of interactions
def get_initial_response(prompt):
    """
    Gets the initial response for a user's query, focusing on educational depth and generating subtopics.
    
    Args:
        prompt (str): The initial prompt for the user's question.
    
    Returns:
        dict: The response from GPT in JSON format.
    """
    response_format = InitialResponse

    response = call_openai_api(prompt, response_format, temperature=0.6)

    if response:
        return response.model_dump()  # Convert Pydantic model to a dictionary
    else:
        return None

def get_single_drill_response(prompt):
    """
    Gets the response for a single topic drill-down, focusing on providing in-depth information on one subtopic.
    
    Args:
        prompt (str): The prompt for drilling down into a specific topic.
    
    Returns:
        dict: The response from GPT in JSON format.
    """
    response_format = SingleDrillResponse

    response = call_openai_api(prompt, response_format, temperature=0.5)

    if response:
        return response.model_dump()  # Convert Pydantic model to a dictionary
    else:
        return None

def get_general_followup_response(prompt):
    """
    Gets the response for a general follow-up question on the current topic, focusing on maintaining the topic continuity.
    
    Args:
        prompt (str): The prompt for the follow-up question.
    
    Returns:
        dict: The response from GPT in JSON format.
    """
    response_format = GeneralFollowupResponse

    response = call_openai_api(prompt, response_format, temperature=0.4)

    if response:
        return response.model_dump()  # Convert Pydantic model to a dictionary
    else:
        return None

def get_multi_drill_response(prompt):
    """
    Gets the response for a multiple topic drill-down, focusing on synthesizing information from multiple sources.
    
    Args:
        prompt (str): The prompt for exploring relationships between multiple topics.
    
    Returns:
        dict: The response from GPT in JSON format.
    """
    response_format = MultiDrillResponse

    response = call_openai_api(prompt, response_format, temperature=0.7)

    if response:
        return response.model_dump()  # Convert Pydantic model to a dictionary
    else:
        return None