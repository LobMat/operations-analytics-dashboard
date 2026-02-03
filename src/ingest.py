import pandas as pd
import psycopg2
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

def load_data_to_psql():
    try:
        BASE_DIR = Path(__file__).resolve().parent.parent
        CSV_PATH = BASE_DIR / "data" / "raw" / "production_data.csv"

        # Load CSV
        df = pd.read_csv(CSV_PATH)

        # Connect to PostgreSQL using a context manager
        with psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        ) as connection:

            with connection.cursor() as cursor:
                for _, row in df.iterrows():
                    cursor.execute(
                        """
                        INSERT INTO production_metrics (date, production_line, shift, units_produced, downtime_minutes, defective_units)
                        VALUES (%s, %s, %s, %s, %s, %s)
                        """,
                        (
                            row["date"],
                            row["production_line"],
                            row["shift"],
                            row["units_produced"],
                            row["downtime_minutes"],
                            row["defective_units"]
                        )
                    )
            connection.commit()
            connection.close()

        print("Data loaded into PostgreSQL successfully.")

    except Exception as e:
        print(f"Error loading data into PostgreSQL: {e}")
