import pandas as pd


def format_currency(value):

    if pd.isna(value):
        return "₹0"

    if value >= 10000000:
        return f"₹{value/10000000:.2f} Cr"

    if value >= 100000:
        return f"₹{value/100000:.2f} L"

    return f"₹{value:,.2f}"


def format_number(value):

    return f"{value:,}"