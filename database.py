from databricks import sql
import pandas as pd
import streamlit as st

from config import (
    SERVER_HOSTNAME,
    HTTP_PATH,
    ACCESS_TOKEN
)

from utils.sql_queries import *


# ==========================================================
# DATABASE CONNECTION
# ==========================================================

@st.cache_resource
def get_connection():
    """
    Creates and caches the Databricks SQL connection.
    """

    return sql.connect(
        server_hostname=SERVER_HOSTNAME,
        http_path=HTTP_PATH,
        access_token=ACCESS_TOKEN
    )


# ==========================================================
# QUERY EXECUTION
# ==========================================================

@st.cache_data(ttl=300)
def execute_query(query: str) -> pd.DataFrame:
    """
    Executes a SQL query and returns a Pandas DataFrame.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(query)

    rows = cursor.fetchall()

    columns = [column[0] for column in cursor.description]

    cursor.close()

    return pd.DataFrame(
        rows,
        columns=columns
    )


# ==========================================================
# GENERIC HELPERS
# ==========================================================

def get_table(query):

    return execute_query(query)


def get_single_row(query):

    df = execute_query(query)

    if df.empty:
        return None

    return df.iloc[0]


def get_scalar(query):

    df = execute_query(query)

    if df.empty:
        return None

    return df.iloc[0, 0]

# ==========================================================
# HOME PAGE
# ==========================================================

def get_sales_summary():

    return get_single_row(
        SALES_SUMMARY_QUERY
    )


def get_customer_summary():

    return get_single_row(
        CUSTOMER_SUMMARY_QUERY
    )


def get_inventory_summary():

    return get_single_row(
        INVENTORY_SUMMARY_QUERY
    )


def get_supplier_summary():

    return get_single_row(
        SUPPLIER_SUMMARY_QUERY
    )


def get_product_summary():

    return get_table(
        PRODUCT_SUMMARY_QUERY
    )


def get_sales_forecast_summary():

    return get_single_row(
        FORECAST_SUMMARY_QUERY
    )


def get_customer_spend_summary():

    return get_single_row(
        CUSTOMER_SPEND_SUMMARY_QUERY
    )


def get_inventory_prediction_summary():

    return get_single_row(
        INVENTORY_PREDICTION_SUMMARY_QUERY
    )

# ==========================================================
# INVENTORY
# ==========================================================

def get_inventory_details():

    return get_table(
        INVENTORY_DETAILS_QUERY
    )


def get_inventory_predictions():

    return get_table(
        INVENTORY_PREDICTION_QUERY
    )


def get_inventory_category_summary():

    return get_table(
        INVENTORY_CATEGORY_QUERY
    )


def get_high_risk_inventory():

    return get_table(
        HIGH_RISK_INVENTORY_QUERY
    )


def get_medium_risk_inventory():

    return get_table(
        MEDIUM_RISK_INVENTORY_QUERY
    )


def get_low_risk_inventory():

    return get_table(
        LOW_RISK_INVENTORY_QUERY
    )


def get_top_inventory_alerts():

    return get_table(
        TOP_INVENTORY_ALERTS_QUERY
    )

# ==========================================================
# CUSTOMER
# ==========================================================

def get_customer_clusters():

    return get_table(
        CUSTOMER_CLUSTER_QUERY
    )


def get_customer_cluster_summary():

    return get_table(
        CUSTOMER_CLUSTER_SUMMARY_QUERY
    )


def get_customer_spend_predictions():

    return get_table(
        CUSTOMER_SPEND_PREDICTION_QUERY
    )


def get_customer_spend_kpi():

    return get_single_row(
        CUSTOMER_SPEND_KPI_QUERY
    )


def get_customer_loyalty_summary():

    return get_table(
        CUSTOMER_LOYALTY_QUERY
    )


def get_customer_distribution():

    return get_table(
        CUSTOMER_SPEND_DISTRIBUTION_QUERY
    )


def get_top_customers():

    return get_table(
        TOP_CUSTOMERS_QUERY
    )


def get_high_value_customers():

    return get_table(
        HIGH_VALUE_CUSTOMERS_QUERY
    )


def get_regular_customers():

    return get_table(
        REGULAR_CUSTOMERS_QUERY
    )


def get_budget_customers():

    return get_table(
        BUDGET_CUSTOMERS_QUERY
    )

# ==========================================================
# FORECAST
# ==========================================================

def get_future_forecast():

    return get_table(
        FUTURE_FORECAST_QUERY
    )


def get_forecast_dashboard():

    return get_table(
        FORECAST_DASHBOARD_QUERY
    )


def get_forecast_history():

    return get_table(
        FORECAST_HISTORY_QUERY
    )


def get_latest_forecast():

    return get_single_row(
        LATEST_FORECAST_QUERY
    )


def get_next_month_forecast():

    return get_single_row(
        NEXT_MONTH_FORECAST_QUERY
    )


def get_forecast_trend():

    return get_table(
        FORECAST_TREND_QUERY
    )


def get_forecast_orders():

    return get_table(
        FORECAST_ORDERS_QUERY
    )

# ==========================================================
# PRODUCTS
# ==========================================================

def get_product_performance():

    return get_table(
        PRODUCT_PERFORMANCE_QUERY
    )


def get_category_performance():

    return get_table(
        CATEGORY_PERFORMANCE_QUERY
    )


def get_order_status_performance():

    return get_table(
        ORDER_STATUS_QUERY
    )


def get_top_products():

    return get_table(
        TOP_PRODUCTS_QUERY
    )


def get_top_profit_products():

    return get_table(
        TOP_PROFIT_PRODUCTS_QUERY
    )


def get_top_rated_products():

    return get_table(
        TOP_RATED_PRODUCTS_QUERY
    )

# ==========================================================
# SUPPLIERS
# ==========================================================

def get_supplier_performance():

    return get_table(
        SUPPLIER_PERFORMANCE_QUERY
    )


def get_supplier_dependency():

    return get_table(
        SUPPLIER_DEPENDENCY_QUERY
    )


def get_supplier_risk_products():

    return get_table(
        SUPPLIER_RISK_PRODUCTS_QUERY
    )


def get_procurement_metrics():

    return get_table(
        PROCUREMENT_METRICS_QUERY
    )


def get_top_suppliers():

    return get_table(
        TOP_SUPPLIERS_QUERY
    )


def get_high_dependency_suppliers():

    return get_table(
        HIGH_DEPENDENCY_SUPPLIERS_QUERY
    )


def get_medium_dependency_suppliers():

    return get_table(
        MEDIUM_DEPENDENCY_SUPPLIERS_QUERY
    )

