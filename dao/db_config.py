import os
import sqlite3
import psycopg2
# path / url de conexão
DB_PATH = "postgresql://neondb_owner:npg_1u2eYmXzkEtn@ep-holy-frog-acqzcy3a-pooler.sa-east-1.aws.neon.tech/neondb?sslmode=requires"

def get_connection():
    return psycopg2.connect(DB_PATH)