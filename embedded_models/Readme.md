

# Hugging Face emebdded Models
1. sentence-transformers/all-mpnet-base-v2"
2. embeddings = HuggingFaceInstructEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2") (dimenssion:768)


2. sentence-transformers/all-MiniLM-L6-v2
   '''
from sentence_transformers import SentenceTransformer
sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embeddings = model.encode(sentences)
print(embeddings)

   '''
