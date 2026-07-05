import streamlit as st


# ==========================================================
# SUCCESS ALERT
# ==========================================================

def success_alert(message: str):

    st.success(message)


# ==========================================================
# INFO ALERT
# ==========================================================

def info_alert(message: str):

    st.info(message)


# ==========================================================
# WARNING ALERT
# ==========================================================

def warning_alert(message: str):

    st.warning(message)


# ==========================================================
# ERROR ALERT
# ==========================================================

def error_alert(message: str):

    st.error(message)


# ==========================================================
# STATUS BADGE
# ==========================================================

def status_badge(status: str):

    badges = {
        "High Risk": "🔴 High Risk",
        "Medium Risk": "🟠 Medium Risk",
        "Low Risk": "🟢 Low Risk",
        "Healthy": "🟢 Healthy",
        "Critical": "🔴 Critical",
        "Warning": "🟠 Warning",
        "Info": "🔵 Information",
        "Success": "🟢 Success"
    }

    st.markdown(
        f"**{badges.get(status, status)}**"
    )


# ==========================================================
# BUSINESS ALERT
# ==========================================================

def business_alert(
    title: str,
    message: str,
    severity: str = "info"
):

    with st.container(border=True):

        st.markdown(f"### {title}")

        if severity.lower() == "success":
            st.success(message)

        elif severity.lower() == "warning":
            st.warning(message)

        elif severity.lower() == "danger":
            st.error(message)

        else:
            st.info(message)


# ==========================================================
# AI RECOMMENDATION
# ==========================================================

def ai_recommendation(
    recommendation: str
):

    with st.container(border=True):

        st.markdown("### 🤖 AI Recommendation")

        st.success(recommendation)


# ==========================================================
# NOTIFICATION ITEM
# ==========================================================

def notification_item(
    title: str,
    description: str,
    icon: str = "🔔"
):

    with st.container(border=True):

        st.markdown(f"#### {icon} {title}")

        st.write(description)


# ==========================================================
# ALERT TIMELINE
# ==========================================================

def alert_timeline(alerts):

    """
    alerts should be a list like:

    [
        {
            "title":"Inventory Risk",
            "message":"Electronics stock below reorder level.",
            "icon":"🔴"
        }
    ]
    """

    for alert in alerts:

        with st.container(border=True):

            st.markdown(
                f"#### {alert.get('icon','🔔')} {alert['title']}"
            )

            st.write(
                alert["message"]
            )


# ==========================================================
# NO ALERTS
# ==========================================================

def no_alerts():

    st.success(
        "🎉 No critical alerts at the moment."
    )


# ==========================================================
# OPERATIONAL HEALTH
# ==========================================================

def operational_health(
    healthy=True
):

    if healthy:

        st.success(
            "🟢 Overall Operational Health : Healthy"
        )

    else:

        st.error(
            "🔴 Operational issues require attention."
        )