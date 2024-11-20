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

topic_tree_after_initialization_sddnq_sddwq_multidrill = {
    "root": {
        "topic": {
            "branch": [
                "Existentialism"
            ],
            "bud": "Existentialism is a philosophical movement that emerged in the 19th and 20th centuries, focusing on individual freedom, choice, and existence. It emphasizes the idea that humans are free and responsible for their own actions in a world that is often irrational or meaningless. Existentialists believe that individuals must create their own sense of purpose and values in life, rather than relying on external sources such as religion or societal norms. Key figures in existentialism include philosophers like S\u00f8ren Kierkegaard, Friedrich Nietzsche, Jean-Paul Sartre, and Albert Camus, each contributing unique perspectives to the understanding of human existence.\n\nUser Follow-up: How does god factor in?\nGPT Answer: In existentialism, the concept of God is often approached with skepticism or redefined in ways that emphasize human freedom and responsibility. Key existentialist thinkers have varied perspectives on the role of God in human existence. For instance, S\u00f8ren Kierkegaard, often considered the father of existentialism, was a Christian existentialist who believed that faith in God was a personal choice that involved a 'leap of faith' beyond rational evidence. Kierkegaard saw this leap as essential to authentic existence. In contrast, Friedrich Nietzsche famously declared 'God is dead,' suggesting that the traditional, religious framework was no longer viable in the modern world. Nietzsche argued that humans must create their own values in the absence of divine authority. Jean-Paul Sartre, an atheist existentialist, posited that without God, humans are 'condemned to be free,' meaning they must take full responsibility for their actions and the creation of meaning in their lives. Albert Camus, while not explicitly focusing on God, explored the 'absurd,' the conflict between humans' search for meaning and the indifferent universe. In this context, belief in God could be seen as one of many possible responses to the absurd. Overall, existentialism often challenges traditional religious views, emphasizing human autonomy and the subjective creation of meaning.\n\nUser Follow-up: Can you explain the 'humans are condemned to be free' line a bit more?\nGPT Answer: The phrase 'humans are condemned to be free' is a central tenet of Jean-Paul Sartre's existential philosophy. Sartre argued that in the absence of a divine creator, humans are left without a predetermined essence or purpose. This lack of inherent meaning means that individuals must create their own essence through their actions. The 'condemnation' comes from the fact that this freedom is inescapable; we are thrown into existence and must choose how to live, which can be a daunting and burdensome responsibility. This freedom demands that we take full accountability for our choices and the values we adopt, as there is no higher power to dictate what is right or wrong. Thus, while freedom is often seen as a positive aspect, Sartre highlights the weight and anxiety that accompany the necessity of constant choice and self-definition in a world without inherent meaning.",
            "related_topics": [],
            "relationship_query": None,
            "current": False
        },
        "branches": [
            {
                "topic": {
                    "branch": "Key figures in existentialism",
                    "bud": None,
                    "related_topics": [],
                    "relationship_query": None,
                    "current": False
                },
                "branches": []
            },
            {
                "topic": {
                    "branch": "Existentialism and the concept of absurdity",
                    "bud": "Existentialism is a philosophical movement that explores the nature of human existence, freedom, and choice. A central theme within existentialism is the concept of 'absurdity,' which refers to the conflict between humans' natural tendency to seek inherent value and meaning in life and the silent, indifferent universe that offers none. This idea is most prominently discussed in the works of existentialist thinkers like Albert Camus, who argued that life is absurd because it lacks meaning, yet humans continue to search for it. Camus famously illustrated this through the myth of Sisyphus, where Sisyphus is condemned to roll a boulder up a hill only to watch it roll back down, symbolizing the futile search for meaning. Despite this, Camus suggested that individuals must embrace the absurd condition of life while simultaneously revolting against it by finding personal meaning and joy in their existence. This paradox of embracing the absurd while seeking meaning is a cornerstone of existential thought, challenging individuals to live authentically and embrace their freedom and responsibility.",
                    "related_topics": [],
                    "relationship_query": None,
                    "current": False
                },
                "branches": [
                    {
                        "topic": {
                            "branch": "Albert Camus and the Myth of Sisyphus",
                            "bud": None,
                            "related_topics": [],
                            "relationship_query": None,
                            "current": False
                        },
                        "branches": []
                    },
                    {
                        "topic": {
                            "branch": "Existential freedom and responsibility",
                            "bud": "User query: do I have a responsibility to be free? Answer: In existentialism, particularly in the works of philosophers like Jean-Paul Sartre, the concept of existential freedom is deeply intertwined with responsibility. Sartre famously declared that 'existence precedes essence,' meaning that individuals are not born with a predefined purpose or essence; rather, they must create it through their actions. This freedom to choose one's path is a fundamental aspect of human existence. However, with this freedom comes the weight of responsibility. Sartre argues that because we are free to make choices, we are also responsible for the consequences of those choices, not only for ourselves but also for the impact they have on others. This responsibility can be daunting, as it implies that we cannot blame our actions on fate, society, or any external forces. Instead, we must own our decisions and the essence we create through them. Thus, in existentialist thought, you do have a responsibility to embrace your freedom and the accountability that comes with it.",
                            "related_topics": [],
                            "relationship_query": None,
                            "current": False
                        },
                        "branches": [
                            {
                                "topic": {
                                    "branch": "Jean-Paul Sartre's concept of 'bad faith'",
                                    "bud": None,
                                    "related_topics": [],
                                    "relationship_query": None,
                                    "current": False
                                },
                                "branches": []
                            },
                            {
                                "topic": {
                                    "branch": "The relationship between freedom and authenticity in existentialism",
                                    "bud": None,
                                    "related_topics": [],
                                    "relationship_query": None,
                                    "current": False
                                },
                                "branches": []
                            },
                            {
                                "topic": {
                                    "branch": "Comparisons between existential freedom and determinism",
                                    "bud": None,
                                    "related_topics": [],
                                    "relationship_query": None,
                                    "current": False
                                },
                                "branches": []
                            }
                        ]
                    },
                    {
                        "topic": {
                            "branch": "The role of absurdity in existential literature",
                            "bud": None,
                            "related_topics": [],
                            "relationship_query": None,
                            "current": False
                        },
                        "branches": []
                    }
                ]
            },
            {
                "topic": {
                    "branch": "Existentialism in literature and art",
                    "bud": None,
                    "related_topics": [],
                    "relationship_query": None,
                    "current": False
                },
                "branches": []
            }
        ]
    },
    "combined_topics": [
        {
            "topic": {
                "branch": "'Bad Faith' in Existentialist Art",
                "bud": "In existentialist art, the concept of 'bad faith,' as proposed by Jean-Paul Sartre, manifests through characters or subjects that deceive themselves to escape the anxiety associated with absolute freedom and responsibility. Artists and writers often portray individuals in existential crises, illustrating how they succumb to societal roles or external definitions of identity to avoid confronting the true nature of their existence. This theme can be seen in characters who live inauthentically, conforming to expectations rather than embracing their freedom to define their essence. In literature and visual arts, this might be depicted through narrative choices, character development, or visual symbolism that emphasize the struggle between authenticity and self-deception.",
                "related_topics": [
                    "Existentialism in literature and art",
                    "Jean-Paul Sartre's concept of 'bad faith'"
                ],
                "relationship_query": "How does the concept of 'bad faith' manifest in existentialist art?",
                "current": True
            },
            "branches": [
                {
                    "topic": {
                        "branch": "Existential themes in modernist literature and painting",
                        "bud": None,
                        "related_topics": [],
                        "relationship_query": None,
                        "current": False
                    },
                    "branches": []
                },
                {
                    "topic": {
                        "branch": "Symbolism of freedom and self-deception in visual arts",
                        "bud": None,
                        "related_topics": [],
                        "relationship_query": None,
                        "current": False
                    },
                    "branches": []
                },
                {
                    "topic": {
                        "branch": "Role of societal norms in shaping existential crises in art",
                        "bud": None,
                        "related_topics": [],
                        "relationship_query": None,
                        "current": False
                    },
                    "branches": []
                }
            ]
        }
    ]
}

initialize_then_general_then_sddnq_then_sddwq_tree = {
    "root": {
        "topic": {
            "branch": [
                "Existentialism"
            ],
            "bud": "Existentialism is a philosophical movement that emerged in the 19th and 20th centuries, focusing on individual freedom, choice, and existence. It emphasizes the idea that humans are free and responsible for their own actions in a world that is often irrational or meaningless. Existentialists believe that individuals must create their own sense of purpose and values in life, rather than relying on external sources such as religion or societal norms. Key figures in existentialism include philosophers like S\u00f8ren Kierkegaard, Friedrich Nietzsche, Jean-Paul Sartre, and Albert Camus, each contributing unique perspectives to the understanding of human existence.\n\nUser Follow-up: How does god factor in?\nGPT Answer: In existentialism, the concept of God is often approached with skepticism or redefined in ways that emphasize human freedom and responsibility. Key existentialist thinkers have varied perspectives on the role of God in human existence. For instance, S\u00f8ren Kierkegaard, often considered the father of existentialism, was a Christian existentialist who believed that faith in God was a personal choice that involved a 'leap of faith' beyond rational evidence. Kierkegaard saw this leap as essential to authentic existence. In contrast, Friedrich Nietzsche famously declared 'God is dead,' suggesting that the traditional, religious framework was no longer viable in the modern world. Nietzsche argued that humans must create their own values in the absence of divine authority. Jean-Paul Sartre, an atheist existentialist, posited that without God, humans are 'condemned to be free,' meaning they must take full responsibility for their actions and the creation of meaning in their lives. Albert Camus, while not explicitly focusing on God, explored the 'absurd,' the conflict between humans' search for meaning and the indifferent universe. In this context, belief in God could be seen as one of many possible responses to the absurd. Overall, existentialism often challenges traditional religious views, emphasizing human autonomy and the subjective creation of meaning.\n\nUser Follow-up: Can you explain the 'humans are condemned to be free' line a bit more?\nGPT Answer: The phrase 'humans are condemned to be free' is a central tenet of Jean-Paul Sartre's existential philosophy. Sartre argued that in the absence of a divine creator, humans are left without a predetermined essence or purpose. This lack of inherent meaning means that individuals must create their own essence through their actions. The 'condemnation' comes from the fact that this freedom is inescapable; we are thrown into existence and must choose how to live, which can be a daunting and burdensome responsibility. This freedom demands that we take full accountability for our choices and the values we adopt, as there is no higher power to dictate what is right or wrong. Thus, while freedom is often seen as a positive aspect, Sartre highlights the weight and anxiety that accompany the necessity of constant choice and self-definition in a world without inherent meaning.",
            "related_topics": [],
            "relationship_query": None,
            "current": False
        },
        "branches": [
            {
                "topic": {
                    "branch": "Key figures in existentialism",
                    "bud": None,
                    "related_topics": [],
                    "relationship_query": None,
                    "current": False
                },
                "branches": []
            },
            {
                "topic": {
                    "branch": "Existentialism and the concept of absurdity",
                    "bud": "Existentialism is a philosophical movement that explores the nature of human existence, freedom, and choice. A central theme within existentialism is the concept of 'absurdity,' which refers to the conflict between humans' natural tendency to seek inherent value and meaning in life and the silent, indifferent universe that offers none. This idea is most prominently discussed in the works of existentialist thinkers like Albert Camus, who argued that life is absurd because it lacks meaning, yet humans continue to search for it. Camus famously illustrated this through the myth of Sisyphus, where Sisyphus is condemned to roll a boulder up a hill only to watch it roll back down, symbolizing the futile search for meaning. Despite this, Camus suggested that individuals must embrace the absurd condition of life while simultaneously revolting against it by finding personal meaning and joy in their existence. This paradox of embracing the absurd while seeking meaning is a cornerstone of existential thought, challenging individuals to live authentically and embrace their freedom and responsibility.",
                    "related_topics": [],
                    "relationship_query": None,
                    "current": False
                },
                "branches": [
                    {
                        "topic": {
                            "branch": "Albert Camus and the Myth of Sisyphus",
                            "bud": None,
                            "related_topics": [],
                            "relationship_query": None,
                            "current": False
                        },
                        "branches": []
                    },
                    {
                        "topic": {
                            "branch": "Existential freedom and responsibility",
                            "bud": "User query: do I have a responsibility to be free? Answer: In existentialism, particularly in the works of philosophers like Jean-Paul Sartre, the concept of existential freedom is deeply intertwined with responsibility. Sartre famously declared that 'existence precedes essence,' meaning that individuals are not born with a predefined purpose or essence; rather, they must create it through their actions. This freedom to choose one's path is a fundamental aspect of human existence. However, with this freedom comes the weight of responsibility. Sartre argues that because we are free to make choices, we are also responsible for the consequences of those choices, not only for ourselves but also for the impact they have on others. This responsibility can be daunting, as it implies that we cannot blame our actions on fate, society, or any external forces. Instead, we must own our decisions and the essence we create through them. Thus, in existentialist thought, you do have a responsibility to embrace your freedom and the accountability that comes with it.",
                            "related_topics": [],
                            "relationship_query": None,
                            "current": True
                        },
                        "branches": [
                            {
                                "topic": {
                                    "branch": "Jean-Paul Sartre's concept of 'bad faith'",
                                    "bud": None,
                                    "related_topics": [],
                                    "relationship_query": None,
                                    "current": False
                                },
                                "branches": []
                            },
                            {
                                "topic": {
                                    "branch": "The relationship between freedom and authenticity in existentialism",
                                    "bud": None,
                                    "related_topics": [],
                                    "relationship_query": None,
                                    "current": False
                                },
                                "branches": []
                            },
                            {
                                "topic": {
                                    "branch": "Comparisons between existential freedom and determinism",
                                    "bud": None,
                                    "related_topics": [],
                                    "relationship_query": None,
                                    "current": False
                                },
                                "branches": []
                            }
                        ]
                    },
                    {
                        "topic": {
                            "branch": "The role of absurdity in existential literature",
                            "bud": None,
                            "related_topics": [],
                            "relationship_query": None,
                            "current": False
                        },
                        "branches": []
                    }
                ]
            },
            {
                "topic": {
                    "branch": "Existentialism in literature and art",
                    "bud": None,
                    "related_topics": [],
                    "relationship_query": None,
                    "current": False
                },
                "branches": []
            }
        ]
    }
}

initialize_then_general_then_single_drillnoquery_tree = {
    "root": {
        "topic": {
            "branch": [
                "Existentialism"
            ],
            "bud": "Existentialism is a philosophical movement that emerged in the 19th and 20th centuries, focusing on individual freedom, choice, and existence. It emphasizes the idea that humans are free and responsible for their own actions in a world that is often irrational or meaningless. Existentialists believe that individuals must create their own sense of purpose and values in life, rather than relying on external sources such as religion or societal norms. Key figures in existentialism include philosophers like S\u00f8ren Kierkegaard, Friedrich Nietzsche, Jean-Paul Sartre, and Albert Camus, each contributing unique perspectives to the understanding of human existence.\n\nUser Follow-up: How does god factor in?\nGPT Answer: In existentialism, the concept of God is often approached with skepticism or redefined in ways that emphasize human freedom and responsibility. Key existentialist thinkers have varied perspectives on the role of God in human existence. For instance, S\u00f8ren Kierkegaard, often considered the father of existentialism, was a Christian existentialist who believed that faith in God was a personal choice that involved a 'leap of faith' beyond rational evidence. Kierkegaard saw this leap as essential to authentic existence. In contrast, Friedrich Nietzsche famously declared 'God is dead,' suggesting that the traditional, religious framework was no longer viable in the modern world. Nietzsche argued that humans must create their own values in the absence of divine authority. Jean-Paul Sartre, an atheist existentialist, posited that without God, humans are 'condemned to be free,' meaning they must take full responsibility for their actions and the creation of meaning in their lives. Albert Camus, while not explicitly focusing on God, explored the 'absurd,' the conflict between humans' search for meaning and the indifferent universe. In this context, belief in God could be seen as one of many possible responses to the absurd. Overall, existentialism often challenges traditional religious views, emphasizing human autonomy and the subjective creation of meaning.\n\nUser Follow-up: Can you explain the 'humans are condemned to be free' line a bit more?\nGPT Answer: The phrase 'humans are condemned to be free' is a central tenet of Jean-Paul Sartre's existential philosophy. Sartre argued that in the absence of a divine creator, humans are left without a predetermined essence or purpose. This lack of inherent meaning means that individuals must create their own essence through their actions. The 'condemnation' comes from the fact that this freedom is inescapable; we are thrown into existence and must choose how to live, which can be a daunting and burdensome responsibility. This freedom demands that we take full accountability for our choices and the values we adopt, as there is no higher power to dictate what is right or wrong. Thus, while freedom is often seen as a positive aspect, Sartre highlights the weight and anxiety that accompany the necessity of constant choice and self-definition in a world without inherent meaning.",
            "related_topics": [],
            "relationship_query": None,
            "current": False
        },
        "branches": [
            {
                "topic": {
                    "branch": "Key figures in existentialism",
                    "bud": None,
                    "related_topics": [],
                    "relationship_query": None,
                    "current": False
                },
                "branches": []
            },
            {
                "topic": {
                    "branch": "Existentialism and the concept of absurdity",
                    "bud": "Existentialism is a philosophical movement that explores the nature of human existence, freedom, and choice. A central theme within existentialism is the concept of 'absurdity,' which refers to the conflict between humans' natural tendency to seek inherent value and meaning in life and the silent, indifferent universe that offers none. This idea is most prominently discussed in the works of existentialist thinkers like Albert Camus, who argued that life is absurd because it lacks meaning, yet humans continue to search for it. Camus famously illustrated this through the myth of Sisyphus, where Sisyphus is condemned to roll a boulder up a hill only to watch it roll back down, symbolizing the futile search for meaning. Despite this, Camus suggested that individuals must embrace the absurd condition of life while simultaneously revolting against it by finding personal meaning and joy in their existence. This paradox of embracing the absurd while seeking meaning is a cornerstone of existential thought, challenging individuals to live authentically and embrace their freedom and responsibility.",
                    "related_topics": [],
                    "relationship_query": None,
                    "current": True
                },
                "branches": [
                    {
                        "topic": {
                            "branch": "Albert Camus and the Myth of Sisyphus",
                            "bud": None,
                            "related_topics": [],
                            "relationship_query": None,
                            "current": False
                        },
                        "branches": []
                    },
                    {
                        "topic": {
                            "branch": "Existential freedom and responsibility",
                            "bud": None,
                            "related_topics": [],
                            "relationship_query": None,
                            "current": False
                        },
                        "branches": []
                    },
                    {
                        "topic": {
                            "branch": "The role of absurdity in existential literature",
                            "bud": None,
                            "related_topics": [],
                            "relationship_query": None,
                            "current": False
                        },
                        "branches": []
                    }
                ]
            },
            {
                "topic": {
                    "branch": "Existentialism in literature and art",
                    "bud": None,
                    "related_topics": [],
                    "relationship_query": None,
                    "current": False
                },
                "branches": []
            }
        ]
    }
}

initialize_then_general_follow_up_tree = {
    "root": {
        "topic": {
            "branch": [
                "Existentialism"
            ],
            "bud": "Existentialism is a philosophical movement that emerged in the 19th and 20th centuries, focusing on individual freedom, choice, and existence. It emphasizes the idea that humans are free and responsible for their own actions in a world that is often irrational or meaningless. Existentialists believe that individuals must create their own sense of purpose and values in life, rather than relying on external sources such as religion or societal norms. Key figures in existentialism include philosophers like S\u00f8ren Kierkegaard, Friedrich Nietzsche, Jean-Paul Sartre, and Albert Camus, each contributing unique perspectives to the understanding of human existence.\n\nUser Follow-up: How does god factor in?\nGPT Answer: In existentialism, the concept of God is often approached with skepticism or redefined in ways that emphasize human freedom and responsibility. Key existentialist thinkers have varied perspectives on the role of God in human existence. For instance, S\u00f8ren Kierkegaard, often considered the father of existentialism, was a Christian existentialist who believed that faith in God was a personal choice that involved a 'leap of faith' beyond rational evidence. Kierkegaard saw this leap as essential to authentic existence. In contrast, Friedrich Nietzsche famously declared 'God is dead,' suggesting that the traditional, religious framework was no longer viable in the modern world. Nietzsche argued that humans must create their own values in the absence of divine authority. Jean-Paul Sartre, an atheist existentialist, posited that without God, humans are 'condemned to be free,' meaning they must take full responsibility for their actions and the creation of meaning in their lives. Albert Camus, while not explicitly focusing on God, explored the 'absurd,' the conflict between humans' search for meaning and the indifferent universe. In this context, belief in God could be seen as one of many possible responses to the absurd. Overall, existentialism often challenges traditional religious views, emphasizing human autonomy and the subjective creation of meaning.",
            "related_topics": [],
            "relationship_query": None,
            "current": True
        },
        "branches": [
            {
                "topic": {
                    "branch": "Key figures in existentialism",
                    "bud": None,
                    "related_topics": [],
                    "relationship_query": None,
                    "current": False
                },
                "branches": []
            },
            {
                "topic": {
                    "branch": "Existentialism and the concept of absurdity",
                    "bud": None,
                    "related_topics": [],
                    "relationship_query": None,
                    "current": False
                },
                "branches": []
            },
            {
                "topic": {
                    "branch": "Existentialism in literature and art",
                    "bud": None,
                    "related_topics": [],
                    "relationship_query": None,
                    "current": False
                },
                "branches": []
            }
        ]
    }
}



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