import mysql.connector
from datetime import datetime

# Database connection function
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="chat_history"
    )

# Function to store a chat message
def save_chat_message(role, content):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    sql = "INSERT INTO chat_history (role, content) VALUES (%s, %s)"
    values = (role, content)
    
    cursor.execute(sql, values)
    conn.commit()
    
    cursor.close()
    conn.close()

# Function to retrieve chat history
def get_chat_history():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    sql = "SELECT * FROM chat_history ORDER BY timestamp DESC LIMIT 10"
    cursor.execute(sql)
    history = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return history
