#!/usr/bin/env python3

import sqlite3
import pandas as pd

# Initialize Database
db_name = "netflix.db"
data_src = "../netflix_titles.csv"


def initialize_schema():
    """
    Function for initializing the sqlite3 database schema
    """

    db_schema_filename = "schema.sql"

    with open(db_schema_filename, "r") as f:
        db_schema = f.read()

    db_calls = []

    for section in db_schema.split("\nGO\n"):
        for sql_call in section.split(";"):
            db_calls.append(sql_call + ";")

    conn = sqlite3.Connection(db_name)
    cur = conn.cursor()

    for statement in db_calls:
        try:
            cur.execute(statement)
        except Exception as e:
            print(f"Error: {e}")
            print(statement)

    conn.commit()
    cur.close()
    conn.close()
    
    return


def main():
    initialize_schema()


# Load Data
df = pd.read_csv(data_src)

