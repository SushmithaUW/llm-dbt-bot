from llama_cpp import Llama
import re
def generate_sql(question, context):
    print("indise generate_sql")

    llm = Llama.from_pretrained(
        repo_id="TheBloke/Mistral-7B-Instruct-v0.2-GGUF",
        filename="mistral-7b-instruct-v0.2.Q2_K.gguf",
        n_ctx=2048
    )

    prompt = (
        "<|user|>\n"
        f"Given the metadata context:\n{context}\n\n"
        f"And the user question:\n\"{question}\"\n\n"
        "Generate a DuckDB SQL query to answer. Only generate the query alone and no additional texts.\n"
        "<|assistant|>\n"
    )

    response = llm(prompt, max_tokens=800, stop=["<|user|>"])
    output = response['choices'][0]['text']
    
    sql_only = re.sub(r"```sql\s*([\s\S]+?)```", r"\1", output).strip()

    
    return sql_only