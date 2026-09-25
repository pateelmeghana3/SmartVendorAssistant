from flask import Flask

from database.db import create_database
from utils.config import SECRET_KEY

# Import Blueprints
from routes.auth import auth_bp
from routes.dashboard import dashboard_bp
from routes.inventory import inventory_bp
from routes.sales import sales_bp
from routes.ai import ai_bp
from routes.weather import weather_bp
from routes.festival import festival_bp

# Create Flask App
app = Flask(__name__)
app.secret_key = SECRET_KEY

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(inventory_bp)
app.register_blueprint(sales_bp)
app.register_blueprint(ai_bp)
app.register_blueprint(weather_bp)
app.register_blueprint(festival_bp)

# ==========================================================
# RUN APPLICATION
# ==========================================================
if __name__ == "__main__":
    create_database()
    app.run(
        debug=False,
        use_reloader=False
    )