import psycopg2
from psycopg2.extras import RealDictCursor
import streamlit as st

def get_db_connection():
    """Establishes a secure connection to the PostgreSQL database using local secrets[cite: 8, 20]."""
    try:
        conn = psycopg2.connect(
            host=st.secrets["postgres"]["host"],
            database=st.secrets["postgres"]["database"],
            user=st.secrets["postgres"]["user"],
            password=st.secrets["postgres"]["password"],
            port=st.secrets["postgres"]["port"]
        )
        return conn
    except Exception as e:
        st.error(f"❌ Database Connection Failed: {e}")
        return None