# LearningGPT 

The idea is to make use of ChatGPT's unique ability to patiently drill down on topics
Developing a holistic understanding of the foundation of a topic is the best way to set yourself up to learn more.


## GENERAL PROCESS

**Primary input:**
- User asks a question about a subject

**Primary output:**
- A section-ized response, where the user can select one section to drill down on
- Here, we warp the input with a prompt that yields a sectioned response, with a main explanation and sections which each have a relevant topic that the user may want to drill down on for better understanding.
- The **TOPIC** is the building block of this system.

**Subsequent input (drill down - one TOPIC):**
- A user may read through the main response, understand some sections, but need more detail on a given **TOPIC**
- The user selects that section by clicking on it, then can input a question, which will be bundled together.
- We get a response by providing the topic tree, question, and prompt wrapper indicating which topic to drill down on.

**Subsequent input (drill down - multiple TOPICs):**
- Same process as with the single topic, but we offer the user an option to select multiple **TOPICs**
- An input box will appear where the user writes a query about the relationship between multiple topics, OR select from a set of predefined relationship queries, such as:
    - "Explain how these topics are related"
    - "How does [Topic A] provide a foundation for understanding [Topic B]?"
    - "What are the key concepts in [Topic A] that are directly applied in [Topic B]?"
  - Here, we should aim for variable-ized topics so the user can plug in selected topics into the boilerplate queries.
- We get a response by providing the topic tree, query, and prompt wrapper indicating which **TOPICs** the questions correspond to.


## FEATURES

**Topic history:**
- It's easy to get lost in a rabbit hole of understanding the foundation of a topic.
- We can avoid that by building a navigable exploration tree of **TOPICs**. Each main query generates a series of **TOPICs**. The user has the ability to drill down on any of these topics, branching the tree.
- If the user selects multiple topics, the branches can merge:
  - From one main **TOPIC**, picking two children of that topic merges them into a single drill down.
  - Users can merge topics from other branches to understand relationships between topics, within the context of the main line of inquiry.

**UI:**
- **Initial input:** Text (and maybe image) input, with instructions on prompting for understanding/learning.
- **Main interaction window:**
  - Nav tree (left 1/4 of window) + conversation list.
  - Output window (right 3/4 of window):
    - Initial output after question: Response, split up into topics that are themselves big buttons.
    - If the user selects one or multiple topics, either by clicking the topic buttons in the response, or by clicking a node in the nav tree, an input for each topic will appear at the bottom of the screen.
    - Once the user has followed up about each topic, they can save the query and add it to their response.
    - Thus, the response will either include:
      1. A general follow-up, if the user didn't select a topic to drill down on (for instance if they switched topics or understood everything in the answer), or
      2. One or more topic/query pairs to drill down on, and optionally a general input text, where the user could, for instance, ask about the relationship between the two topics.


## DATA STRUCTURES:
- **Topic:** The fundamental unit of the system. It is composed of 2 key/value pairs, as well as a marker which says if this is the current topic in question. Key/value pairs: 
  - **First:**
    - **"branch"**: A topic, i.e. a short explanation from original response.
    - **"bud"**: An explanation, i.e. the full response from GPT.
  - **Second:** 
    - **"related topics"**: references to other topics which the user combined together to form a new bud
    - **"relationship query"**: the user's query as to the relationship between the related topics (if applicable), 
- **Topic tree:** A navigable tree of topics. Its root is the initial prompt the user started with.
  - Topics are generated from the initial prompt, becoming the first branches of the tree.
  - If a user selects one topic to drill down on, that branch grows a bud (a deeper explanation of that topic) as well as branches (relevant topics in the explanation that the user can further drill down on).
  - For multiple topics, multiple branches join together into one bud, then branch into relevant new topics.
  - The user can optionally input an additional prompt regarding the relationship between multiple branches, giving the new bud richer context.
  - If a user doesn't select any topics and just asks a new question, a new root is made (like an aspen, it sends up a separate shoot with its own new branches, rather than going deeper into the existing tree).
  - EXAMPLE TOPIC TREE AT END OF PAGE
- **Lite Topic tree:** This is a lightweight version of the full topic tree that we can pass as context along with queries. It will only contain the branches - not the text-heavy buds, nor the relationships.


## PROMPTS
# Which prompt is used is based on:
  # If it is the first query (initial prompt)
  # If the user selects a topic to drill down on
  # If the user supplies a query related to the drill down
  # How many topics the user selects to drill down on at one time

- **Initial prompt:**
  - **Task explanation:** "You are a helpful tutor. Your goal is to improve the user's understanding of the topic in question. Do this by educationally answering the user's question, AND providing 2-3 relevant sub-topics that the user can choose to drill down on to further improve their understanding. You will provide this information in JSON format, following the structure of this example:"
    - Example:
    - **User:** Explain dot products
    - **Response:**
      ```
      {
        "answer": "[An explanation of dot products]",
        "sub_topics": [
          "Geometric interpretation of dot products",
          "The relationship between dot products and vector projection",
          "Applications of dot products in physics and engineering"
        ]
      }
      ```
  - **Query parameters:**
    - **Task explanation** (no topic tree extant yet)
    - **User query** 

- **Subsequent prompts:**
  - **For single topic drill-down:**
    - **WITHOUT ADDITIONAL TOPIC QUERY:**
        - **Task explanation:** "You are a helpful tutor. Your goal is to improve the user's understanding of the topic in question. This is part of an ongoing line of inquiry, defined by this topic tree:
        [topic tree in JSON format, with a marker for which topic we're on]
        The user has asked for a deeper explanation of the following topic. Based on the general line of inquiry, drill down on this topic to help the user understand it, given the context of the other topics in the tree. Provide an educational answer on the topic, AND provide 2-3 relevant sub-topics that the user can choose to drill down on to further improve their understanding. You will provide this information in JSON format, following the structure of this example:"
            - Example:
            - **Current topic:** Dot products
            - **Response:**
            ```
            {
                "answer": "[An explanation of dot products]",
                "sub_topics": [
                "Geometric interpretation of dot products",
                "The relationship between dot products and vector projection",
                "Applications of dot products in physics and engineering"
                ]
            }
            ```
        - **Query parameters:** (just a drill down without an additional query)
            - **Task Explanation + lite Topic tree**
            - **Current topic**

    - **WITH ADDITIONAL TOPIC QUERY:**
        - **Task explanation:** "You are a helpful tutor. Your goal is to improve the user's understanding of the topic in question. This is part of an ongoing line of inquiry, defined by this topic tree:
        [topic tree in JSON format, with a marker for which topic we're on]
        The user has a specific question about the following topic. Answer the user's question, keeping in mind the context of the other topics in the tree. Provide an educational answer, AND provide 2-3 relevant sub-topics that the user can choose to drill down on to further improve their understanding. You will provide this information in JSON format, following the structure of this example:"
            - Example:
            - **Current topic:** Dot products
            - **User query:** Please explain the relationship between dot products and vector projection.
            - **Response:**
            ```
            {
                "answer": "[An explanation of the relationship between dot products and vector projection]",
                "sub_topics": [
                "Derivation of the vector projection formula",
                "Applications of vector projection in real-world scenarios",
                "Understanding the geometric interpretation of vector projection"
                ]
            }
            ```
        - **Query parameters:** (just a drill down without an additional query)
            - **Task Explanation + lite Topic tree**
            - **Current topic**
            - **User query**

  - **For multiple topic drill-down:**
    - **Task explanation:** "You are a helpful tutor. Your goal is to improve the user's understanding of the topic in question. This is part of an ongoing line of inquiry, defined by this topic tree:
    [topic tree in JSON format, with a marker for which topic we're on]
    The user has a question regarding something about the relationship between multiple topics. Given the topics in question, as well as the context of the other topics in the full tree, answer the user's question, AND provide 2-3 relevant sub-topics that the user can choose to drill down on to further improve their understanding. You will provide this information in JSON format, following the structure of this example:"
        - Example:
        - **Current topics:** "Dot products", "Machine learning"
        - **User query:** What are the key concepts in [Dot products] that are directly applied in [Machine learning]?
        - **Response:**
        ```
        {
            "answer": "[An explanation of the key concepts in dot products that are directly applied in machine learing]",
            "sub_topics": [
              "Role of dot products in calculating similarity between feature vectors",
              "Dot products in the weighted sum calculation within neural networks",
              "Application of dot products in optimization algorithms such as gradient descent"
          ]
        }
        ```
    - **Query parameters:**
        - **Task Explanation + lite Topic tree**
        - **Current topics** (comma separated list)
        - **User query**
        
  - **For general follow up:**
    - **Task explanation:** "You are a helpful tutor. Your goal is to improve the user's understanding of the topic in question. This is part of an ongoing line of inquiry, defined by this topic tree:
    [topic tree in JSON format, with a marker for which topic we're on]
    Based on the context of the topic tree, educationally answer the user's question, AND provide 2-3 relevant sub-topics that the user can choose to drill down on to further improve their understanding. You will provide this information in JSON format, following the structure of this example:"
    - Example:
    - **User:** Explain dot products
    - **Response:**
      ```
      {
        "answer": "[An explanation of dot products]",
        "sub_topics": [
          "Geometric interpretation of dot products",
          "The relationship between dot products and vector projection",
          "Applications of dot products in physics and engineering"
        ]
      }
      ```
    - **Query parameters:**
      - **Task explanation + lite topic tree**
      - **User query** 


## Example topic tree:
{
  "root": {
    "topic": {
      "branch": "Machine Learning Overview",
      "bud": "Machine learning is a field of artificial intelligence that allows computers to learn from data and make decisions without being explicitly programmed. It involves various algorithms and approaches such as supervised learning, unsupervised learning, and reinforcement learning.",
      "related_topics": [],
      "relationship_query": null,
      "current": false
    },
    "branches": [
      {
        "topic": {
          "branch": "Supervised Learning",
          "bud": "Supervised learning involves using labeled datasets to train models. These models are then able to make predictions based on new, unseen data. Examples include linear regression, logistic regression, and classification models.",
          "related_topics": [],
          "relationship_query": null,
          "current": false
        },
        "branches": [
          {
            "topic": {
              "branch": "Linear Regression",
              "bud": "Linear regression is a supervised learning algorithm used to predict continuous values based on input features. It works by finding a line that best fits the data points, minimizing the error between predicted and actual values.",
              "related_topics": [],
              "relationship_query": null,
              "current": false
            },
            "branches": [
              {
                "topic": {
                  "branch": "Gradient Descent in Linear Regression",
                  "bud": "Gradient descent is an optimization algorithm used to minimize the cost function in linear regression by iteratively adjusting the model parameters to find the optimal fit.",
                  "related_topics": [],
                  "relationship_query": null,
                  "current": false
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
          "relationship_query": null,
          "current": false
        },
        "branches": []
      },
      {
        "topic": {
          "branch": "Dot Products in Machine Learning",
          "bud": "Dot products are used in machine learning to calculate the similarity between vectors, which is fundamental for various tasks, including classification and feature extraction.",
          "related_topics": [],
          "relationship_query": null,
          "current": true
        },
        "branches": [
          {
            "topic": {
              "branch": "Role of Dot Products in Neural Networks",
              "bud": "In neural networks, dot products are used in the forward pass to calculate the weighted sum of the inputs for each neuron. This operation helps the network understand how different features combine to predict an output.",
              "related_topics": [],
              "relationship_query": null,
              "current": false
            },
            "branches": []
          },
          {
            "topic": {
              "branch": "Dot Product as a Measure of Similarity",
              "bud": "The dot product can be used to measure the similarity between two vectors. This is particularly useful in natural language processing (NLP) for tasks such as word embeddings, where the dot product helps determine how similar two word vectors are.",
              "related_topics": [],
              "relationship_query": null,
              "current": false
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
        "current": false
      },
      "branches": []
    }
  ]
}

# Example lite topic tree:
Machine Learning Overview [  Supervised Learning [    Linear Regression [      Gradient Descent in Linear Regression []
    ]
  ],
  Unsupervised Learning [],
  Dot Products in Machine Learning* [    Role of Dot Products in Neural Networks [],
    Dot Product as a Measure of Similarity []
  ]
]

Combined Topics [  Linear Algebra and CNNs []
]

  # Full topic tree --> lite topic tree conversion:
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

        return result

    # Start from the root of the topic tree
    return traverse(tree["root"])