from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

DB_USER = "admin"
DB_PASSWORD = "admin1234"
DB_HOST = "database-2.crp74docgkpu.us-east-1.rds.amazonaws.com"
DB_NAME = "database-2"

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

def test_connection():
    try:
        engine = create_engine(SQLALCHEMY_DATABASE_URL)
        with engine.connect() as connection:
            result = connection.execute("SELECT DATABASE();")
            database_name = result.fetchone()
            print(f"Successfully connected to the database: {database_name}")
    except OperationalError as e:
        print(f"OperationalError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    test_connection()
