import streamlit as st

from datetime import datetime

from config import APP_NAME
from config import COMPANY_NAME


# ==========================================================
# SIDEBAR
# ==========================================================

def show_sidebar():

    with st.sidebar:

        # -----------------------------------------------
        # LOGO / TITLE
        # -----------------------------------------------

        st.title("🛒 RetailMart AI")

        st.caption(
            "AI-Powered Retail Intelligence Platform"
        )

        st.divider()

        # -----------------------------------------------
        # USER
        # -----------------------------------------------

        st.subheader("👤 User")

        st.write("Retail Operations Manager")

        st.caption(COMPANY_NAME)

        st.divider()

        # -----------------------------------------------
        # PLATFORM STATUS
        # -----------------------------------------------

        st.subheader("🖥 Platform Status")

        st.success("Connected")

        st.caption("Databricks SQL Warehouse")

        st.divider()

        # -----------------------------------------------
        # LAST REFRESH
        # -----------------------------------------------

        st.subheader("🕒 Session")

        st.write(
            datetime.now().strftime(
                "%d %b %Y"
            )
        )

        st.caption(
            datetime.now().strftime(
                "%I:%M %p"
            )
        )

        if st.button(
            "🔄 Refresh Data",
            use_container_width=True
        ):
            st.cache_data.clear()
            st.rerun()

        st.divider()

        # -----------------------------------------------
        # QUICK MODULES
        # -----------------------------------------------

        st.subheader("📌 Available Modules")

        st.markdown(
            """
- 🏠 Home

- 📦 Inventory Intelligence

- 👥 Customer Intelligence

- 📈 Forecast Center

- 📦 Product Intelligence

- 🚚 Supplier Intelligence

- 🤖 AI Insights

- 📄 Reports

- 📊 Analytics Dashboard

- ℹ About
"""
        )

        st.divider()

        # -----------------------------------------------
        # VERSION
        # -----------------------------------------------

        st.caption(APP_NAME)

        st.caption("Version 1.0")

        st.caption("Built with Streamlit + Databricks")