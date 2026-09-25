from database.db import get_connection
from services.predictor import predict


# ==========================================================
# AI DEMAND PREDICTION
# ==========================================================

def demand_prediction(weather, festival):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            name,
            stock
        FROM products
    """)

    products = cursor.fetchall()

    predictions = []

    for product in products:

        # Last 7 sales
        cursor.execute("""
            SELECT quantity_sold
            FROM sales
            WHERE product_id=?
            ORDER BY id DESC
            LIMIT 7
        """, (product["id"],))

        rows = cursor.fetchall()

        sales_history = [row["quantity_sold"] for row in rows]

        # If there isn't enough data,
        # create a simple history
        if len(sales_history) < 2:

            sales_history = [1, 2]

        sales_history.reverse()

        result = predict({

            "sales": sales_history,

            "stock": product["stock"],

            "temp": weather["temp"],

            "condition": weather["condition"],

            "festival": festival

        })

        predictions.append({

            "product": product["name"],

            "stock": product["stock"],

            "predicted": result["predicted"],

            "restock": result["restock"],

            "temperature": weather["temp"],

            "condition": weather["condition"]

        })

    connection.close()

    return predictions