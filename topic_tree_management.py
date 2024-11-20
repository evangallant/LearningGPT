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

    def set_all_current_to_false(node):
        if isinstance(node, list):
            for item in node:
                set_all_current_to_false(item)
        else:
            if "current" in node["topic"]:  # Make sure the key exists before setting
                node["topic"]["current"] = False
            for branch in node.get("branches", []):
                set_all_current_to_false(branch)

    def find_and_update(node, current_topic, update_func):
        if isinstance(node, list):
            for item in node:
                if find_and_update(item, current_topic, update_func):
                    return True
        else:
            if isinstance(node["topic"].get("branch"), list):
                branch_value = node["topic"].get("branch")[0]  # Extract if it's a list
            else:
                branch_value = node["topic"].get("branch")

            if branch_value == current_topic:
                update_func(node)
                node["topic"]["current"] = True
                return True

            # Recursively search branches
            for branch in node.get("branches", []):
                if find_and_update(branch, current_topic, update_func):
                    return True
        return False

    set_all_current_to_false(topic_tree["root"])
    if "combined_topics" in topic_tree:
        set_all_current_to_false(topic_tree["combined_topics"])

    if update_type == "single_drill_no_query":
        def update_func(node):
            node["topic"]["bud"] = gpt_json.get("answer", "")
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

        find_and_update(topic_tree["root"], current_topic[0], update_func)
        if "combined_topics" in topic_tree:
            find_and_update(topic_tree["combined_topics"], current_topic[0], update_func)

    elif update_type == "single_drill_with_query":
        if not user_query:
            raise ValueError("User query required for single drill with query.")

        def update_func(node):
            node["topic"]["bud"] = "User query: " + user_query + " Answer: " + gpt_json.get("answer", "")
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

        find_and_update(topic_tree["root"], current_topic[0], update_func)
        if "combined_topics" in topic_tree:
            find_and_update(topic_tree["combined_topics"], current_topic[0], update_func)

    elif update_type == "multi_drill":
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

        if "combined_topics" not in topic_tree:
            topic_tree["combined_topics"] = []
        topic_tree["combined_topics"].append(combined_branch)

    elif update_type == "general_follow_up":
        def update_func(node):
            existing_bud = node["topic"].get("bud", "")
            new_answer = gpt_json.get("answer", "")
            updated_bud = f"{existing_bud}\n\nUser Follow-up: {user_query}\nGPT Answer: {new_answer}"
            node["topic"]["bud"] = updated_bud

        find_and_update(topic_tree["root"], current_topic[0], update_func)
        if "combined_topics" in topic_tree:
            find_and_update(topic_tree["combined_topics"], current_topic[0], update_func)

    else:
        raise ValueError("Unknown update type.")

    return topic_tree