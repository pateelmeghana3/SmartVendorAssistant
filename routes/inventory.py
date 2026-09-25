from flask import Blueprint, render_template, request, redirect, session

from models.product import (
    get_all_products,
    search_products,
    get_product,
    add_product,
    update_product,
    delete_product
)

# ==========================================================
# CREATE BLUEPRINT
# ==========================================================

inventory_bp = Blueprint("inventory", __name__)


# ==========================================================
# INVENTORY PAGE
# ==========================================================

@inventory_bp.route("/inventory")
def inventory():

    if "user" not in session:
        return redirect("/login")

    search = request.args.get("search")

    if search:
        products = search_products(search)
    else:
        products = get_all_products()

    return render_template(
        "inventory.html",
        products=products,
        search=search
    )


# ==========================================================
# ADD PRODUCT
# ==========================================================

@inventory_bp.route("/add_product", methods=["GET", "POST"])
def add_new_product():

    if "user" not in session:
        return redirect("/login")

    if request.method == "POST":

        name = request.form["name"]
        price = request.form["price"]
        stock = request.form["stock"]

        add_product(name, price, stock)

        return redirect("/inventory")

    return render_template("add_product.html")


# ==========================================================
# UPDATE PRODUCT
# ==========================================================

@inventory_bp.route("/update_product/<int:id>", methods=["GET", "POST"])
def edit_product(id):

    if "user" not in session:
        return redirect("/login")

    if request.method == "POST":

        name = request.form["name"]
        price = request.form["price"]
        stock = request.form["stock"]

        update_product(id, name, price, stock)

        return redirect("/inventory")

    product = get_product(id)

    return render_template(
        "update_product.html",
        product=product
    )


# ==========================================================
# DELETE PRODUCT
# ==========================================================

@inventory_bp.route("/delete_product/<int:id>")
def remove_product(id):

    if "user" not in session:
        return redirect("/login")

    delete_product(id)

    return redirect("/inventory")