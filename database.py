import sqlite3

def update_basic_details(firstname,lastname,phonenumber,email,linkedin,github):

    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE BasicDetails
        SET FirstName = ?,
            LastName = ?,
            PhoneNumber = ?,
            Email = ?,
            LinkedIn = ?,
            GitHub = ?
        WHERE id = 1
    """,
    (firstname,lastname,phonenumber,email,linkedin,github)
    )

    connection.commit()
    connection.close()

    return "success"

def get_basic_details():

    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT FirstName, LastName, PhoneNumber, Email, LinkedIn, GitHub
        FROM BasicDetails
    """)

    data = cursor.fetchone()

    connection.close()

    return data