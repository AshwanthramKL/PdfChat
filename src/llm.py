from langchain.llms import CTransformers

llm = CTransformers(model='models\llama-2-7b-chat.ggmlv3.q8_0.bin',
                    model_type="llama",
                    config={
                        "max_new_tokens": 256,
                        # temperature set to 0.01 to avoid exploration and generate direct answers
                        "temperature": 0.01
                    })
