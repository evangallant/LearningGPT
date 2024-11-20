# Update the topic tree
    # HERE WE NEED TO MAKE SURE TO USE 'None', NOT 'Null' FOR EMPTY VALUES

# Convert a full topic tree to the lite bracketed format
def convert_to_bracketed(tree, is_current=False):
    def traverse(node, current_marker=""):
        # Extract the topic name and whether it's the current topic
        topic_name = node["topic"].get("branch", "")
        current_marker = "*" if node["topic"].get("current", False) else ""

        # Start the representation for this topic
        result = f"{topic_name}{current_marker}"

        # Process children branches if they exist
        branches = node.get("branches", [])
        if branches:
            result += " ["
            sub_topics = []
            for branch in branches:
                sub_topics.append(traverse(branch))
            result += ", ".join(sub_topics)
            result += "]"
        else:
            result += " []"

        # Handle relationship_query if it exists and is not null
        relationship_query = node.get("relationship_query", None)
        if relationship_query:
            result += f" (Relationship: {relationship_query})"

        return result

    # Start from the root of the topic tree
    return traverse(tree["root"])

def find_current_topic(node):
    """
    Recursively finds the current topic in the topic tree.
    
    Args:
        node (dict): The current node of the topic tree.
        
    Returns:
        dict: The dictionary of the current topic or None if not found.
    """
    # Check if the current node is marked as current
    if node["topic"].get("current", False):
        return node

    # Recursively check each branch if it exists
    for branch in node.get("branches", []):
        current_topic = find_current_topic(branch)
        if current_topic:
            return current_topic

    # If not found in the current node or branches, return None
    return None



sample_topic_tree = {
  "root": {
    "topic": {
      "branch": "Machine Learning Overview",
      "bud": "Machine learning is a field of artificial intelligence that allows computers to learn from data and make decisions without being explicitly programmed. It involves various algorithms and approaches such as supervised learning, unsupervised learning, and reinforcement learning.",
      "related_topics": [],
      "relationship_query": None,
      "current": False
    },
    "branches": [
      {
        "topic": {
          "branch": "Supervised Learning",
          "bud": "Supervised learning involves using labeled datasets to train models. These models are then able to make predictions based on new, unseen data. Examples include linear regression, logistic regression, and classification models.",
          "related_topics": [],
          "relationship_query": None,
          "current": False
        },
        "branches": [
          {
            "topic": {
              "branch": "Linear Regression",
              "bud": "Linear regression is a supervised learning algorithm used to predict continuous values based on input features. It works by finding a line that best fits the data points, minimizing the error between predicted and actual values.",
              "related_topics": [],
              "relationship_query": None,
              "current": False
            },
            "branches": [
              {
                "topic": {
                  "branch": "Gradient Descent in Linear Regression",
                  "bud": "Gradient descent is an optimization algorithm used to minimize the cost function in linear regression by iteratively adjusting the model parameters to find the optimal fit.",
                  "related_topics": [],
                  "relationship_query": None,
                  "current": False
                },
                "branches": []
              }
            ]
          }
        ]
      },
      {
        "topic": {
          "branch": "Unsupervised Learning",
          "bud": "Unsupervised learning involves using unlabeled datasets to find hidden patterns or structures within data. Examples include clustering algorithms like K-means and dimensionality reduction techniques like PCA.",
          "related_topics": [],
          "relationship_query": None,
          "current": False
        },
        "branches": []
      },
      {
        "topic": {
          "branch": "Dot Products in Machine Learning",
          "bud": "Dot products are used in machine learning to calculate the similarity between vectors, which is fundamental for various tasks, including classification and feature extraction.",
          "related_topics": [],
          "relationship_query": None,
          "current": True
        },
        "branches": [
          {
            "topic": {
              "branch": "Role of Dot Products in Neural Networks",
              "bud": "In neural networks, dot products are used in the forward pass to calculate the weighted sum of the inputs for each neuron. This operation helps the network understand how different features combine to predict an output.",
              "related_topics": [],
              "relationship_query": None,
              "current": False
            },
            "branches": []
          },
          {
            "topic": {
              "branch": "Dot Product as a Measure of Similarity",
              "bud": "The dot product can be used to measure the similarity between two vectors. This is particularly useful in natural language processing (NLP) for tasks such as word embeddings, where the dot product helps determine how similar two word vectors are.",
              "related_topics": [],
              "relationship_query": None,
              "current": False
            },
            "branches": []
          }
        ]
      }
    ]
  },
  "combined_topics": [
    {
      "topic": {
        "branch": "Linear Algebra and CNNs",
        "bud": "Linear algebra concepts, such as matrix operations, underlie the implementation of Convolutional Neural Networks (CNNs). In CNNs, image data is represented as matrices, and convolution operations are performed through matrix multiplications.",
        "related_topics": [
          "Linear Regression",
          "Convolutional Neural Networks"
        ],
        "relationship_query": "How do linear algebra concepts underpin Convolutional Neural Networks?",
        "current": False
      },
      "branches": []
    }
  ]
}


# Example lite topic tree:
example_lite_tree = """Machine Learning Overview [  Supervised Learning [    Linear Regression [      Gradient Descent in Linear Regression []
    ]
  ],
  Unsupervised Learning [],
  Dot Products in Machine Learning* [    Role of Dot Products in Neural Networks [],
    Dot Product as a Measure of Similarity []
  ]
]

Combined Topics [  Linear Algebra and CNNs []
]"""