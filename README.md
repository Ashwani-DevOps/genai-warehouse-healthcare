![CI](https://github.com/<your-username>/<your-repo>/actions/workflows/ci.yml/badge.svg)

# GenAI Warehouse Healthcheck System

Modular Flask + Streamlit app for inventory validation, demand forecasting, and alerting.

## Features
- 📦 Inventory validation
- 📈 Forecasting with Prophet
- 📊 Plotly + Streamlit visualization
- 🔔 Gmail + Slack alerts
- 🐳 Dockerized
- ✅ CI/CD with GitHub Actions
- 🛡️ flake8 + gitleaks + OWASP ZAP
- 📦 GitHub Container Registry

## Setup
1. Copy `.env.example` → `.env`
2. Run: `docker build -t genai-warehouse . && docker run -p 5000:5000 genai-warehouse`
