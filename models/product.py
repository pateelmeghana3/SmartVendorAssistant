from database.db import get_connection


# ==========================================================
# GET ALL PRODUCTS
# ==========================================================

def get_all_products():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM products")

    products = cursor.fetchall()

    connection.close()

    return products


# ==========================================================
# SEARCH PRODUCTS
# ==========================================================

def search_products(search):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM products
        WHERE name LIKE ?
        """,
        ('%' + search + '%',)
    )

    products = cursor.fetchall()

    connection.close()

    return products


# ==========================================================
# GET SINGLE PRODUCT
# ==========================================================

def get_product(product_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM products
        WHERE id=?
        """,
        (product_id,)
    )

    product = cursor.fetchone()

    connection.close()

    return product


# ==========================================================
# ADD PRODUCT
# ==========================================================

def add_product(name, price, stock):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO products(name, price, stock)
        VALUES(?, ?, ?)
        """,
        (name, price, stock)
    )

    connection.commit()
    connection.close()


# ==========================================================
# UPDATE PRODUCT
# ==========================================================

def update_product(product_id, name, price, stock):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE products
        SET name=?, price=?, stock=?
        WHERE id=?
        """,
        (name, price, stock, product_id)
    )

    connection.commit()
    connection.close()


# ==========================================================
# DELETE PRODUCT
# ==========================================================

def delete_product(product_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM products
        WHERE id=?
        """,
        (product_id,)
    )

    connection.commit()
    connection.close()


# ==========================================================
# TOTAL PRODUCTS
# ==========================================================

def total_products():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT COUNT(*) AS total_products
        FROM products
        """
    )

    total = cursor.fetchone()["total_products"]

    connection.close()

    return total


# ==========================================================
# LOW STOCK COUNT
# ==========================================================

def low_stock_count():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT COUNT(*) AS low_stock
        FROM products
        WHERE stock <= 5
        """
    )

    low_stock = cursor.fetchone()["low_stock"]

    connection.close()

    return low_stock


# ==========================================================
# GET PRODUCT PRICE & STOCK
# (Used while recording a sale)
# ==========================================================

def get_product_stock_price(product_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT price, stock
        FROM products
        WHERE id=?
        """,
        (product_id,)
    )

    product = cursor.fetchone()

    connection.close()

    return product


# ==========================================================
# UPDATE PRODUCT STOCK
# (After a Sale)
# ==========================================================

def update_stock(product_id, new_stock):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE products
        SET stock=?
        WHERE id=?
        """,
        (new_stock, product_id)
    )

    connection.commit()
    connection.close()