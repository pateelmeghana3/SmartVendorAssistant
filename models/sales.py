from database.db import get_connection


# ==========================================================
# GET ALL SALES
# ==========================================================

def get_all_sales():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            s.id,
            p.name,
            s.quantity_sold,
            s.total_price,
            s.date
        FROM sales s
        JOIN products p
        ON s.product_id = p.id
        ORDER BY s.id DESC
    """)

    sales = cursor.fetchall()

    connection.close()

    return sales


# ==========================================================
# ADD SALE
# ==========================================================

def add_sale(product_id, quantity, total_price):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO sales(
            product_id,
            quantity_sold,
            total_price
        )
        VALUES(?,?,?)
    """, (product_id, quantity, total_price))

    connection.commit()
    connection.close()


# ==========================================================
# TOTAL SALES
# ==========================================================

def total_sales():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*) AS total_sales
        FROM sales
    """)

    total = cursor.fetchone()["total_sales"]

    connection.close()

    return total


# ==========================================================
# TOTAL REVENUE
# ==========================================================

def total_revenue():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT SUM(total_price) AS revenue
        FROM sales
    """)

    revenue = cursor.fetchone()["revenue"]

    connection.close()

    return revenue if revenue else 0


# ==========================================================
# TOTAL UNITS SOLD
# ==========================================================

def total_units_sold():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT SUM(quantity_sold) AS units
        FROM sales
    """)

    units = cursor.fetchone()["units"]

    connection.close()

    return units if units else 0


# ==========================================================
# TOP SELLING PRODUCT
# ==========================================================

def top_product():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            p.name,
            SUM(s.quantity_sold) AS total_qty
        FROM sales s
        JOIN products p
        ON s.product_id = p.id
        GROUP BY s.product_id
        ORDER BY total_qty DESC
        LIMIT 1
    """)

    product = cursor.fetchone()

    connection.close()

    return product


# ==========================================================
# SALES CHART DATA
# ==========================================================

def sales_chart_data():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            DATE(date) AS day,
            SUM(total_price) AS revenue
        FROM sales
        GROUP BY DATE(date)
        ORDER BY DATE(date)
    """)

    rows = cursor.fetchall()

    connection.close()

    return [dict(row) for row in rows]