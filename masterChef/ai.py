from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from decouple import config
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

KEY = config("Hugging_Face")
repo_id = "mistralai/Mistral-7B-Instruct-v0.3"
llm = HuggingFaceEndpoint(repo_id=repo_id, huggingfacehub_api_token=KEY)

chat = ChatHuggingFace(llm=llm)

def master_chef(human_text):

    # Define the system message template
    systemMessagePrompt = SystemMessagePromptTemplate.from_template(
        "Your name is Tonmoy. You are a master chef so First Introduce yourself as Tonmoy The Master Chef. You can write any type of food recipe which can be cooked in 10 minutes. You are only allowed to answer food-related queries. If you don't know the answer, then tell 'I don't know the answer.'"
    )

    # Define the human message template
    humanMessagePrompt = HumanMessagePromptTemplate.from_template("{human_text}")

    # Create the chat prompt
    chatPrompt = ChatPromptTemplate.from_messages([
        systemMessagePrompt,
        humanMessagePrompt
    ])

    formattedChatPrompt = chatPrompt.format_messages(human_text=human_text)
    response = chat.invoke(formattedChatPrompt)
    return response.content
