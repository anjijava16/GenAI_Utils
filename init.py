import os

from langchain_aws import ChatBedrock

from monitoring_langsmith_phoenix_llms.langsmith_utils import enable_langsmith_enabled

import os

def enable_langsmith_enabled():
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_API_KEY"] = "langmsith"

def enable_phoenix_arize():
    # import phoenix as px
    # session = px.launch_app()
    from phoenix.trace.langchain import LangChainInstrumentor
    LangChainInstrumentor().instrument()

def init():
    os.environ['OPENAI_API_KEY'] = "sk-openai"
    #enable_langsmith_enabled()

def anthropic_sonnet_20240229(model_name:str='anthropic.claude-3-sonnet-20240229-v1:0'):
    chat = ChatBedrock(
        model_id=model_name,
        model_kwargs={"temperature": 0.1},
    )
    return chat



from langchain_openai import AzureChatOpenAI, AzureOpenAI, AzureOpenAIEmbeddings
import os
def init_azure_openai():
    os.environ["AZURE_OPENAI_API_KEY"] = '14900f85476d64cd697497b370db6b1a2'
    os.environ["AZURE_OPENAI_ENDPOINT"] = "https://multiagentsystem.openai.azure.com/"
    os.environ["SERPAPI_API_KEY"] = "545454"
    llm = AzureChatOpenAI(
        azure_deployment="gpt40",  # or your deployment
        api_version="2024-02-15-preview",  # or your api version
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        # other params...
    )
    return llm

def init_azure_openai_embedded():
    os.environ["AZURE_OPENAI_API_KEY"] = '34454'
    os.environ["AZURE_OPENAI_ENDPOINT"] = "https://multiagentsystem.openai.azure.com/"
    os.environ["SERPAPI_API_KEY"] = "45454"
    os.environ["AZURE_OPENAI_API_VERSION"]="2024-02-01"
    # client = AzureOpenAI(
    #     api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    #     api_version="2024-02-01",
    #     azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
    # )
    model="text-embedde"
    embeddings = AzureOpenAIEmbeddings(
        model=model
        # dimensions: Optional[int] = None, # Can specify dimensions with new text-embedding-3 models
        # azure_endpoint="https://<your-endpoint>.openai.azure.com/", If not provided, will read env variable AZURE_OPENAI_ENDPOINT
        # api_key=... # Can provide an API key directly. If missing read env variable AZURE_OPENAI_API_KEY
        # openai_api_version=..., # If not provided, will read env variable AZURE_OPENAI_API_VERSION
    )
    return embeddings
# llm=init()
