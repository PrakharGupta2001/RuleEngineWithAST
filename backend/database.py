# backend/database.py

import sqlite3

def init_db():
    """Initialize the SQLite database and create the required tables."""
    conn = sqlite3.connect('rules.db', check_same_thread=False)  # Allow multithreaded access
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rule_text TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    return conn

def save_rule(conn, rule_text):
    """Save a new rule to the database."""
    cursor = conn.cursor()
    cursor.execute('INSERT INTO rules (rule_text) VALUES (?)', (rule_text,))
    conn.commit()
    return cursor.lastrowid

def get_all_rules(conn):
    """Retrieve all rules from the database."""
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM rules')
    return cursor.fetchall()

def get_rule_by_id(conn, rule_id):
    """Retrieve a specific rule by its ID."""
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM rules WHERE id = ?', (rule_id,))
    return cursor.fetchone()

def update_rule(conn, rule_id, rule_text):
    """Update an existing rule in the database."""
    cursor = conn.cursor()
    cursor.execute('UPDATE rules SET rule_text = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?', (rule_text, rule_id))
    conn.commit()

def delete_rule(conn, rule_id):
    """Delete a rule from the database."""
    cursor = conn.cursor()
    cursor.execute('DELETE FROM rules WHERE id = ?', (rule_id,))
    conn.commit()
