# Smart Vendor Assistant | AI-Powered Inventory & Demand Forecasting System

A full-stack Flask application that helps local vendors manage inventory, track sales, analyze business performance, and optimize stock planning using machine learning, weather intelligence, and festival-based demand insights.

---

## 🚀 Features

### 📦 Inventory Management
- Add, update, search, and delete products
- Real-time inventory tracking
- Low-stock monitoring and management

### 💰 Sales Management
- Record product sales
- Automatic stock deduction after sales
- Revenue and sales tracking

### 📊 Business Analytics
- Interactive business dashboard
- Revenue and sales statistics
- Top-selling product analysis
- Sales trend visualization

### 🤖 AI Demand Forecasting
- Demand prediction using Scikit-learn Linear Regression
- Historical sales-based forecasting
- Weather and festival-aware demand adjustments
- Automated restocking recommendations

### 🌦️ Weather Intelligence
- Live weather integration using OpenWeatherMap API
- Weather-based inventory suggestions
- Context-aware business recommendations

### 🎉 Festival Insights
- Manage upcoming festivals
- Festival-driven inventory planning
- Demand-aware stocking recommendations

### 🧠 AI Business Insights
- Combined analysis of inventory, sales, weather, and festivals
- Actionable recommendations for vendors
- Inventory optimization support

---
## 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │      User UI        │
                    │ HTML • CSS • JS     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     Flask App       │
                    │      app.py         │
                    └──────────┬──────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
        ▼                      ▼                      ▼
 ┌─────────────┐       ┌─────────────┐       ┌─────────────┐
 │ Inventory   │       │   Sales     │       │ Dashboard   │
 │ Management  │       │ Management  │       │ Analytics   │
 └──────┬──────┘       └──────┬──────┘       └──────┬──────┘
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              ▼
                    ┌─────────────────────┐
                    │   SQLite Database   │
                    │ Products • Sales    │
                    │ Users • Festivals   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ AI Prediction Engine│
                    │ Linear Regression   │
                    └──────────┬──────────┘
                               │
                 ┌─────────────┼─────────────┐
                 │                           │
                 ▼                           ▼
      ┌──────────────────┐       ┌──────────────────┐
      │ Weather Service  │       │ Festival Module  │
      │ OpenWeather API  │       │ Upcoming Events  │
      └─────────┬────────┘       └─────────┬────────┘
                │                          │
                └──────────┬───────────────┘
                           ▼
                ┌──────────────────────┐
                │ Business Insights &  │
                │ Restock Suggestions  │
                └──────────────────────┘
```
---

## 🛠️ Tech Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python |
| Backend Framework | Flask |
| Database | SQLite |
| Machine Learning | Scikit-learn |
| ML Algorithm | Linear Regression |
| Numerical Computing | NumPy |
| Frontend | HTML, CSS, JavaScript |
| Template Engine | Jinja2 |
| API Integration | OpenWeatherMap API |
| Version Control | Git & GitHub |

---

## 📂 Project Structure

```text
SmartVendorAssistant/
│
├── database/
│   └── db.py
│
├── models/
│   ├── ai.py
│   ├── festival.py
│   ├── product.py
│   ├── sales.py
│   └── user.py
│
├── routes/
│   ├── ai.py
│   ├── auth.py
│   ├── dashboard.py
│   ├── festival.py
│   ├── inventory.py
│   ├── sales.py
│   └── weather.py
│
├── services/
│   ├── predictor.py
│   └── weather_service.py
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│
├── utils/
│   └── config.py
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🤖 Demand Forecasting Workflow

```text
Historical Sales Data
          │
          ▼
Linear Regression Model
          │
          ▼
Base Demand Prediction
          │
 ┌────────┴─────────┐
 ▼                  ▼
Weather Rules   Festival Rules
          │
          ▼
Adjusted Demand
          │
          ▼
Restock Recommendation
```

### Restock Logic

```python
restock_quantity = max(
    0,
    predicted_demand - current_stock
)
```

---

## 🔒 Security Features

- Session-based authentication
- Protected application routes
- Environment-based configuration management
- Secure API key handling using `.env`
- Sensitive files excluded from version control

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/pateelmeghana3/SmartVendorAssistant.git
cd SmartVendorAssistant
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Environment

**Windows**

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file and add your secret keys and OpenWeatherMap API credentials.

```env
SECRET_KEY=your_secret_key
OPENWEATHER_API_KEY=your_api_key
```

### 6. Run Application

```bash
python app.py
```

---

## 🎯 Key Highlights

- Developed a full-stack business management platform for local vendors.
- Implemented inventory and sales lifecycle management.
- Built demand forecasting using Linear Regression.
- Integrated real-time weather data through OpenWeatherMap API.
- Designed a recommendation engine based on weather and festival trends.
- Generated actionable business insights from operational data.
- Applied CRUD operations, session management, and database design using Flask and SQLite.

---

## 🚀 Future Enhancements

- Advanced forecasting models (Random Forest, XGBoost)
- Cloud deployment (AWS/Azure)
- Role-based access control
- Email and SMS inventory alerts
- Advanced analytics dashboards
- Personalized recommendation engine
- Mobile-responsive enhancements

---

## 👩‍💻 Author

**Pateel Meghana Reddy**

B.E. Computer Science & Engineering (AI & ML)  
CMR Institute of Technology, Bengaluru

GitHub: https://github.com/pateelmeghana3

---

## 📄 License

This project is developed for educational, research, and portfolio purposes.