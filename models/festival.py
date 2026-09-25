import requests
from datetime import datetime

from database.db import get_connection


# ==========================================================
# GET ALL CUSTOM FESTIVALS
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
# ADD CUSTOM FESTIVAL
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
# DELETE CUSTOM FESTIVAL
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
# FETCH UPCOMING INDIAN FESTIVALS FROM API
# ==========================================================

def fetch_festivals_from_api():

    url = "https://indian-festival-api.vercel.app/api/festivals?upcoming=true"

    try:

        response = requests.get(url, timeout=10)

        response.raise_for_status()

        result = response.json()

        if not result.get("success"):
            return []

        return result.get("data", [])

    except requests.exceptions.RequestException:

        return []

    except ValueError:

        return []


# ==========================================================
# GET NEXT UPCOMING FESTIVAL
# ==========================================================

def next_festival():

    today = datetime.now().date()

    # ------------------------------------------------------
    # GET FESTIVALS FROM API
    # ------------------------------------------------------

    festivals = fetch_festivals_from_api()

    upcoming = []

    current_year = today.year

    date_key = "date_" + str(current_year)

    for festival in festivals:

        festival_name = festival.get("name")
        festival_date = festival.get(date_key)

        if not festival_name or not festival_date:
            continue

        try:

            date_object = datetime.strptime(
                festival_date,
                "%Y-%m-%d"
            ).date()

            if date_object >= today:

                upcoming.append({
                    "festival_name": festival_name,
                    "festival_date": festival_date
                })

        except ValueError:

            continue

    # ------------------------------------------------------
    # RETURN NEXT API FESTIVAL
    # ------------------------------------------------------

    if upcoming:

        upcoming.sort(
            key=lambda x: x["festival_date"]
        )

        return upcoming[0]

    # ------------------------------------------------------
    # FALLBACK TO CUSTOM DATABASE FESTIVALS
    # ------------------------------------------------------

    connection = get_connection()
    cursor = connection.cursor()

    today_string = today.strftime("%Y-%m-%d")

    cursor.execute("""
        SELECT *
        FROM festivals
        WHERE festival_date >= ?
        ORDER BY festival_date ASC
        LIMIT 1
    """, (today_string,))

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
# COUNT CUSTOM FESTIVALS
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