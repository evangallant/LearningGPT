def initialize_topic_tree(gpt_json):
    """
    Initializes the topic tree based on the initial GPT response.
    
    Args:
        gpt_json (dict): The JSON response from GPT for the initial query.
            Expected structure:
            {
                "answer": "[An explanation of dot products]",
                "topic_name": "Dot Products",
                "sub_topics": [
                    "Geometric interpretation of dot products",
                    "The relationship between dot products and vector projection",
                    "Applications of dot products in physics and engineering"
                ]
            }
    
    Returns:
        dict: The initialized topic tree.
    """
    topic_tree = {
        "root": {
            "topic": {
                "branch": gpt_json.get("topic_name", ""),
                "bud": gpt_json.get("answer", ""),
                "related_topics": [],
                "relationship_query": None,
                "current": True
            },
            "branches": []
        }
    }

    # Create branches for the sub-topics
    for sub_topic in gpt_json.get("sub_topics", []):
        topic_tree["root"]["branches"].append({
            "topic": {
                "branch": sub_topic,
                "bud": None,
                "related_topics": [],
                "relationship_query": None,
                "current": False
            },
            "branches": []
        })

    return topic_tree


def update_topic_tree(topic_tree, update_type, gpt_json, current_topic=None, user_query=None):
    """
    Updates the topic tree based on the user's action.
    
    Args:
        topic_tree (dict): The current topic tree structure.
        update_type (str): The type of update to be performed. Possible values:
                          - "single_drill_no_query"
                          - "single_drill_with_query"
                          - "multi_drill"
                          - "general_follow_up"
        gpt_json (dict): The JSON response from GPT for the new query.
        current_topic (array, optional): The topic currently being drilled down on (in an array), OR a comma separated array of multiple topics in a multi_drill query.
        user_query (str, optional): The user's question about the relationship between topics.
        combined_topic_name (str, optional): GPT's suggestion for a new topic name resulting from a multi-drill query
    
    Returns:
        dict: The updated topic tree.
    """
    if not update_type:
        raise ValueError("Update type required.")

    if update_type == "single_drill_no_query":
        # Find the current topic and update its details
        def find_and_update(node):
            if isinstance(node, list):
                for item in node:
                    if find_and_update(item):
                        return True
            else:
                if node["topic"].get("branch") == current_topic[0]:
                    node["topic"]["bud"] = gpt_json.get("answer", "")
                    node["topic"]["current"] = True
                    # Add new branches based on sub_topics
                    node["branches"] = [
                        {
                            "topic": {
                                "branch": sub_topic,
                                "bud": None,
                                "related_topics": [],
                                "relationship_query": None,
                                "current": False
                            },
                            "branches": []
                        }
                        for sub_topic in gpt_json.get("sub_topics", [])
                    ]
                    return True
                # Recursively search branches
                for branch in node.get("branches", []):
                    if find_and_update(branch):
                        return True
            return False

        # Update the current topic to False for all nodes
        def set_all_current_to_false(node):
            if isinstance(node, list):
                for item in node:
                    set_all_current_to_false(item)
            else:
                node["topic"]["current"] = False
                for branch in node.get("branches", []):
                    set_all_current_to_false(branch)

        set_all_current_to_false(topic_tree["root"])
        if "combined_topics" in topic_tree:
            set_all_current_to_false(topic_tree["combined_topics"])

        find_and_update(topic_tree["root"])
        if "combined_topics" in topic_tree:
            find_and_update(topic_tree["combined_topics"])

    elif update_type == "single_drill_with_query":
        # Similar to single_drill_no_query, but also includes a user query
        if not user_query:
            raise ValueError("User query required for single drill with query.")

        def find_and_update_with_query(node):
            if isinstance(node, list):
                for item in node:
                    if find_and_update_with_query(item):
                        return True
            else:
                if node["topic"].get("branch") == current_topic[0]:
                    node["topic"]["bud"] = gpt_json.get("answer", "")
                    node["topic"]["current"] = True
                    # Add new branches based on sub_topics
                    node["branches"] = [
                        {
                            "topic": {
                                "branch": sub_topic,
                                "bud": None,
                                "related_topics": [],
                                "relationship_query": None,
                                "current": False
                            },
                            "branches": []
                        }
                        for sub_topic in gpt_json.get("sub_topics", [])
                    ]
                    return True
                # Recursively search branches
                for branch in node.get("branches", []):
                    if find_and_update_with_query(branch):
                        return True
            return False

        # Update the current topic to False for all nodes
        def set_all_current_to_false(node):
            if isinstance(node, list):
                for item in node:
                    set_all_current_to_false(item)
            else:
                node["topic"]["current"] = False
                for branch in node.get("branches", []):
                    set_all_current_to_false(branch)

        set_all_current_to_false(topic_tree["root"])
        if "combined_topics" in topic_tree:
            set_all_current_to_false(topic_tree["combined_topics"])

        find_and_update_with_query(topic_tree["root"])
        if "combined_topics" in topic_tree:
            find_and_update_with_query(topic_tree["combined_topics"])

    elif update_type == "multi_drill":
        # Create a combined topic for the multi-drill action
        if not user_query:
            raise ValueError("User query required for multi-drill.")
        
        if not gpt_json.get("combined_topic_name"):
            raise ValueError("GPT Json missing 'combined_topic_name' value, required for multi-drill.")

        combined_branch = {
            "topic": {
                "branch": gpt_json.get("combined_topic_name"),
                "bud": gpt_json.get("answer", ""),
                "related_topics": current_topic,
                "relationship_query": user_query,
                "current": True
            },
            "branches": []
        }

        # Add branches for sub-topics from the gpt_json
        for sub_topic in gpt_json.get("sub_topics", []):
            combined_branch["branches"].append({
                "topic": {
                    "branch": sub_topic,
                    "bud": None,
                    "related_topics": [],
                    "relationship_query": None,
                    "current": False
                },
                "branches": []
            })

        # Append the new combined branch under "combined_topics"
        if "combined_topics" not in topic_tree:
            topic_tree["combined_topics"] = []
        topic_tree["combined_topics"].append(combined_branch)

    elif update_type == "general_follow_up":
        # Update the current node by appending the user's question and GPT's answer
        def find_and_update_follow_up(node):
            if isinstance(node, list):
                for item in node:
                    if find_and_update_follow_up(item):
                        return True
            else:
                if node["topic"].get("branch") == current_topic[0]:
                    # Append user's question and GPT's answer to the existing bud
                    existing_bud = node["topic"].get("bud", "")
                    new_answer = gpt_json.get("answer", "")
                    updated_bud = f"{existing_bud}\n\nUser Follow-up: {user_query}\nGPT Answer: {new_answer}"
                    node["topic"]["bud"] = updated_bud
                    return True
                # Recursively search branches
                for branch in node.get("branches", []):
                    if find_and_update_follow_up(branch):
                        return True
            return False

        # Update the current topic to False for all nodes
        def set_all_current_to_false(node):
            if isinstance(node, list):
                for item in node:
                    set_all_current_to_false(item)
            else:
                node["topic"]["current"] = False
                for branch in node.get("branches", []):
                    set_all_current_to_false(branch)

        set_all_current_to_false(topic_tree["root"])
        if "combined_topics" in topic_tree:
            set_all_current_to_false(topic_tree["combined_topics"])
        
        # Find the current node and update it
        find_and_update_follow_up(topic_tree["root"])
        if "combined_topics" in topic_tree:
            find_and_update_follow_up(topic_tree["combined_topics"])

    else:
        raise ValueError("Unknown update type.")

    return topic_tree


# BRAINSTORM/EXPLANATION:

# Here we want to abstract away the creation and updating of the tree
# The tree develops as follows:
    # Initial response creates the root and generates the initial topic name (branch), bud, and first branches
        # The root topic is now the current topic, and has it's 'current_topic' flag set to 'True'
        # Each branch is initialized with only the topic name (branch)
    # If the user selects a new branch to drill down on, that branch info is filled in following the response. For instance, if a user initially asks about dot products, the tree will look as follows:

# {
#   "root": {
#     "topic": {
#       "branch": "Machine Learning Overview",
#       "bud": "Machine learning is a field of artificial intelligence that allows computers to learn from data and make decisions without being explicitly programmed. It involves various algorithms and approaches such as supervised learning, unsupervised learning, and reinforcement learning.",
#       "related_topics": [],
#       "relationship_query": None,
#       "current": True
#     },
#     "branches": [
#       {
#         "topic": {
#           "branch": "Supervised Learning",
#           "bud": None,
#           "related_topics": [],
#           "relationship_query": None,
#           "current": False
#         },
#         "branches": []
#       },
#       {
#         "topic": {
#           "branch": "Unsupervised Learning",
#           "bud": None,
#           "related_topics": [],
#           "relationship_query": None,
#           "current": False
#         },
#         "branches": []
#       },
#       {
#         "topic": {
#           "branch": "Dot Products in Machine Learning",
#           "bud": None,
#           "related_topics": [],
#           "relationship_query": None,
#           "current": True
#         },
#         "branches": []
#       }
#     ]
#   }
# }

# # THEN, if the user selects one of the sub-topics to dive into further (in this case, say they chose 'Supervised Learning'):
#     # 1) that topic's 'current' flag is set to True
#     # 2) we send GPT the query and get a response
#     # 3) the 'branches' value of that topic is fleshed out with new sub-topics based on GPT's response JSON. For instance, if the user subsequently selects the 'Supervised Learning' branch, the tree will be updated to look as follows:

# {
#   "root": {
#     "topic": {
#       "branch": "Machine Learning Overview",
#       "bud": "Machine learning is a field of artificial intelligence that allows computers to learn from data and make decisions without being explicitly programmed. It involves various algorithms and approaches such as supervised learning, unsupervised learning, and reinforcement learning.",
#       "related_topics": [],
#       "relationship_query": None,
#       "current": False
#     },
#     "branches": [
#       {
#         "topic": {
#           "branch": "Supervised Learning",
#           "bud": "Supervised learning involves using labeled datasets to train models. These models are then able to make predictions based on new, unseen data. Examples include linear regression, logistic regression, and classification models.",
#           "related_topics": [],
#           "relationship_query": None,
#           "current": True
#         },
#         "branches": [
#           {
#             "topic": {
#               "branch": "Semi supervised learning",
#               "bud": None,
#               "related_topics": [],
#               "relationship_query": None,
#               "current": False
#             },
#             "branches": []
#           },
#           {
#             "topic": {
#               "branch": "Fully supervised learning",
#               "bud": None,
#               "related_topics": [],
#               "relationship_query": None,
#               "current": False
#             },
#             "branches": []
#           },
#           {
#             "topic": {
#               "branch": "Linear Regression",
#               "bud": None,
#               "related_topics": [],
#               "relationship_query": None,
#               "current": False
#             },
#             "branches": []
#           }
#         ]
#       },
#       {
#         "topic": {
#           "branch": "Unsupervised Learning",
#           "bud": None,
#           "related_topics": [],
#           "relationship_query": None,
#           "current": False
#         },
#         "branches": []
#       },
#       {
#         "topic": {
#           "branch": "Dot Products in Machine Learning",
#           "bud": None,
#           "related_topics": [],
#           "relationship_query": None,
#           "current": False
#         },
#         "branches": []
#       }
#     ]
#   }
# }


# Note that the 'bud' values are only filled out once the topic is the subject of its own query. Topics are initialized with just the 'branch' topic name. 

# In general, there are 4 possible scenarios for how the tree should be updated:
    # 1) The initialization of the tree (first message from the user), which creates the root, first topic's title and bud, and sub topics
    # 2) The user drills down on a single topic, which updates the current topic flag, gets a response from GPT, fills out the 'bud' (full answer on the topic), and expands the tree by generating that topic's sub-topics
    # 3) The user drills down on multiple topics, which updates the 'related_topics' value of the topics in question to include the branch names that the user selected together, adds the user's query about the relationship to the 'relationship_query' field of those topics, gets a response from GPT, and creates a new branch under the 'combined_topics' section of the tree.
    # 4) The user asks a new question without drilling down, which creates a new 'root' branch in the tree