# Setting up the prompt that will be sent to the llama2 model and making sure it doesn't hallucinate

# Note: Model highly sensitive -> If altering my code/prompt use precise indentation or prompt template.

qa_template = """Use the following pieces of information to answer the user's question.
4	If you don't know the answer, just say that you don't know, don't try to make up an answer.
5
6	Context: {context}
7	Question: {question}
8
9	Only return the helpful answer below and nothing else.
10	Helpful answer:
"""

summary_template = """
"""