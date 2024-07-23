import os
from langchain_huggingface import HuggingFaceEmbeddings
from fewshorts import fewshorts
from langchain_qdrant import Qdrant


os.environ['HUGGINGFACEHUB_API_TOKEN'] = 'Bearer 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'


embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


text=[" ".join(example.values()) for example in fewshorts]

print(text)

# Qdrant configuration
url = "https://2c973bea-6822-482e-bf52-28a6d940865e.us-east4-0.gcp.cloud.qdrant.io"
api_key = "1Yz0UmYsyshSCbiaecoeFPkN5LMd3H43B172CjegPVTfBfb6F9AG6w"
collection_name = "text2sql-fewshorts"



doc_store = Qdrant.from_texts(text, embeddings, url=url, api_key=api_key, collection_name=collection_name,metadatas=fewshorts)


