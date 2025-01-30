import os
from dotenv import load_dotenv
from embed_store import vectorize_document
from langchain.llms import HuggingFaceHub
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from config import HUGGINGFACEHUB_API_TOKEN



def initialize_vector_store():
    """Initialize the vector store and retriever."""
    vectorstore = vectorize_document()
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3})
    return retriever  

def initialize_llm():
    """Initialize the Hugging Face model with API token."""
    # set you huggingface api here
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN  
    return HuggingFaceHub(
        repo_id="tiiuae/falcon-7b-instruct",
        model_kwargs={"temperature": 0.1, "max_length": 500}
    )

def create_prompt():
    """Define the chat prompt template."""
    return ChatPromptTemplate.from_template("""
    Answer the following question based only on the provided context. 
    Think step by step before providing a detailed answer
    <context>
    {context}
    </context>
    Question: {input}
    """)

def create_document_chain(llm, prompt):
    """Create the document processing chain."""
    return create_stuff_documents_chain(llm, prompt)

def create_retrieval_chain_pipeline(retriever, document_chain):
    """Create the final retrieval-based chain pipeline."""
    return create_retrieval_chain(retriever, document_chain)

def generate_answer(query):
    retriever = initialize_vector_store()
    llm = initialize_llm()
    prompt = create_prompt()
    document_chain = create_document_chain(llm, prompt)

    # Create retrieval-based QA chain
    retrieval_chain = create_retrieval_chain_pipeline(retriever, document_chain)

    # Process query
    response = retrieval_chain.invoke({"input": query})
    
    answer = response.get("answer", "No answer found.")
    
    top_chunks = response.get("context", [])  # Assuming context holds retrieved chunks

    return answer, top_chunks  # Ensure the function returns two values

if __name__ == "__main__":
    query = "agroforestry"
    generate_answer(query)