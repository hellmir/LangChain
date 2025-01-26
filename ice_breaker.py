from langchain_community.chat_models import ChatClovaX
from langchain_core.prompts import PromptTemplate

information = "토마토, 밀가루"

if __name__ == "__main__":
    print("Hello LangChain!")

summary_template = """
    Given the information {information} about ingredients from I want you to create:
    1. Several recommendations of recipe from the ingredients
    2. Answer in KOREAN
    """

summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)
llm = ChatClovaX(model="HCX-003")

chain = summary_prompt_template | llm

res = chain.invoke(input={"information": information})

print(res)
