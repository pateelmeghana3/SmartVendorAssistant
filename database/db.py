import sqlite3
from utils.config import DATABASE_NAME


# ==========================================================
# DATABASE CONNECTION
# ==========================================================

def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


# ==========================================================
# CREATE DATABASE (FRESH SCHEMA)
# ==========================================================

def create_database():

    connection = get_connection()
    cursor = connection.cursor()

    # USERS TABLE (UPDATED)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            security_question TEXT NOT NULL,
            security_answer TEXT NOT NULL
        )
    """)

    # PRODUCTS TABLE
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    """)

    # SALES TABLE
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            quantity_sold INTEGER,
            total_price REAL,
            date TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # FESTIVALS TABLE
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS festivals(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            festival_name TEXT NOT NULL,
            festival_date TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()