from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.vectorstores import FAISS
from data_preprocessing  import get_final_document




# Embedding Using Huggingface

huggingface_embeddings = HuggingFaceBgeEmbeddings(
    model_name="BAAI/bge-small-en-v1.5",
    model_kwargs={'device':"cpu"},
    encode_kwargs={'normalize_embeddings':True}
)

def vectorize_document():
    document = get_final_document()
    vectorstore =FAISS.from_documents(document, huggingface_embeddings)
    return vectorstore



if __name__=="__main__":
    vector_store = vectorize_document()

