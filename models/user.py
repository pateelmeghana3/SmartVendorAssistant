from database.db import get_connection


# ==========================================================
# CHECK IF USER EXISTS
# ==========================================================

def user_exists(username):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=?",
        (username,)
    )

    user = cursor.fetchone()
    connection.close()

    return user


# ==========================================================
# CREATE NEW USER (UPDATED)
# ==========================================================

def create_user(username, password, security_question, security_answer):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO users(username, password, security_question, security_answer)
        VALUES(?,?,?,?)
    """, (username, password, security_question, security_answer))

    connection.commit()
    connection.close()


# ==========================================================
# LOGIN USER
# ==========================================================

def login_user(username, password):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM users
        WHERE username=? AND password=?
    """, (username, password))

    user = cursor.fetchone()
    connection.close()

    return user


# ==========================================================
# GET SECURITY QUESTION
# ==========================================================

def get_security_question(username):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT security_question
        FROM users
        WHERE username=?
    """, (username,))

    result = cursor.fetchone()
    connection.close()

    return result


# ==========================================================
# VERIFY SECURITY ANSWER
# ==========================================================

def verify_security_answer(username, answer):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM users
        WHERE username=? AND security_answer=?
    """, (username, answer))

    user = cursor.fetchone()
    connection.close()

    return user


# ==========================================================
# UPDATE PASSWORD
# ==========================================================

def update_password(username, new_password):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE users
        SET password=?
        WHERE username=?
    """, (new_password, username))

    connection.commit()
    connection.close()