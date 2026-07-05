# ==========================================================
# RETAILMART AI PLATFORM
# SQL QUERIES
# ==========================================================

# ==========================================================
# HOME PAGE
# ==========================================================

SALES_SUMMARY_QUERY = """
SELECT *
FROM retailmart.gold.gold_sales_summary
"""

CUSTOMER_SUMMARY_QUERY = """
SELECT *
FROM retailmart.gold.gold_customer_summary
"""

INVENTORY_SUMMARY_QUERY = """
SELECT *
FROM retailmart.gold.gold_inventory_summary
"""

SUPPLIER_SUMMARY_QUERY = """
SELECT *
FROM retailmart.gold.gold_supplier_summary
"""

PRODUCT_SUMMARY_QUERY = """
SELECT *
FROM retailmart.gold.gold_product_summary
"""

# ==========================================================
# ML MODEL SUMMARY
# ==========================================================

CUSTOMER_SPEND_SUMMARY_QUERY = """
SELECT *
FROM retailmart.ml_db.customer_prediction_summary
"""

CUSTOMER_CLUSTER_SUMMARY_QUERY = """
SELECT *
FROM retailmart.ml_db.customer_cluster_summary
"""

FORECAST_SUMMARY_QUERY = """
SELECT *
FROM retailmart.ml_db.sales_forecast_dashboard_summary
"""

INVENTORY_PREDICTION_SUMMARY_QUERY = """
SELECT *
FROM retailmart.ml_db.inventory_dashboard_summary
"""

# ==========================================================
# INVENTORY INTELLIGENCE
# ==========================================================

INVENTORY_DETAILS_QUERY = """
SELECT *
FROM retailmart.ml_db.inventory_dashboard_details
"""

HIGH_RISK_INVENTORY_QUERY = """
SELECT *
FROM retailmart.ml_db.inventory_dashboard_details
WHERE predicted_risk='High Risk'
ORDER BY stock_gap ASC
"""

MEDIUM_RISK_INVENTORY_QUERY = """
SELECT *
FROM retailmart.ml_db.inventory_dashboard_details
WHERE predicted_risk='Medium Risk'
ORDER BY stock_gap ASC
"""

LOW_RISK_INVENTORY_QUERY = """
SELECT *
FROM retailmart.ml_db.inventory_dashboard_details
WHERE predicted_risk='Low Risk'
"""

INVENTORY_CATEGORY_QUERY = """
SELECT *
FROM retailmart.ml_db.inventory_category_summary
"""

INVENTORY_PREDICTION_QUERY = """
SELECT *
FROM retailmart.ml_db.inventory_final_predictions
"""

TOP_INVENTORY_ALERTS_QUERY = """
SELECT
store_name,
city,
category,
predicted_risk,
stock_quantity,
reorder_level,
stock_gap
FROM retailmart.ml_db.inventory_dashboard_details
WHERE predicted_risk='High Risk'
ORDER BY stock_gap ASC
LIMIT 10
"""
# ==========================================================
# CUSTOMER INTELLIGENCE
# ==========================================================

CUSTOMER_CLUSTER_QUERY = """
SELECT *
FROM retailmart.ml_db.customer_cluster_predictions
"""

CUSTOMER_CLUSTER_SUMMARY_QUERY = """
SELECT *
FROM retailmart.ml_db.customer_cluster_summary
"""

CUSTOMER_SPEND_PREDICTION_QUERY = """
SELECT *
FROM retailmart.ml_db.customer_spend_predictions
"""

CUSTOMER_SPEND_KPI_QUERY = """
SELECT *
FROM retailmart.ml_db.customer_spend_dashboard_kpi
"""

CUSTOMER_LOYALTY_QUERY = """
SELECT *
FROM retailmart.ml_db.customer_spend_loyalty_summary
"""

CUSTOMER_SPEND_DISTRIBUTION_QUERY = """
SELECT *
FROM retailmart.ml_db.customer_spend_prediction_distribution
"""

TOP_CUSTOMERS_QUERY = """
SELECT
customer_id,
prediction,
label
FROM retailmart.ml_db.customer_spend_top_customers
ORDER BY prediction DESC
"""

TOP_20_CUSTOMERS_QUERY = """
SELECT *
FROM retailmart.ml_db.customer_spend_dashboard_kpi
ORDER BY prediction DESC
LIMIT 20
"""

HIGH_VALUE_CUSTOMERS_QUERY = """
SELECT *
FROM retailmart.ml_db.customer_cluster_predictions
WHERE cluster_name='High Value Customers'
ORDER BY total_spend DESC
"""

REGULAR_CUSTOMERS_QUERY = """
SELECT *
FROM retailmart.ml_db.customer_cluster_predictions
WHERE cluster_name='Regular Customers'
"""

BUDGET_CUSTOMERS_QUERY = """
SELECT *
FROM retailmart.ml_db.customer_cluster_predictions
WHERE cluster_name='Budget Customers'
"""

# ==========================================================
# SALES FORECAST
# ==========================================================

FUTURE_FORECAST_QUERY = """
SELECT *
FROM retailmart.ml_db.future_sales_forecast
ORDER BY forecast_date
"""

FORECAST_DASHBOARD_QUERY = """
SELECT *
FROM retailmart.ml_db.sales_forecast_dashboard
ORDER BY forecast_date
"""

FORECAST_HISTORY_QUERY = """
SELECT *
FROM retailmart.ml_db.sales_forecast_predictions
ORDER BY forecast_date
"""

LATEST_FORECAST_QUERY = """
SELECT *
FROM retailmart.ml_db.future_sales_forecast
ORDER BY forecast_date DESC
LIMIT 1
"""

NEXT_MONTH_FORECAST_QUERY = """
SELECT *
FROM retailmart.ml_db.future_sales_forecast
ORDER BY forecast_date
LIMIT 1
"""

FORECAST_TREND_QUERY = """
SELECT
forecast_date,
forecast_revenue
FROM retailmart.ml_db.future_sales_forecast
ORDER BY forecast_date
"""

FORECAST_ORDERS_QUERY = """
SELECT
forecast_date,
monthly_orders
FROM retailmart.ml_db.future_sales_forecast
ORDER BY forecast_date
"""

# ==========================================================
# PRODUCT INTELLIGENCE
# ==========================================================

PRODUCT_PERFORMANCE_QUERY = """
SELECT *
FROM retailmart.gold.gold_product_performance
"""

CATEGORY_PERFORMANCE_QUERY = """
SELECT *
FROM retailmart.gold.gold_product_category_performance
"""

ORDER_STATUS_QUERY = """
SELECT *
FROM retailmart.gold.gold_order_status_performance
"""

TOP_PRODUCTS_QUERY = """
SELECT *
FROM retailmart.gold.gold_product_performance
ORDER BY product_revenue DESC
LIMIT 20
"""

TOP_PROFIT_PRODUCTS_QUERY = """
SELECT *
FROM retailmart.gold.gold_product_performance
ORDER BY product_profit DESC
LIMIT 20
"""

TOP_RATED_PRODUCTS_QUERY = """
SELECT *
FROM retailmart.gold.gold_product_performance
ORDER BY product_rating DESC
LIMIT 20
"""

CATEGORY_REVENUE_QUERY = """
SELECT
category,
category_revenue
FROM retailmart.gold.gold_product_category_performance
ORDER BY category_revenue DESC
"""

# ==========================================================
# SUPPLIER INTELLIGENCE
# ==========================================================

SUPPLIER_PERFORMANCE_QUERY = """
SELECT *
FROM retailmart.gold.gold_supplier_performance
"""

SUPPLIER_DEPENDENCY_QUERY = """
SELECT *
FROM retailmart.gold.gold_supplier_dependency
"""

SUPPLIER_RISK_PRODUCTS_QUERY = """
SELECT *
FROM retailmart.gold.gold_supplier_risk_products
"""

PROCUREMENT_METRICS_QUERY = """
SELECT *
FROM retailmart.gold.gold_procurement_metrics
"""

TOP_SUPPLIERS_QUERY = """
SELECT *
FROM retailmart.gold.gold_supplier_performance
ORDER BY inventory_value DESC
LIMIT 20
"""

HIGH_DEPENDENCY_SUPPLIERS_QUERY = """
SELECT *
FROM retailmart.gold.gold_supplier_dependency
WHERE dependency_level='High'
"""

MEDIUM_DEPENDENCY_SUPPLIERS_QUERY = """
SELECT *
FROM retailmart.gold.gold_supplier_dependency
WHERE dependency_level='Medium'
"""
