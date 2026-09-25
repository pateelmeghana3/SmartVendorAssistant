from flask import Blueprint, render_template, request, redirect, session

from models.sales import (
    get_all_sales,
    add_sale,
    total_sales,
    total_revenue
)

from models.product import (
    get_all_products,
    get_product_stock_price,
    update_stock
)

sales_bp = Blueprint("sales", __name__)


# ==========================================================
# SALES PAGE
# ==========================================================

@sales_bp.route("/sales")
def sales():

    if "user" not in session:
        return redirect("/login")

    sales_data = get_all_sales()
    products = get_all_products()

    return render_template(
        "sales.html",
        sales=sales_data,
        products=products
    )


# ==========================================================
# ADD SALE
# ==========================================================

@sales_bp.route("/add_sale", methods=["POST"])
def create_sale():

    if "user" not in session:
        return redirect("/login")

    product_id = int(request.form["product_id"])
    quantity = int(request.form["quantity"])

    product = get_product_stock_price(product_id)

    if not product:
        return "Product not found"

    price = product["price"]
    stock = product["stock"]

    if quantity > stock:
        return "Not enough stock"

    total_price = price * quantity

    # Add sale
    add_sale(product_id, quantity, total_price)

    # Update stock
    new_stock = stock - quantity
    update_stock(product_id, new_stock)

    return redirect("/sales")