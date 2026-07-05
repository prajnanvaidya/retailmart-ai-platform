import pandas as pd


def format_currency(value):

    if value is None or pd.isna(value):
        return "₹0"

    value = float(value)

    if value >= 10000000:
        return f"₹{value/10000000:.2f} Cr"

    if value >= 100000:
        return f"₹{value/100000:.2f} L"

    return f"₹{value:,.2f}"


def format_number(value):

    if value is None or pd.isna(value):
        return "0"

    return f"{int(value):,}"


def format_percentage(value):

    if value is None or pd.isna(value):
        return "0%"

    return f"{value:.2f}%"


def get_status_color(status):

    colors = {

        "High Risk": "🔴",

        "Medium Risk": "🟠",

        "Low Risk": "🟢"

    }

    return colors.get(status, "⚪")