from sklearn.linear_model import LinearRegression
import numpy as np


# ==========================================================
# TRAIN MODEL
# ==========================================================

def train_model(sales_history):

    """
    sales_history = [10, 12, 15, 18, 20]
    """

    if len(sales_history) < 2:
        return None

    X = np.arange(len(sales_history)).reshape(-1, 1)
    y = np.array(sales_history)

    model = LinearRegression()
    model.fit(X, y)

    return model


# ==========================================================
# PREDICT NEXT SALE
# ==========================================================

def predict_next_sale(sales_history):

    model = train_model(sales_history)

    if model is None:
        return 0

    next_day = np.array([[len(sales_history)]])

    prediction = model.predict(next_day)

    return max(0, round(float(prediction[0])))


# ==========================================================
# APPLY WEATHER & FESTIVAL EFFECT
# ==========================================================

def adjust_prediction(prediction, temperature, weather, festival=False):

    demand = prediction

    # Hot weather
    if temperature >= 35:
        demand *= 1.20

    # Rain
    if weather.lower() == "rain":
        demand *= 1.15

    # Festival
    if festival:
        demand *= 1.30

    return round(demand)


# ==========================================================
# FINAL AI PREDICTION
# ==========================================================

def predict(product):

    """
    product dictionary

    {
        "sales":[5,6,7,8],
        "stock":20,
        "temp":36,
        "condition":"Rain",
        "festival":True
    }

    """

    base_prediction = predict_next_sale(product["sales"])

    final_prediction = adjust_prediction(
        base_prediction,
        product["temp"],
        product["condition"],
        product["festival"]
    )

    restock = max(0, final_prediction - product["stock"])

    return {

        "predicted": final_prediction,

        "restock": restock

    }