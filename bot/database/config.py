import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432"),
    "database": os.getenv("DB_NAME", "users_db"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", "password")
}

def get_db_url() -> str:
    return f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@" \
           f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"


def get_db_url_sql() -> str:
    return f"sqlite:///{DB_CONFIG['database']}"