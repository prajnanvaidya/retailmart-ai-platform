import streamlit as st

from datetime import datetime


# ==========================================================
# PAGE HEADER
# ==========================================================

def page_header(

    title: str,

    subtitle: str = "",

    icon: str = "📊"

):
    """
    Displays a professional page header.
    """

    col1, col2 = st.columns([4, 1])

    with col1:

        st.title(f"{icon} {title}")

        if subtitle:

            st.caption(subtitle)

    with col2:

        st.metric(

            label="Today",

            value=datetime.now().strftime("%d %b %Y")

        )

    st.divider()


# ==========================================================
# WELCOME HEADER
# ==========================================================

def welcome_header(

    user_name="User"

):

    hour = datetime.now().hour

    if hour < 12:

        greeting = "Good Morning"

    elif hour < 17:

        greeting = "Good Afternoon"

    else:

        greeting = "Good Evening"

    st.markdown(

        f"""

# {greeting}, {user_name} 👋

Welcome back to the **RetailMart AI Platform**.

"""

    )

    st.divider()


# ==========================================================
# SECTION TITLE
# ==========================================================

def section_title(

    title,

    icon="📌"

):

    st.markdown(

        f"## {icon} {title}"

    )


# ==========================================================
# SUB SECTION
# ==========================================================

def subsection(

    title

):

    st.markdown(

        f"### {title}"

    )


# ==========================================================
# LAST UPDATED
# ==========================================================

def last_updated():

    st.caption(

        f"Last Updated : {datetime.now().strftime('%d %b %Y %I:%M %p')}"

    )


# ==========================================================
# PAGE FOOTER
# ==========================================================

def page_footer():

    st.divider()

    st.caption(

        "RetailMart AI Platform • Powered by Databricks, Streamlit & Machine Learning"

    )