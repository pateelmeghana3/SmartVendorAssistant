from database.db import get_connection
from datetime import datetime


# ==========================================================
# GET ALL FESTIVALS
# ==========================================================

def get_all_festivals():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM festivals
        ORDER BY festival_date
    """)

    festivals = cursor.fetchall()

    connection.close()

    return festivals


# ==========================================================
# ADD FESTIVAL
# ==========================================================

def add_festival(name, date):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO festivals(
            festival_name,
            festival_date
        )
        VALUES(?, ?)
    """, (name, date))

    connection.commit()
    connection.close()


# ==========================================================
# DELETE FESTIVAL
# ==========================================================

def delete_festival(festival_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM festivals
        WHERE id=?
    """, (festival_id,))

    connection.commit()
    connection.close()


# ==========================================================
# GET NEXT UPCOMING FESTIVAL
# ==========================================================

def next_festival():

    connection = get_connection()
    cursor = connection.cursor()

    today = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("""
        SELECT *
        FROM festivals
        WHERE festival_date >= ?
        ORDER BY festival_date ASC
        LIMIT 1
    """, (today,))

    festival = cursor.fetchone()

    connection.close()

    return festival


# ==========================================================
# GET FESTIVALS WITHIN NEXT N DAYS
# ==========================================================

def upcoming_festivals(days=30):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM festivals
        WHERE julianday(festival_date) - julianday('now') <= ?
          AND julianday(festival_date) >= julianday('now')
        ORDER BY festival_date
    """, (days,))

    festivals = cursor.fetchall()

    connection.close()

    return festivals


# ==========================================================
# COUNT FESTIVALS
# ==========================================================

def festival_count():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*) AS total
        FROM festivals
    """)

    total = cursor.fetchone()["total"]

    connection.close()

    return total