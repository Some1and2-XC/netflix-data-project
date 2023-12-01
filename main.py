#!/usr/bin/env python3

import warnings
import sqlite3
import pandas as pd

# Suppresses warnings from pandas
warnings.simplefilter(action="ignore", category=UserWarning)

# Setting Constants
db_name = "netflix.db"  # filename of the sqlite db
data_src = "../netflix_titles.csv"  # Source directory of the data


def initialize_schema():
    """
    Function for initializing the sqlite3 database schema (unused)
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


def get_comma_values(df, key: str) -> pd.DataFrame:
    """
    function for getting the comma values from a dataframe
    df: pd.DataFrame
        The dataframe that is being searched through
    key: str
        The key string to index df from
    """

    return df[df[key].notna()][key] \
        .map(lambda cv: cv.split(", ")) \
        .explode() \
        .to_frame() \
        .rename(columns = {0:key})


def count_values(srs):
    """
    Function for getting the counts of values in a pandas series
    srs: pd.Series
        the series that is being passed
    """

    return str(srs.value_counts().head(5)) + "\n"


def answer_questions():
    """
    Function for answering questions about the dataset
    """

    print("Q#1: Which actor appears the most?")
    print(count_values(actors))

    print("Q#2: Which genre has the most content?")
    print(count_values(genres))

    print("Q#3: Which director has made the most TV Shows?")
    print(
        count_values(
            df \
            [df.type == "TV Show"] \
            .director))

    print("Q#4: Which director has made the most PG Movies?")
    print(
        count_values(
            df \
            [df.rating == "PG"] \
            [df.type == "Movie"] \
            .director
    ))

    print("Q#5: Which director has made the most R Rated Movies?")
    print(
        count_values(
            df \
            [df.rating == "R"] \
            [df.type == "Movie"] \
            .director))

# Load Data
df = pd.read_csv(data_src, encoding="ascii", encoding_errors="ignore")

# Get column values
ratings = df.rating.unique()
countries = df.country.unique()
tv_types = df.type.unique()
directors = df.director.unique()
actors = get_comma_values(df, "cast")
genres = get_comma_values(df, "listed_in")

# Questions
answer_questions()
