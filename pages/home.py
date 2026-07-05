import streamlit as st

from database import *

from components.header import *

from components.cards import *

from components.charts import *

from components.tables import *

from components.alerts import *

from utils.helpers import *


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(

    page_title="RetailMart AI",

    page_icon="🏠",

    layout="wide"

)


# ==========================================================
# LOAD DATA
# ==========================================================

sales_summary = get_sales_summary()

customer_summary = get_customer_summary()

inventory_summary = get_inventory_summary()

supplier_summary = get_supplier_summary()

forecast_summary = get_sales_forecast_summary()

customer_prediction_summary = get_customer_spend_summary()

inventory_prediction_summary = get_inventory_prediction_summary()

inventory_alerts = get_top_inventory_alerts()

forecast = get_future_forecast()

customer_clusters = get_customer_cluster_summary()


# ==========================================================
# PAGE HEADER
# ==========================================================

welcome_header(
    user_name="Operations Manager"
)

page_header(

    title="RetailMart AI Platform",

    subtitle="Business Operations Command Center",

    icon="🛒"

)

# ==========================================================
# TODAY'S OPERATIONAL SUMMARY
# ==========================================================

section_title(

    "Today's Operational Summary",

    "📊"

)

col1, col2, col3, col4 = st.columns(4)

with col1:

    metric_card(

        "Total Revenue",

        format_currency(

            sales_summary["total_revenue"]

        )

    )

with col2:

    metric_card(

        "Total Orders",

        format_number(

            sales_summary["total_orders"]

        )

    )

with col3:

    metric_card(

        "Customers",

        format_number(

            customer_summary["total_customers"]

        )

    )

with col4:

    metric_card(

        "Products",

        format_number(

            inventory_summary["total_products"]

        )

    )


col5, col6, col7, col8 = st.columns(4)

with col5:

    metric_card(

        "Average Order Value",

        format_currency(

            sales_summary["avg_order_value"]

        )

    )

with col6:

    metric_card(

        "Repeat Customers",

        format_number(

            customer_summary["repeat_customers"]

        )

    )

with col7:

    metric_card(

        "Low Stock Products",

        format_number(

            inventory_summary["low_stock_products"]

        )

    )

with col8:

    metric_card(

        "Active Suppliers",

        format_number(

            supplier_summary["total_suppliers"]

        )

    )

section_title(

    "Overall Business Health",

    "🟢"

)

operational_health(

    inventory_prediction_summary["high_risk_inventory"] == 0

)

# ==========================================================
# TODAY'S PRIORITIES
# ==========================================================

section_title(

    "Today's Priorities",

    "🎯"

)

priority_col1, priority_col2 = st.columns([3, 2])

with priority_col1:

    if inventory_prediction_summary["high_risk_inventory"] > 0:

        business_alert(

            title="Critical Inventory",

            message=f"{int(inventory_prediction_summary['high_risk_inventory'])} inventory items are classified as High Risk and require immediate replenishment.",

            severity="danger"

        )

    else:

        success_alert(

            "No High Risk inventory items detected."

        )

    if inventory_summary["low_stock_products"] > 0:

        business_alert(

            title="Low Stock Products",

            message=f"{int(inventory_summary['low_stock_products'])} products are below the recommended stock level.",

            severity="warning"

        )

    else:

        success_alert(

            "All products are above minimum stock levels."

        )

    ai_recommendation(

    "Review the upcoming sales forecast while planning procurement and inventory allocation."

    )

with priority_col2:

    status_card(

        title="Inventory Health",

        status="warning" if inventory_prediction_summary["high_risk_inventory"] > 0 else "success",

        message=f"{int(inventory_prediction_summary['high_risk_inventory'])} High Risk Items"

    )

    status_card(

        title="Forecast Status",

        status="success",

        message="Forecast model updated successfully."

    )

    status_card(

        title="Customer Segmentation",

        status="success",

        message="Customer clusters available."

    )

# ==========================================================
# OPERATIONAL SNAPSHOT
# ==========================================================

section_title(

    "Operational Snapshot",

    "📌"

)

snapshot1, snapshot2, snapshot3 = st.columns(3)

with snapshot1:

    insight_card(

        title="Customer Prediction",

        insight=(
            f"Average predicted customer spend is "
            f"{format_currency(customer_prediction_summary['average_prediction'])}."
        )

    )

with snapshot2:

    insight_card(

        title="Sales Forecast",

        insight=(
            f"Average monthly forecast revenue is "
            f"{format_currency(forecast_summary['average_forecast_revenue'])}."
        )

    )

with snapshot3:

    insight_card(

        title="Inventory",

        insight=(
            f"{int(inventory_prediction_summary['medium_risk_inventory'])} inventory items are currently under Medium Risk."
        )

    )

# ==========================================================
# BUSINESS RECOMMENDATIONS
# ==========================================================

section_title(

    "Recommended Actions",

    "🤖"

)

recommendation_card(

    title="Inventory",

    recommendation="Prioritize replenishment for High Risk inventory before the next procurement cycle."

)

recommendation_card(

    title="Customers",

    recommendation="Launch loyalty campaigns targeting High Value Customers to improve retention."

)

recommendation_card(

    title="Forecast",

    recommendation="Use upcoming revenue forecast while planning inventory purchasing."

)

recommendation_card(

    title="Operations",

    recommendation="Review stores with recurring inventory shortages and adjust reorder policies."

)

# ==========================================================
# FORECAST & CUSTOMER ANALYTICS
# ==========================================================

section_title(

    "Business Analytics",

    "📈"

)

analytics_col1, analytics_col2 = st.columns(2)

with analytics_col1:

    line_chart(

        dataframe=forecast,

        x="forecast_label",

        y="forecast_revenue",

        title="Revenue Forecast (Next 6 Months)"

    )

with analytics_col2:

    pie_chart(

        dataframe=customer_clusters,

        names="cluster_name",

        values="customers",

        title="Customer Segment Distribution"

    )

# ==========================================================
# INVENTORY & CUSTOMER ANALYSIS
# ==========================================================

analysis_col1, analysis_col2 = st.columns(2)

with analysis_col1:

    bar_chart(

        dataframe=customer_clusters,

        x="cluster_name",

        y="avg_total_spend",

        title="Average Spend by Customer Segment",

        color="cluster_name"

    )

with analysis_col2:

    bar_chart(

        dataframe=customer_clusters,

        x="cluster_name",

        y="customers",

        title="Customers per Segment",

        color="cluster_name"

    )

# ==========================================================
# CRITICAL INVENTORY ALERTS
# ==========================================================

section_title(

    "Critical Inventory Alerts",

    "🚨"

)

if inventory_alerts.empty:

    no_alerts()

else:

    display_table(

        inventory_alerts

    )

# ==========================================================
# FORECAST SNAPSHOT
# ==========================================================

section_title(

    "Forecast Snapshot",

    "📅"

)

top_records(

    forecast,

    rows=6

)

st.page_link(

    "pages/04_Forecast_Center.py",

    label="Open Forecast Center →",

    icon="📈"

)

# ==========================================================
# CUSTOMER SEGMENT SUMMARY
# ==========================================================

section_title(

    "Customer Cluster Summary",

    "👥"

)

top_records(

    customer_clusters,

    rows=3

)

st.page_link(

    "pages/03_Customer_Intelligence.py",

    label="Open Customer Intelligence →",

    icon="👥"

)