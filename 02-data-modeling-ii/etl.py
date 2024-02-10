import glob
import json
import os
from typing import List

from cassandra.cluster import Cluster


table_drop_events = "DROP TABLE IF EXISTS events"
table_drop_actors = "DROP TABLE IF EXISTS actors"
table_drop_repos = "DROP TABLE IF EXISTS repos"

table_create_events = """
    CREATE TABLE IF NOT EXISTS events
    (
        id text,
        type text,
        public boolean,
        actor_id int,
        repo_id int,
        PRIMARY KEY (
            id,
            type
        ),
        CONSTRAINT fk_actor FOREIGN KEY(actor_id) REFERENCES actors(id),
        CONSTRAINT fk_repo FOREIGN KEY(repo_id) REFERENCES repos(id)
    )
"""

table_create_actors = """
    CREATE TABLE IF NOT EXISTS actors (
        id int,
        login text,
        PRIMARY KEY(id)
    )

"""

table_create_repos = """
    CREATE TABLE IF NOT EXISTS repos (
        id int,
        name text,
        PRIMARY KEY(id)
    )
"""

create_table_queries = [
    table_create_actors,
    table_create_repos,
    table_create_events,
]
drop_table_queries = [
    table_drop_events,
    table_drop_actors,
    table_drop_repos,
]

def drop_tables(session):
    for query in drop_table_queries:
        try:
            rows = session.execute(query)
        except Exception as e:
            print(e)


def create_tables(session):
    for query in create_table_queries:
        try:
            session.execute(query)
        except Exception as e:
            print(e)


def get_files(filepath: str) -> List[str]:
    """
    Description: This function is responsible for listing the files in a directory
    """

    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, "*.json"))
        for f in files:
            all_files.append(os.path.abspath(f))

    num_files = len(all_files)
    print(f"{num_files} files found in {filepath}")

    return all_files


def process(session, filepath):
    # Get list of files from filepath
    all_files = get_files(filepath)

    for datafile in all_files:
        with open(datafile, "r") as f:
            data = json.loads(f.read())
            for each in data:
                # Print some sample data
                print(each["id"], each["type"], each["actor"]["login"])

                # Insert data into tables here
                insert_data(session, each)

def insert_data(session, each):
    actor_id = str(each["actor"]["id"])
    insert_statement = f"""
                    INSERT INTO actors (
                        id,
                        login
                    ) VALUES ({each["actor"]["id"]}, 
                    '{each["actor"]["login"]}')
                """
    session.execute(insert_statement)
    
    event_id = str(each["id"])
    insert_statement = f"""
                    INSERT INTO events (
                        id,
                        type,
                        actor_id,
                        repo_id
                    ) VALUES ('{each["id"]}', 
                    '{each["type"]}', 
                    '{each["actor"]["id"]}', 
                    '{each["repo"]["id"]}')
                """
    session.execute(insert_statement)
    
    repo_id = each["repo"]["id"]
    insert_statement = f"""
                    INSERT INTO repos (
                        id,
                        name
                    ) VALUES ({each["repo"]["id"]}, 
                    '{each["repo"]["name"]}')
                """
    session.execute(insert_statement)

def insert_sample_data(session):
    query = f"""
    INSERT INTO events (id, type, public) VALUES ('23487929637', 'IssueCommentEvent', true)
    """
    session.execute(query)


def main():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()

    # Create keyspace
    try:
        session.execute(
            """
            CREATE KEYSPACE IF NOT EXISTS github_events
            WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }
            """
        )
    except Exception as e:
        print(e)

    # Set keyspace
    try:
        session.set_keyspace("github_events")
    except Exception as e:
        print(e)

    drop_tables(session)
    create_tables(session)

    # process(session, filepath="../data")
    insert_sample_data(session)

    # Select data in Cassandra and print them to stdout
    query = """
    SELECT * from events WHERE id = '23487929637' AND type = 'IssueCommentEvent'
    """
    try:
        rows = session.execute(query)
    except Exception as e:
        print(e)

    for row in rows:
        print(row)


if __name__ == "__main__":
    main()