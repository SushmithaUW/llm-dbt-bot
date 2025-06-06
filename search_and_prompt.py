from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

def semantic_search(query, k=3):
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.load_local("dbt_faiss_index", embedding_model, allow_dangerous_deserialization=True)

    # Run a search
    results = vectorstore.similarity_search(query, k)
    return  [doc.page_content for doc in results]

