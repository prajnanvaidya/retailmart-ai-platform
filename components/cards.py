import streamlit as st


# ==========================================================
# KPI METRIC CARD
# ==========================================================

def metric_card(
    title,
    value,
    delta=None,
    help_text=None
):

    st.metric(

        label=title,

        value=value,

        delta=delta,

        help=help_text

    )


# ==========================================================
# STATUS CARD
# ==========================================================

def status_card(

    title,

    status,

    message

):

    status_icons = {

        "success": "🟢",

        "warning": "🟠",

        "danger": "🔴",

        "info": "🔵"

    }

    icon = status_icons.get(

        status,

        "⚪"

    )

    with st.container(

        border=True

    ):

        st.subheader(

            f"{icon} {title}"

        )

        st.write(

            message

        )


# ==========================================================
# AI INSIGHT CARD
# ==========================================================

def insight_card(

    title,

    insight

):

    with st.container(

        border=True

    ):

        st.markdown(

            f"### 💡 {title}"

        )

        st.write(

            insight

        )


# ==========================================================
# BUSINESS RECOMMENDATION CARD
# ==========================================================

def recommendation_card(

    title,

    recommendation

):

    with st.container(

        border=True

    ):

        st.markdown(

            f"### 🎯 {title}"

        )

        st.success(

            recommendation

        )


# ==========================================================
# ALERT CARD
# ==========================================================

def alert_card(

    title,

    description,

    severity="warning"

):

    with st.container(

        border=True

    ):

        st.markdown(

            f"### 🚨 {title}"

        )

        if severity == "danger":

            st.error(

                description

            )

        elif severity == "warning":

            st.warning(

                description

            )

        elif severity == "success":

            st.success(

                description

            )

        else:

            st.info(

                description

            )


# ==========================================================
# SECTION HEADER
# ==========================================================

def section_header(

    title,

    subtitle=None

):

    st.title(

        title

    )

    if subtitle:

        st.caption(

            subtitle

        )

    st.divider()


# ==========================================================
# EMPTY STATE
# ==========================================================

def empty_state(

    message="No data available."

):

    st.info(

        message

    )


# ==========================================================
# LOADING PLACEHOLDER
# ==========================================================

def loading_state(

    text="Loading..."

):

    with st.spinner(

        text

    ):

        pass