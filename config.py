# config.py

from dotenv import load_dotenv
import os

load_dotenv()

# Databricks Connection

SERVER_HOSTNAME = os.getenv("DATABRICKS_SERVER_HOSTNAME")
HTTP_PATH = os.getenv("DATABRICKS_HTTP_PATH")
ACCESS_TOKEN = os.getenv("DATABRICKS_TOKEN")

# App

APP_NAME = "RetailMart AI Platform"

THEME_COLOR = "#4F8BF9"

COMPANY_NAME = "RetailMart"

REFRESH_INTERVAL = 300