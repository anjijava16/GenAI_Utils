from enum import Enum

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

app = FastAPI(
    title="Chat Memory API",
    description="""ChatApplication.""",
    version="0.0.1",
    debug=True,
)

from monitoring_langsmith_phoenix_llms.langsmith_utils import enable_langsmith_enabled
from utils.start_up import init, anthropic_sonnet_20240229

class ModelName(str,Enum):
    OPENAI="OPENAI"
    AWS_ANTHROPIC_SONNET="AWS_ANTHROPIC_SONNET"
class ChatHistoryMessage(BaseModel):
    input_model:ModelName='OpenAI'
    session_id:str=None
    query: str = None
    user_id: str = None

# conn_info = "postgresql://postgres:postgres@localhost/postgres"
# sync_connection = psycopg.connect(conn_info)

@app.post("/chat")
def chat_application(chat_history:ChatHistoryMessage):
    init()
    enable_langsmith_enabled()
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant."),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}"),
        ]
    )

    if chat_history.input_model=="AWS_Sonnet":
        llm = anthropic_sonnet_20240229()
    else:
        llm = ChatOpenAI()

    chain = prompt | llm

    from langchain_core.runnables.history import RunnableWithMessageHistory
    from langchain_community.chat_message_histories import PostgresChatMessageHistory

    # Use a single PostgresChatMessageHistory instance
    message_history = PostgresChatMessageHistory(
        connection_string="postgresql://postgres:postgres@localhost/postgres",
        session_id=chat_history.session_id,
    )

    # Get the existing messages from the history
    existing_messages = message_history.messages
    print(f" existing_messages type ={type(existing_messages)}")


    # Create a list to hold all messages
    full_message_log = existing_messages + [
        {"type": "human", "content": chat_history.query}
    ]



    chain_with_history = RunnableWithMessageHistory(
        chain,
        lambda session_id: message_history,
        input_messages_key="input",
        history_messages_key="history",
    )


    # This is where we configure the user and session id
    config = {"configurable": {"user_id": chat_history.user_id, "session_id": chat_history.session_id}}
    response=chain_with_history.invoke({"input": chat_history.query}, config=config)
    print(f" type of response ={response}")
    return {
        "response": response,
        "full_message_history": full_message_log
    }


# Q:print(chain_with_history.invoke({"input": "Hi This is Anji, I am in Philly USA, I am going Hyderabad next year 2026"}, config=config))
# A: content="Hello Anji! That's exciting that you're planning a trip to Hyderabad next year. How can I assist you with your travel plans or preparations for your trip?" additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 33, 'prompt_tokens': 38, 'total_tokens': 71, 'completion_tokens_details': {'audio_tokens': 0, 'reasoning_tokens': 0, 'accepted_prediction_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None} id='run-3a4b97f0-d13c-40ea-81cb-d2887aea92cc-0' usage_metadata={'input_tokens': 38, 'output_tokens': 33, 'total_tokens': 71, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}

# "input": "Please tell me where I am going now ?"
# content='Based on your message, you are currently in Philadelphia, USA, and you are planning to travel to Hyderabad, India in 2026.' additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 28, 'prompt_tokens': 88, 'total_tokens': 116, 'completion_tokens_details': {'audio_tokens': 0, 'reasoning_tokens': 0, 'accepted_prediction_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None} id='run-ea08e02c-d6c1-4b63-b5d0-42442daef269-0' usage_metadata={'input_tokens': 88, 'output_tokens': 28, 'total_tokens': 116, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8207)


    A
