# LearningGPT 

The idea is to make use of ChatGPT's unique ability to patiently drill down on topics.
Developing a holistic understanding of the foundation of a topic is the best way to set yourself up to learn more.


## TODO:
- Today: outlined general flow, created prompt generation functions, created topic tree generation functions
- TODO: Figure out order of operations, given a general interaction (initial query, follow up, topic deviance, topic combination, etc.), as well as the processing steps that need to happen between the user's submission --> prompt creation --> API call --> JSON parsing --> tree update --> update what the user sees

## Input/Output Process Overview for LearningGPT

### Step 1: Initial Question from User
- **Input:**
  - **user_query**: e.g., "Can you help me understand logarithms?"
- **Process:**
  1. **Prompt Creation**:
     - Call `create_initial_query(user_query)` to generate the `initial_query`. This function constructs a complete prompt that will guide GPT in providing an answer and suggesting sub-topics.
  2. **Call GPT API**:
     - Call the OpenAI API to get the JSON response (`gpt_json`).
     - **gpt_json Structure**:
       - "answer": (string) The main educational response, e.g., "Logarithms help determine how many times a base number is multiplied to achieve a given value."
       - "topic_name": (string) A brief identifier for the topic, e.g., "Logarithms Overview."
       - "sub_topics": (list of strings) Suggested drill-down topics, e.g., ["Logarithmic rules", "Logarithms in real-world applications", "Base changes in logarithms"]
  3. **Initialize Topic Tree**:
     - Call `initialize_topic_tree(gpt_json)` to create the initial topic tree, structured based on the GPT output.
  4. **Output:**
     - Display the response (main answer), suggested topics, and a visual representation of the topic tree to the user.

### Step 2: User Follows Up with a General Question (General Follow-Up)
- **Input:**
  - **topic_tree**: The current topic tree structure.
  - **user_query**: e.g., "But why are logarithms useful in real life?"
  - **bud**: The content of the current topic node that contains the full educational response.
- **Process:**
  1. **Prompt Creation**:
     - Call `create_general_follow_up(topic_tree, user_query, bud)` to generate a prompt for GPT.
  2. **Call GPT API**:
     - Call the OpenAI API to get a new JSON response (`gpt_json`).
     - **gpt_json Structure**:
       - "answer": (string) The main follow-up response, e.g., "Logarithms are useful for understanding exponential growth, such as population growth, and for simplifying complex multiplication problems in various scientific domains."
  3. **Update Topic Tree**:
     - Call `update_topic_tree(topic_tree, "general_follow_up", gpt_json, current_topic, user_query)` to append the new content to the corresponding topic node.
     - The `current_topic` is derived from the topic tree's current state, specifically finding the node where the `current` flag is set to `True`.
  4. **Output:**
     - Display the updated response, adding the new explanation and highlighting the growth of the knowledge in the topic tree.

### Step 3: User Drills Down into a Specific Topic Without an Additional Query (Single Drill Down Without Query)
- **Input:**
  - **topic_tree**: The current topic tree structure.
  - **current_topic**: e.g., ["Logarithmic rules"] (an array containing the selected topic to drill down into).
- **Process:**
  1. **Prompt Creation**:
     - Call `create_single_topic_drill_down_noquery(topic_tree, current_topic)` to generate a prompt for GPT.
  2. **Call GPT API**:
     - Call the OpenAI API to get the JSON response (`gpt_json`).
     - **gpt_json Structure**:
       - "answer": (string) An in-depth explanation of the chosen topic, e.g., "Logarithmic rules, such as product, quotient, and power rules, help simplify complex logarithmic expressions."
       - "sub_topics": (list of strings) Suggested sub-topics, e.g., ["Product rule of logarithms", "Change of base formula", "Natural logarithms"]
  3. **Update Topic Tree**:
     - Call `update_topic_tree(topic_tree, "single_drill_no_query", gpt_json, current_topic)` to update the current topic with the new answer and add new branches for the sub-topics.
  4. **Output:**
     - Display the updated response, including the in-depth explanation of the chosen topic and new suggested sub-topics.

### Step 4: User Drills Down with a Specific Question (Single Drill Down with Query)
- **Input:**
  - **topic_tree**: The current topic tree structure.
  - **current_topic**: e.g., ["Logarithms in real-world applications"]
  - **user_query**: e.g., "How are logarithms used in audio engineering?"
- **Process:**
  1. **Prompt Creation**:
     - Call `create_single_topic_drill_down_withquery(topic_tree, current_topic, user_query)` to generate a prompt that incorporates the user's specific question.
  2. **Call GPT API**:
     - Call the OpenAI API to get the JSON response (`gpt_json`).
     - **gpt_json Structure**:
       - "answer": (string) e.g., "In audio engineering, logarithms are used to measure sound intensity in decibels, allowing for better perception and control of volume changes."
       - "sub_topics": (list of strings) Suggested sub-topics, e.g., ["Decibels and sound pressure levels", "Frequency response curves", "Application of logarithms in equalizers"]
  3. **Update Topic Tree**:
     - Call `update_topic_tree(topic_tree, "single_drill_with_query", gpt_json, current_topic, user_query)` to update the current topic's `bud` and generate new branches for sub-topics.
  4. **Output:**
     - Display the updated in-depth response, including the answer to the user's question and further suggested topics.

### Step 5: User Wants to Explore Relationships Between Multiple Topics (Multi Drill Down)
- **Input:**
  - **topic_tree**: The current topic tree structure.
  - **current_topics**: e.g., ["Logarithmic rules", "Logarithms in real-world applications"]
  - **user_query**: e.g., "How do logarithmic rules help in simplifying calculations in scientific domains?"
- **Process:**
  1. **Prompt Creation**:
     - Call `create_multiple_topic_drill_down(topic_tree, current_topics, user_query)` to generate a prompt for exploring the relationship between multiple selected topics.
  2. **Call GPT API**:
     - Call the OpenAI API to get the JSON response (`gpt_json`).
     - **gpt_json Structure**:
       - "combined_topic_name": (string) e.g., "Logarithmic Rules and Applications"
       - "answer": (string) e.g., "Logarithmic rules such as product and power rules simplify calculations by reducing complex multiplication and division, which is particularly helpful in scientific domains dealing with exponential data."
       - "sub_topics": (list of strings) Suggested sub-topics, e.g., ["Using logarithms in astronomical calculations", "Logarithmic data transformation in biology"]
  3. **Update Topic Tree**:
     - Call `update_topic_tree(topic_tree, "multi_drill", gpt_json, current_topics, user_query)` to create a new branch under "combined_topics".
  4. **Output:**
     - Display the combined explanation and suggested sub-topics, visually linking multiple areas of exploration.

### Summary of the Steps
Each of the described steps ensures a continuous update of the topic tree while preserving contextual learning. With every user interaction, the topic tree either deepens (via a single drill) or broadens (via a multi-topic drill), all while maintaining a structured approach to managing educational content and exploration.



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
#### Which prompt is used is based on:
  - If it is the first query (initial prompt)
  - If the user selects a topic to drill down on
  - If the user supplies a query related to the drill down
  - How many topics the user selects to drill down on at one time

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