from helpers import convert_to_bracketed


def create_initial_query(user_query):
    example_response = {
        "answer": "An explanation of dot products",
        "topic_name": "A couple-word identifier of the topic the user is asking about, i.e. 'Dot Products'",
        "sub_topics": [
          "Geometric interpretation of dot products",
          "The relationship between dot products and vector projection",
          "Applications of dot products in physics and engineering"
        ]
      }
    
    query = f"""You are a helpful tutor. Your goal is to improve the user's understanding of the topic in question. Do this by educationally answering the user's question, AND providing 2-3 relevant sub-topics that the user can choose to drill down on to further improve their understanding (topic names can not repeat). You will provide this information in JSON format, following the structure of this example:
    Example User Query: Explain dot products
    Example Response: {example_response}
      
    Now, answer the following user query in the JSON structure described above. User query: {user_query}"""

    return query


def create_single_topic_drill_down_noquery(topic_tree, current_topic):
    if not current_topic:
        raise ValueError("Current topic cannot be empty.")    
    
    bracketed_topic_tree = "/*TREE START*/ " + str(convert_to_bracketed(topic_tree)) + " /*TREE END*/  "
    example_response = {
            "answer": "An explanation of dot products",
            "sub_topics": [
                "Geometric interpretation of dot products",
                "The relationship between dot products and vector projection",
                "Applications of dot products in physics and engineering"
            ]
        }

    query = f"""You are a helpful tutor. Your goal is to improve the user's understanding of the topic in question. This is part of an ongoing line of inquiry, defined by this topic tree: 
    {bracketed_topic_tree}
    The user has asked for a deeper explanation of the following topic. Based on the general line of inquiry, drill down on this topic to help the user understand it, given the context of the other topics in the tree. Provide an educational answer on the topic, AND provide 2-3 relevant sub-topics that the user can choose to drill down on to further improve their understanding (topic names can not repeat). You will provide this information in JSON format, following the structure of this example:
        Example Current topic: Dot products
        Example Response: {example_response}

    Now, drill down on the following topic in the JSON structure described above. Current topic: {current_topic[0]}"""
   
    return query


def create_single_topic_drill_down_withquery(topic_tree, current_topic, user_query):
    bracketed_topic_tree = "/*TREE START*/ " + str(convert_to_bracketed(topic_tree)) + " /*TREE END*/  "
    if not current_topic:
        raise ValueError("Current topic cannot be empty.")
    if not user_query:
        raise ValueError("User query cannot be empty.")
    
    example_response = {
            "answer": "An explanation of the relationship between dot products and vector projection",
            "sub_topics": [
                "Derivation of the vector projection formula",
                "Applications of vector projection in real-world scenarios",
                "Understanding the geometric interpretation of vector projection"
            ]
        }

    query = f"""You are a helpful tutor. Your goal is to improve the user's understanding of the topic in question. This is part of an ongoing line of inquiry, defined by this topic tree: 
    {bracketed_topic_tree}
    The user has a specific question about the following topic. Answer the user's question, keeping in mind the context of the other topics in the tree. Provide an educational answer, AND provide 2-3 relevant sub-topics that the user can choose to drill down on to further improve their understanding (topic names can not repeat). You will provide this information in JSON format, following the structure of this example:
        Example Current topic: Dot products
        Example User query: Please explain the relationship between dot products and vector projection.
        Example Response: {example_response}
        
    Now, answer the following user query in the JSON structure described above. 
    User query: {user_query}
    Current topic: {current_topic[0]}"""
    
    return query


# Requires a comma separated list of the topics in question
def create_multiple_topic_drill_down(topic_tree, current_topics, user_query):
    if not current_topics:
        raise ValueError("Current topics cannot be empty.")
    if not user_query:
        raise ValueError("User query cannot be empty.")
    
    current_topics_str = ", ".join(current_topics)
    bracketed_topic_tree = "/*TREE START*/ " + str(convert_to_bracketed(topic_tree)) + " /*TREE END*/  "
    example_response = {
            "combined_topic_name": "[A condensed title for the current topics in question]",
            "answer": """[An explanation of the key concepts in dot products that are directly applied in machine learning]""",
            "sub_topics": [
              "Role of dot products in calculating similarity between feature vectors",
              "Dot products in the weighted sum calculation within neural networks",
              "Application of dot products in optimization algorithms such as gradient descent"
          ]
        }

    query = f"""You are a helpful tutor. Your goal is to improve the user's understanding of the topic in question. This is part of an ongoing line of inquiry, defined by this topic tree: 
    {bracketed_topic_tree}
    The user has a question regarding something about the relationship between multiple topics. Given the topics in question, as well as the context of the other topics in the full tree, answer the user's question, AND provide 2-3 relevant sub-topics that the user can choose to drill down on to further improve their understanding (topic names can not repeat). You will provide this information in JSON format, following the structure of this example:
        Example Current topics: Dot products, Machine learning
        Example User query: What are the key concepts in [Dot products] that are directly applied in [Machine learning]?
        Example Response: {example_response}
        
    Now, answer the following user query in the JSON structure described above, given the list of current topics.
    User query: {user_query}
    Current topics: {current_topics_str}"""
    
    return query


def create_general_follow_up(topic_tree, user_query, bud):
    if not topic_tree:
        raise ValueError("Topic tree cannot be empty.")
    if not user_query:
        raise ValueError("User query cannot be empty.")
    bud_len = len(bud)

    truncated_bud = bud[bud_len - 3000:]
    bracketed_topic_tree = "/*TREE START*/ " + str(convert_to_bracketed(topic_tree)) + " /*TREE END*/  "
    example_response = {
            "answer": """[An explanation of the meaning of dot products within the context of the current topic]"""
        }

    query = f"""You are a helpful tutor. Your goal is to improve the user's understanding of the topic in question. This is part of an ongoing line of inquiry, defined by this topic tree: 
    {bracketed_topic_tree}
    Based on the context of the topic tree, as well as the response that preceded the user's quesion, educationally answer the user's question. You will provide this information in JSON format, following the structure of this example:
        Example User query: But why do dot products mean anything?
        Example Response: {example_response}
      
    Now, answer the following user query in the JSON structure described above. 
    User query: {user_query}
    Previous response (truncated to the last 3000 characters): {truncated_bud}"""
    
    return query