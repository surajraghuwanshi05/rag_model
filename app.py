import streamlit as st
from rag_model import generate_answer

# Streamlit app for handling user queries
def main():
    # Display title and instructions
    st.title("RAG-based Chatbot")
    st.write("Ask a question, and the model will provide an answer.")

    # Input box for user query
    user_query = st.text_input("Your Question:")

    
    if user_query:
        # Generate answer using RAG model
        answer, top_chunks = generate_answer(user_query)
        answer = answer.split("Think step by step before providing a detailed answer.")[-1]

        # Display the answer
        st.subheader("Answer")
        st.write(answer)
        


if __name__ == '__main__':
    main()







