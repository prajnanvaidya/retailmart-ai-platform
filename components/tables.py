import streamlit as st
import pandas as pd


# ==========================================================
# STANDARD TABLE
# ==========================================================

def display_table(

    dataframe: pd.DataFrame,

    height: int = 450

):
    """
    Displays a responsive dataframe.
    """

    st.dataframe(

        dataframe,

        use_container_width=True,

        height=height,

        hide_index=True

    )


# ==========================================================
# INTERACTIVE TABLE
# ==========================================================

def interactive_table(

    dataframe: pd.DataFrame,

    height: int = 500

):
    """
    Displays an interactive dataframe with sorting,
    filtering and resizing.
    """

    st.dataframe(

        dataframe,

        use_container_width=True,

        height=height,

        hide_index=True

    )


# ==========================================================
# TOP RECORDS TABLE
# ==========================================================

def top_records(

    dataframe: pd.DataFrame,

    rows: int = 10,

    height: int = 350

):
    """
    Displays first N records.
    """

    st.dataframe(

        dataframe.head(rows),

        use_container_width=True,

        hide_index=True,

        height=height

    )


# ==========================================================
# DOWNLOAD TABLE
# ==========================================================

def downloadable_table(

    dataframe: pd.DataFrame,

    filename: str

):
    """
    Shows dataframe and download button.
    """

    st.dataframe(

        dataframe,

        use_container_width=True,

        hide_index=True

    )

    csv = dataframe.to_csv(

        index=False

    ).encode(

        "utf-8"

    )

    st.download_button(

        label="📥 Download CSV",

        data=csv,

        file_name=filename,

        mime="text/csv"

    )


# ==========================================================
# EMPTY TABLE
# ==========================================================

def empty_table(

    message="No records available."

):

    st.info(

        message

    )


# ==========================================================
# SEARCH RESULT TABLE
# ==========================================================

def search_table(

    dataframe: pd.DataFrame,

    keyword: str,

    column: str

):

    if keyword:

        dataframe = dataframe[

            dataframe[column]

            .astype(str)

            .str.contains(

                keyword,

                case=False,

                na=False

            )

        ]

    st.dataframe(

        dataframe,

        use_container_width=True,

        hide_index=True

    )