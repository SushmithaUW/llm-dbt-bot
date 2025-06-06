import duckdb
import pandas as pd

def run_query(sql, data_path="../jaffle-shop/my_database.duckdb"):
    con = duckdb.connect(data_path, read_only=True)
    result = con.execute(sql).fetchdf()
    return result
