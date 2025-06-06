from search_and_prompt import semantic_search
from generate_sql import generate_sql
from run_sql import run_query

question = input("Type your question (e.g. 'give all customers with spend greater than 0'):")
print(question)


if question:   
    print("inside the if")
    context = "\n".join(semantic_search(question))
    sql = generate_sql(question, context)

    try:
        result =  run_query(sql)
        result.to_csv("data/result.csv")
    except Exception as e:
        print(e)
