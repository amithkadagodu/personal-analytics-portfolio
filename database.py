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

def get_edu():

    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM education_details ORDER BY year DESC;")

    data = cursor.fetchall()

    connection.close()

    return data    

def update_edu(university,degree,year):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("""

    INSERT INTO education_details (university, degree, year)
    VALUES (?, ?, ?)
""",(university,degree,year)
)
    connection.commit()
    connection.close()
    return "success"



def get_exp():

    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM experience")
    data = cursor.fetchall()

    connection.close()
    return data

def update_exp(company,role,start,end):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO experience(company,role,start,upto)
    VALUES(?,?,?,?);
    """,(company,role,start,end))
    connection.commit()
    connection.close()
    return "success"

def get_certi():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM certification ORDER BY year DESC")
    data = cursor.fetchall()
    connection.close()
    return data

def update_certi(certification,by,year,url):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO certification (name,certi_with,year,url)
    VALUES(?,?,?,?);
    """,(certification,by,year,url))
    connection.commit()
    connection.close()
    return "success" 

def get_projects():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM projects ORDER BY id DESC")
    data = cursor.fetchall()
    connection.close()
    return data  

def update_projects(name,url):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO projects (name,url)
    VALUES(?,?);
    """,(name,url))
    connection.commit()
    connection.close()
    return "success"   