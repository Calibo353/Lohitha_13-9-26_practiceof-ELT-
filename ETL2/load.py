from sqlalchemy import create_engine, URL
from config import DB_CONFIG


def load(df, table_name="iris"):

    connection_url = URL.create(
        "mysql+pymysql",
        username=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        host=DB_CONFIG["host"],
        database=DB_CONFIG["database"]
    )

    engine = create_engine(connection_url)

    df.to_sql(
        table_name,
        con=engine,
        if_exists="replace",
        index=False
    )

    print(f"Loaded {len(df)} rows into '{table_name}' table")