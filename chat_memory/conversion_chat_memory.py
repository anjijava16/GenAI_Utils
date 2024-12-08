from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

from monitoring_langsmith_phoenix_llms.langsmith_utils import enable_langsmith_enabled
from utils.start_up import init

# conn_info = "postgresql://postgres:postgres@localhost/postgres"
# sync_connection = psycopg.connect(conn_info)

enable_langsmith_enabled()
init()
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ]
)

chain = prompt | ChatOpenAI()

from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import PostgresChatMessageHistory
import uuid

# history = PostgresChatMessageHistory(
#     connection_string="postgresql://postgres:postgres@localhost/postgres",
#     session_id="foo",
# )
# table_name = 'message_store'


# def get_session_history(session_id: str) -> BaseChatMessageHistory:
#     return PostgresChatMessageHistory(
#         table_name,
#         session_id,
#         sync_connection=sync_connection
#     )


#session_id = str(uuid.uuid4())
session_id = '71717'
# Initialize the chat history manager
# chat_history = PostgresChatMessageHistory(
#     table_name,
#     session_id,
#     sync_connection=sync_connection
# )
# content='Hello Anji! How can I assist you today?' additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 11, 'prompt_tokens': 23, 'total_tokens': 34, 'completion_tokens_details': {'audio_tokens': 0, 'reasoning_tokens': 0, 'accepted_prediction_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None} id='run-2344ec17-52ff-45a8-9b36-58d023c3d26c-0' usage_metadata={'input_tokens': 23, 'output_tokens': 11, 'total_tokens': 34, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}
#content='Hello Anji! How can I assist you today?' additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 11, 'prompt_tokens': 48, 'total_tokens': 59, 'completion_tokens_details': {'audio_tokens': 0, 'reasoning_tokens': 0, 'accepted_prediction_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None} id='run-a368b2b7-22c1-4cc4-be0e-eb6c9c446b8c-0' usage_metadata={'input_tokens': 48, 'output_tokens': 11, 'total_tokens': 59, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}
#content="Hello, Anji! It's nice to meet you. How can I help you today?" additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 19, 'prompt_tokens': 73, 'total_tokens': 92, 'completion_tokens_details': {'audio_tokens': 0, 'reasoning_tokens': 0, 'accepted_prediction_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None} id='run-31647ce0-23c6-47d7-8ab8-12b44286a144-0' usage_metadata={'input_tokens': 73, 'output_tokens': 19, 'total_tokens': 92, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}
#content='Hello Anji! It seems like you are introducing yourself multiple times. How can I assist you today?' additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 21, 'prompt_tokens': 106, 'total_tokens': 127, 'completion_tokens_details': {'audio_tokens': 0, 'reasoning_tokens': 0, 'accepted_prediction_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None} id='run-95cf0827-7e66-4881-b5da-bbc6d8228ae0-0' usage_metadata={'input_tokens': 106, 'output_tokens': 21, 'total_tokens': 127, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}

chain_with_history = RunnableWithMessageHistory(
    chain,
    lambda session_id: PostgresChatMessageHistory(
        connection_string="postgresql://postgres:postgres@localhost/postgres",
        session_id=session_id,
    ),
    input_messages_key="input",
    history_messages_key="history",
)


# This is where we configure the user and session id
config = {"configurable": {"user_id": "user_1", "session_id": session_id}}
print(chain_with_history.invoke({"input": "Please tell me where I am going now ?"}, config=config))


# Q:print(chain_with_history.invoke({"input": "Hi This is Anji, I am in Philly USA, I am going Hyderabad next year 2026"}, config=config))
# A: content="Hello Anji! That's exciting that you're planning a trip to Hyderabad next year. How can I assist you with your travel plans or preparations for your trip?" additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 33, 'prompt_tokens': 38, 'total_tokens': 71, 'completion_tokens_details': {'audio_tokens': 0, 'reasoning_tokens': 0, 'accepted_prediction_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None} id='run-3a4b97f0-d13c-40ea-81cb-d2887aea92cc-0' usage_metadata={'input_tokens': 38, 'output_tokens': 33, 'total_tokens': 71, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}

# "input": "Please tell me where I am going now ?"
# content='Based on your message, you are currently in Philadelphia, USA, and you are planning to travel to Hyderabad, India in 2026.' additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 28, 'prompt_tokens': 88, 'total_tokens': 116, 'completion_tokens_details': {'audio_tokens': 0, 'reasoning_tokens': 0, 'accepted_prediction_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None} id='run-ea08e02c-d6c1-4b63-b5d0-42442daef269-0' usage_metadata={'input_tokens': 88, 'output_tokens': 28, 'total_tokens': 116, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}
