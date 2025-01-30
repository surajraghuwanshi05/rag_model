from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader




def Load_pdf(pdf_path):
    """
    load the text from the pdf
    """
    loader = PyPDFLoader(pdf_path)
    docs= loader.load()
    return docs

def load_text(text_path):
    loader=TextLoader(text_path)
    text_documents=loader.load()
    return text_documents



def text_split(docs):
    """Split the text into chuncks"""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    documents=text_splitter.split_documents(docs)
    return documents



def get_final_document():
    pdf_path = "artifacts/Review.pd"  
    docs = Load_pdf(pdf_path)
    return text_split(docs)  


if __name__=="__main__":

    pdf_path = "aritfacts/review.pdf"
    text_path = "artifacts/agroforestry.txt" 
    docs = Load_pdf(pdf_path) 
    final_document = text_split(docs=docs)







