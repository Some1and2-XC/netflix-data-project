#!/usr/bin/env python3

import sqlite3
import pandas as pd

# Setting Constants
db_name = "netflix.db"  # filename of the sqlite db
data_src = "../netflix_titles.csv"  # Source directory of the data


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
            cur.close()
            conn.close()
            return False

    conn.commit()
    cur.close()
    conn.close()
    
    return True


# Initializes the database Schema
assert initialize_schema()
print("[1] Schema Initialized")

# Load Data
df = pd.read_csv(data_src)

