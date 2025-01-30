# RAG-based Chatbot with Streamlit API 
This project implements a Retrieval-Augmented Generation (RAG) model-based chatbot with a Flask API. The chatbot generates responses by retrieving relevant documents from a vector store and passing them through a language model for context-aware responses. The application also stores the conversation history in a MySQL database and provides endpoints for interacting with the chatbot and retrieving the chat history.

---

## Project Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/surajraghuwanshi05/rag_model.git
   cd https://github.com/surajraghuwanshi05/rag_model.git
   ```
   

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```


3. Start the streamlit  Server
To start the streamlit server, run the following command:
```streamlit run  app.py```

## How to Use the App

1. Open the app in your browser.
2. Type your question into the input box.
3. Click **"Get Answer"** to see the response generated by the RAG model.
4. The model will provide an answer based on the input question, using the knowledge stored in the system.

## Customizing the App

To customize the model or modify the way answers are generated, you can edit the `generate_answer` function inside the `rag_model.py` module.

- You can adjust the context, change the model repository, or fine-tune the response behavior.





   ### `data_preprocessing.py`

This module handles the preprocessing of raw data from text files into smaller chunks that can be processed and analyzed by the chatbot. The steps involved in this module are:

1. **Loading Data**:
   - The `load_data_from_file` function loads the raw text data from a specified text file.
   - The text is read line-by-line or in its entirety, depending on the structure of the input file.

2. **Chunking the Data**:
   - The `split_into_chunks` function processes the loaded text data and divides it into manageable chunks.
   - The chunks are typically based on a set character limit or logical sections (e.g., paragraphs), making it easier for the RAG model to handle and retrieve relevant portions of the data.

3. **Data Preparation**:
   - Once the data is chunked, the processed chunks are either saved locally or passed directly to the vector store.
   - This prepares the data for later use in the vectorization process where it will be converted into vectors for efficient retrieval during chatbot interactions.




   ### `embed_store.py`

In this module, we take the preprocessed data and convert it into a vector database that the chatbot can query to retrieve relevant chunks of text for answering user queries. The steps in this module are:

1. **Vectorizing Data**:
   - The `vectorize_data` function processes the data chunks by converting them into numerical vectors. These vectors represent the semantic meaning of the text, making it easier for the model to understand and retrieve contextually relevant information.

2. **Storing Vectors**:
   - The `create_vector_store` function stores the vectors into a database, enabling fast similarity-based searches. This makes it possible for the Retrieval-Augmented Generation (RAG) model to retrieve similar text chunks based on a user's query.

3. **Retrieval**:
   - Once the vectors are stored, the vector store allows fast retrieval of relevant chunks. The retrieval process matches the input query to the most semantically similar text chunks from the database, facilitating context-aware response generation.

This module is critical for transforming raw text data into a form that can be efficiently searched and utilized by the chatbot.

---

### `rag_model.py`

This module contains the logic for the Retrieval-Augmented Generation (RAG) pipeline, which combines document retrieval with a language model to generate meaningful and context-aware responses to user queries. The steps in this module include:

1. **Vector Store Integration**:
   - The `initialize_vector_store` function loads the vector store created in the `vector.py` module. This allows the RAG model to retrieve the relevant document chunks during a query.

2. **Language Model Integration**:
   - The `initialize_llm` function sets up a language model from Hugging Face (Falcon-7B-Instruct). This model processes the retrieved chunks and generates a response based on the provided context.

3. **Answer Generation**:
   - The `generate_answer` function accepts a query from the user, retrieves the most relevant document chunks from the vector store, processes them using the language model, and returns a response. This is the core functionality of the RAG system.

4. **Document Chain**:
   - The `create_document_chain` function combines the document retrieval and answer generation steps into a unified pipeline. It ensures that the RAG model can answer questions by using both the retrieved context and the generative capabilities of the language model.

This module is the heart of the chatbot, combining data retrieval and generative capabilities to produce informative responses based on the context.

---


## app.py

### Overview
`app.py` is the main file that runs the Streamlit app, which allows users to interact with the RAG-based chatbot. The app takes user queries, sends them to the RAG model for answer generation, and displays the result.

### How it Works
1. The app displays a title and an input box for the user to type their question.
2. Once the user submits a question, the `generate_answer` function from the `rag_model.py` module is called to generate a response.
3. The app displays the generated answer in a user-friendly format.


## rag.ipynb

The `rag.ipynb` file was used for testing and experimentation during the development of the RAG-based chatbot. It served as an environment to:

- Try different configurations of the RAG pipeline.
- Test various queries and evaluate the model's responses.
- Experiment with different vector stores, retrievers, and LLMs (Large Language Models).
- Fine-tune and debug the `generate_answer` function before integrating it into the main application (`app.py`).

This Jupyter notebook helped to quickly iterate and verify components of the system, ensuring that the model was providing relevant and accurate responses before being deployed in the Streamlit app.





## Area of Improvement

While the current implementation of the RAG-based chatbot is functional, there are several areas where the project could be enhanced for better performance and user experience:

### 1. **Error Handling and Validation**
   - Currently, the app doesn't handle edge cases or errors gracefully. Implementing better error handling (e.g., invalid queries, empty inputs, or failed model requests) would improve the robustness of the system.
   
### 2. **Model Fine-tuning**
   - The current model might not always provide highly relevant or accurate answers. Fine-tuning the model with a more specific dataset or adding domain-specific knowledge could improve the quality of responses.
   
### 3. **User Authentication**
   - Adding user authentication could allow for a personalized experience, where the user's chat history is saved and can be referenced in future interactions.
   
### 4. **Real-time Chat History**
   - The current implementation does not show dynamic chat history. It could be improved by storing and displaying a real-time chat history from a database or session-based storage.
   

   
### 5. **Improved UI/UX**
   - The user interface can be enhanced with more interactive elements, such as dropdowns or suggestions based on previous queries, to make the experience more engaging.
   

### 6. **Logging and Analytics**
   - Implementing logging and analytics would help track app usage, identify patterns, and provide insights for future improvements.
   



