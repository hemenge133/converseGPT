# Model Inputs / Variables

from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder, SystemMessagePromptTemplate


def initChat():
    systemprompt="You are a helpful assistant."

    model_kwargs = {"top_p": 1, "frequency_penalty": 0.1, "presence_penalty": 0.1}

    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.5, model_kwargs=model_kwargs)

    prompt = ChatPromptTemplate(
        messages=[
            SystemMessagePromptTemplate.from_template(systemprompt),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template("{message}")
        ]
    )

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation = LLMChain(
    llm=chat,
    prompt=prompt,
    memory=memory
)

    return chat,memory,conversation