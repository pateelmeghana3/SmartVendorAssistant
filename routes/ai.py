from flask import Blueprint, render_template, redirect, session

from models.ai import demand_prediction

from models.sales import (
    total_revenue,
    total_units_sold,
    top_product
)

from models.product import (
    low_stock_count
)

from models.festival import (
    next_festival
)

ai_bp = Blueprint("ai", __name__)


# ==========================================================
# AI INSIGHTS
# ==========================================================

@ai_bp.route("/ai_insights")
def ai_insights():

    if "user" not in session:
        return redirect("/login")

    # ======================================================
    # WEATHER
    # (Replace later with live weather API values)
    # ======================================================

    weather = {
        "temp": 36,
        "condition": "Rain"
    }

    # ======================================================
    # FESTIVAL
    # ======================================================

    upcoming = next_festival()
    festival = upcoming is not None

    # ======================================================
    # MACHINE LEARNING PREDICTION
    # ======================================================

    predictions = demand_prediction(weather, festival)

    # ======================================================
    # BUSINESS ANALYTICS
    # ======================================================

    revenue = total_revenue()
    total_units = total_units_sold()
    low_stock = low_stock_count()
    top = top_product()

    insights = []

    # ======================================================
    # SALES
    # ======================================================

    if total_units < 10:
        insights.append("⚠ Sales are low. Consider promotional offers.")
    elif total_units < 30:
        insights.append("📊 Sales are stable.")
    else:
        insights.append("🔥 Excellent sales performance.")

    # ======================================================
    # REVENUE
    # ======================================================

    if revenue < 1000:
        insights.append("💰 Revenue is below target.")
    elif revenue < 5000:
        insights.append("📈 Revenue is steadily improving.")
    else:
        insights.append("🚀 Business revenue is performing very well.")

    # ======================================================
    # STOCK
    # ======================================================

    if low_stock > 0:
        insights.append(f"📦 {low_stock} product(s) need immediate restocking.")
    else:
        insights.append("✅ Inventory is healthy.")

    # ======================================================
    # TOP PRODUCT
    # ======================================================

    if top:

        qty = top["total_qty"] if "total_qty" in top.keys() else 0

        insights.append(
            f"🏆 Top Product: {top['name']} ({qty} units sold)"
        )

    else:

        insights.append("🏆 No sales have been recorded yet.")

    # ======================================================
    # WEATHER INSIGHTS
    # ======================================================

    if weather["temp"] >= 35:
        insights.append(
            "☀ Hot weather detected. Cold drinks and ice cream demand is expected to increase."
        )

    elif weather["temp"] <= 20:
        insights.append(
            "❄ Cooler weather detected. Tea, coffee and bakery items may sell more."
        )

    if weather["condition"].lower() == "rain":
        insights.append(
            "🌧 Rain expected. Umbrellas, raincoats and hot beverages may experience higher demand."
        )

    # ======================================================
    # FESTIVAL INSIGHTS
    # ======================================================

    if upcoming:

        insights.append(
            f"🎉 Upcoming Festival: {upcoming['festival_name']}"
        )

        festival_name = upcoming["festival_name"].lower()

        if "diwali" in festival_name:
            insights.append("🪔 Stock diyas, sweets, lights and gift hampers.")

        elif "christmas" in festival_name:
            insights.append("🎄 Increase cakes, chocolates and gift items.")

        elif "sankranti" in festival_name:
            insights.append("🌾 Increase rice, jaggery and sesame products.")

        elif "ugadi" in festival_name:
            insights.append("🥭 Stock mangoes, neem flowers and traditional sweets.")

        elif "ramzan" in festival_name:
            insights.append("🌙 Increase dates, milk and dry fruits.")

    else:

        insights.append("📅 No upcoming festival found.")

    # ======================================================
    # RENDER
    # ======================================================

    return render_template(
        "ai_insights.html",
        predictions=predictions,
        insights=insights,
        revenue=revenue,
        total_units=total_units,
        low_stock=low_stock,
        top_product=top,
        weather=weather,
        upcoming=upcoming
    )