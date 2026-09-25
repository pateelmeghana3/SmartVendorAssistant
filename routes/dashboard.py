from flask import Blueprint, render_template, redirect, session

from models.product import (
    total_products,
    low_stock_count
)

from models.sales import (
    total_sales,
    total_revenue,
    top_product,
    sales_chart_data
)

# ==========================================================
# CREATE BLUEPRINT
# ==========================================================

dashboard_bp = Blueprint("dashboard", __name__)


# ==========================================================
# DASHBOARD
# ==========================================================

@dashboard_bp.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/login")

    return render_template(
        "dashboard.html",
        total_products=total_products(),
        low_stock=low_stock_count(),
        total_sales=total_sales(),
        revenue=total_revenue(),
        top_product=top_product(),
        chart_data=sales_chart_data()
    )