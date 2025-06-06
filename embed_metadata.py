import json

from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document


with open("../jaffle-shop/target/catalog.json", "r") as f:
    metadata = json.load(f)

chunks = []

for node_key, node in metadata["nodes"].items():
    table_name = node["metadata"]["name"]
    schema = node["metadata"]["schema"]
    database = node["metadata"]["database"]
    columns = node["columns"]

    table_text = f"Table: {table_name}\nSchema: {schema}\nDatabase: {database}\nColumns:\n"
    for col_name, col_meta in columns.items():
        table_text += f"  - {col_name} ({col_meta['type']})\n"

    chunks.append({
        "id": node_key,
        "type": "table",
        "table_name": table_name,
        "content": table_text
    })

documents = []
for chunk in chunks:
    doc = Document(
        page_content=chunk["content"],
        metadata={
            "id": chunk["id"],
            "type": chunk["type"],
            "table_name": chunk.get("table_name"),
            "column_name": chunk.get("column_name"),
        }
    )
    documents.append(doc)

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vectorstore = FAISS.from_documents(documents, embedding_model)
vectorstore.save_local("dbt_faiss_index")
