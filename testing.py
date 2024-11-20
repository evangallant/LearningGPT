from prompts import create_general_follow_up, create_initial_query, create_multiple_topic_drill_down, create_single_topic_drill_down_noquery, create_single_topic_drill_down_withquery
from helpers import sample_topic_tree, find_current_topic
from topic_tree_management import initialize_topic_tree, update_topic_tree
from openai_calls import call_openai_api, get_general_followup_response, get_initial_response, get_multi_drill_response, get_single_drill_response
import json
import openai

###############  PROMPT CREATION --> GPT CALL --> TREE UPDATE TESTING  #################
# INITIAL
user_query = "help me understand existentialism"

prompt = create_initial_query(user_query)

response = get_initial_response(prompt)
print(response)
response_json = json.loads(response)

topic_tree = initialize_topic_tree(response_json)
print(json.dumps(topic_tree, indent=4))

# GENERAL FOLLOW UP
user_query = "How does god factor in?"

current_topic_node = find_current_topic(topic_tree["root"])
print(current_topic_node)
current_topic = current_topic_node['topic']['branch']

gff_prompt = create_general_follow_up(topic_tree, user_query, current_topic_node['topic']['bud'])
print(gff_prompt)

gff_response = get_general_followup_response(gff_prompt)
gff_response_json = json.loads(gff_response)

topic_tree = update_topic_tree(topic_tree, "general_follow_up", gff_response_json, current_topic, user_query)
print(json.dumps(topic_tree, indent=4))

# SINGLE DRILL DOWN NO QUERY
current_topic_node = find_current_topic(topic_tree["root"])
current_topic = current_topic_node['topic']['branch']

sddnq_prompt = create_single_topic_drill_down_noquery(topic_tree, current_topic)
print(sddnq_prompt)

sddnq_response = get_single_drill_response(sddnq_prompt)
sddnq_response_json = json.loads(sddnq_response)

topic_tree = update_topic_tree(topic_tree, "single_drill_no_query", sddnq_response_json, current_topic)
print(json.dumps(topic_tree, indent=4))

# SINGLE DRILL DOWN WITH QUERY
user_query = "can you give the definition of freedom within the context of existentialism?"
current_topic_node = find_current_topic(topic_tree["root"])
current_topic = current_topic_node['topic']['branch']

sddnwq_prompt = create_single_topic_drill_down_withquery(topic_tree, current_topic, user_query)
print(sddnwq_prompt)

sddwq_response = get_general_followup_response(sddnwq_prompt)
sddwq_response_json = json.loads(sddwq_response)

topic_tree = update_topic_tree(topic_tree, "single_drill_with_query", sddwq_response_json, current_topic, user_query)
print(json.dumps(topic_tree, indent=4))


# MULTI DRILL



##############################  GPT CALL TESTING  ##############################



###############################  TREE MANAGEMENT TESTING  ##############################
# initial_gpt_json = {
#                 "answer": "Dot products are a math thing",
#                 "topic_name": "Dot Products",
#                 "sub_topics": [
#                     "Geometric interpretation of dot products",
#                     "The relationship between dot products and vector projection",
#                     "Applications of dot products in physics and engineering"
#                 ]
#             }

# initial_tree = initialize_topic_tree(initial_gpt_json)
# subsequent_gpt_json = {
#                 "answer": "Dot products look pretty when mapped to a 2 or 3d plane",
#                 "sub_topics": [
#                     "more on dot product geometry",
#                     "how to calculate dot product geometry"
#                 ]
#             }
# current_topic = ["Geometric interpretation of dot products"]
# user_query = "hello?"

# updated_tree = update_topic_tree(initial_tree, "single_drill_with_query", subsequent_gpt_json, current_topic, user_query)

# current_topics = ["Geometric interpretation of dot products", "Applications of dot products in physics and engineering"]
# multi_gpt_json = {
#             "combined_topic_name": "Relationship between Dot Products and Machine Learning",
#             "answer": "Dot products are fundamental in machine learning, particularly in determining similarity between vectors and in optimizing models. In the context of supervised learning, dot products help calculate the weighted sum of input features during model prediction. This is crucial in algorithms like linear regression, where the dot product is used to compute predictions from input features and weights. In neural networks, dot products are used in the forward propagation step to determine the inputs to activation functions. Furthermore, dot products are used in optimization algorithms like gradient descent to adjust model parameters by computing gradients efficiently.",
#             "sub_topics": [
#                 "Dot products in neural network weight calculations",
#                 "Role of dot products in measuring vector similarity for clustering",
#                 "Use of dot products in gradient-based optimization techniques"
#             ]
#         }

# updated_tree = update_topic_tree(updated_tree, "multi_drill", multi_gpt_json, current_topics, user_query)

# current_topic = ["The relationship between dot products and vector projection"]
# user_query = "can you help me understand vector projection on a 2d plane?"
# query = create_single_topic_drill_down_withquery(updated_tree, current_topic, user_query)
# response = {
#     "answer": "Vector projection is a way to determine how much of one vector lies along the direction of another vector. On a 2D plane, given two vectors, A and B, the projection of vector A onto vector B represents the shadow or component of A along the direction of B. To calculate this, you use the dot product to find how much of A points in the direction of B, and then normalize it by the length of B. Mathematically, the formula for the projection of A onto B is: \n\nproj_B(A) = (A · B / |B|^2) * B. \n\nIn this formula, A · B is the dot product of vectors A and B, and |B| is the magnitude (or length) of vector B. The dot product essentially measures how aligned A is with B, and dividing by |B|^2 scales the projection to match the length of B. The resulting vector points in the same direction as B and has a magnitude that represents how much of A is along B’s direction.\n\nOn a 2D plane, this projection is often useful for applications such as decomposing forces or determining the influence of a vector in a particular direction.",
#     "sub_topics": [
#         "Calculating the dot product in 2D",
#         "Understanding orthogonal components and their relationship to projection",
#         "Applications of vector projection in physics and engineering"
#     ]
# }

# updated_tree = update_topic_tree(updated_tree, "single_drill_no_query", response, current_topic, user_query)

# current_topics = ["Relationship between Dot Products and Machine Learning", "Understanding orthogonal components and their relationship to projection"]
# user_query = "what does orthogonality have to do with machine learning?"
# query = create_multiple_topic_drill_down(updated_tree, current_topics, user_query)
# multi_gpt_json = {
#     "combined_topic_name": "Orthogonality and Machine Learning",
#     "answer": "In machine learning, orthogonality is an important concept because it often represents independence between features or components. When vectors are orthogonal, their dot product is zero, indicating that they do not influence each other. This independence is particularly valuable when trying to minimize feature redundancy. For instance, orthogonal features provide unique information without overlapping, leading to a more efficient model. Orthogonality also plays a key role in optimization, where gradients or parameter updates that are orthogonal can simplify training, leading to better convergence properties.",
#     "sub_topics": [
#         "Impact of orthogonal features on model performance",
#         "Role of orthogonality in gradient descent and optimization",
#         "Orthogonality in Principal Component Analysis (PCA) and its implications for feature extraction"
#     ]
# }

# updated_tree = update_topic_tree(updated_tree, "multi_drill", multi_gpt_json, current_topics, user_query)

# current_topic = ["Orthogonality and Machine Learning"]
# user_query = "I think I need a deeper explanation of orthogonality, can you help?"
# bud = "In machine learning, orthogonality is an important concept because it often represents independence between features or components. When vectors are orthogonal, their dot product is zero, indicating that they do not influence each other. This independence is particularly valuable when trying to minimize feature redundancy. For instance, orthogonal features provide unique information without overlapping, leading to a more efficient model. Orthogonality also plays a key role in optimization, where gradients or parameter updates that are orthogonal can simplify training, leading to better convergence properties."

# query = create_general_follow_up(updated_tree, user_query, bud)
# response = {
#   "answer": "Orthogonality, in the context of vectors, means that two vectors are at right angles (90 degrees) to each other. This is significant because when vectors are orthogonal, they have no directional influence on each other. Geometrically, you can think of orthogonal vectors as being completely independent in space—if one vector points along the x-axis and another along the y-axis, any movement in one direction does not change the position along the other. Mathematically, orthogonality is determined using the dot product. If the dot product of two vectors is zero, it implies that the vectors are orthogonal. This is because the dot product formula includes the cosine of the angle between the two vectors; when this angle is 90 degrees, the cosine value is zero, resulting in a dot product of zero. Orthogonality also has important implications for vector projection. When projecting one vector onto another, if the vectors are orthogonal, the projection will be zero since they have no shared component. In engineering and physics, orthogonality helps in breaking down complex systems into simpler, independent components, such as decomposing forces or analyzing signal components in different directions. This independence property is also why orthogonal bases are so useful in mathematics, allowing us to represent vectors in a coordinate system where each axis (or basis vector) is orthogonal to the others, simplifying many calculations and providing a clear interpretation of vector components."
# }

# response["answer"] = response["answer"].replace("\n", "")

# updated_tree = update_topic_tree(updated_tree, "general_follow_up", response, current_topic, user_query)

# json_output = json.dumps(updated_tree, indent=4)
# print(json_output)



##############################  PROMPT TESTING  ##############################

# topic_tree = sample_topic_tree
# current_topic = "Gaussian elimination"
# current_topics = "Dot products, machine learning"

# # Initial query
# initial_user_query = "Can you explain dot products in plain english"
# initial_query = create_initial_query(initial_user_query)
# # print(initial_query)

# # Single topic drill down w/o query
# single_drill_no_query = create_single_topic_drill_down_noquery(sample_topic_tree, current_topic)
# # print(single_drill_no_query)

# # Single topic drill down w/ query
# drill_user_query = "Please explain more about this subject"
# single_drill_with_query = create_single_topic_drill_down_withquery(sample_topic_tree, current_topic, drill_user_query)
# # print(single_drill_with_query)

# # Multi topic
# multi_user_query = "Please explain how these topics are related"
# multi_query = create_multiple_topic_drill_down(topic_tree, current_topics, multi_user_query)
# print(multi_query)