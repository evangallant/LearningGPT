from openai import OpenAI
import os

def call_openai_api(prompt, temperature=0.5, max_tokens=300):
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
        client = OpenAI()

        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are part of a learning interface, helping users understand topics more thoroughly by exploring sub topics and relationships."},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"},
            temperature=temperature
        )

        return completion.choices[0].message.content
    
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
    return call_openai_api(prompt, temperature=0.6)

def get_single_drill_response(prompt):
    """
    Gets the response for a single topic drill-down, focusing on providing in-depth information on one subtopic.
    
    Args:
        prompt (str): The prompt for drilling down into a specific topic.
    
    Returns:
        dict: The response from GPT in JSON format.
    """
    return call_openai_api(prompt, temperature=0.5)

def get_general_followup_response(prompt):
    """
    Gets the response for a general follow-up question on the current topic, focusing on maintaining the topic continuity.
    
    Args:
        prompt (str): The prompt for the follow-up question.
    
    Returns:
        dict: The response from GPT in JSON format.
    """
    return call_openai_api(prompt, temperature=0.4)

def get_multi_drill_response(prompt):
    """
    Gets the response for a multiple topic drill-down, focusing on synthesizing information from multiple sources.
    
    Args:
        prompt (str): The prompt for exploring relationships between multiple topics.
    
    Returns:
        dict: The response from GPT in JSON format.
    """
    return call_openai_api(prompt, temperature=0.7)

# Example usage
def main():
    user_prompt = "Explain how neural networks work."
    initial_query_prompt = create_initial_query(user_prompt)
    response = get_initial_response(initial_query_prompt)
    if response:
        print(response)

if __name__ == "__main__":
    main()