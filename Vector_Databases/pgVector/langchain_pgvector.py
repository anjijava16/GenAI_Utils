import os

import psycopg2
from langchain_community.vectorstores import PGVector
from openai import OpenAI
from langchain.embeddings import OpenAIEmbeddings
from VectorEmbedds.embedded.embedded_utils import get_embedding_langchain

#from VectorEmbedds.reader.read_csv import read_embedded_df

os.environ['OPENAI_API_KEY'] = ""
client = OpenAI()

connection = psycopg2.connect("host=localhost dbname=postgres user=postgres")
cur = connection.cursor()

query_string = "PostgreSQL is my favorite database"
embed = get_embedding_langchain(query_string)
embedding_function = OpenAIEmbeddings()
# Create a PGVector instance to house the documents and embeddings
from langchain.vectorstores.pgvector import DistanceStrategy

db = PGVector(
    connection_string='postgresql+psycopg2://postgres:postgres@localhost:5432/postgres',
    embedding_function=embedding_function,
    collection_name="embeddings",
    distance_strategy=DistanceStrategy.COSINE
)
print(db)
print(type(db))
#
# retriever = db.as_retriever()
# print(retriever)
# retriever = db.as_retriever(search_kwargs={'k': 3})  # default 4
#
# #Fetch the k=3 most similar documents
# docs =  db.similarity_search(query, k=3)

from langchain.schema import Document

# Query for which we want to find semantically similar documents
query = "Tell me about how Edeva uses Timescale?"
#
# #Fetch the k=3 most similar documents
# docs =  db.similarity_search(query, k=3)
# #The query on our database returns a list of LangChain Documents, let's learn how to interact with those documents below:

docs =  db.similarity_search(query, k=3)

print(type(docs))
print(docs)
