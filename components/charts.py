import streamlit as st
import plotly.express as px


# ==========================================================
# BAR CHART
# ==========================================================

def bar_chart(

    dataframe,

    x,

    y,

    title,

    color=None,

    horizontal=False

):

    if horizontal:

        fig = px.bar(

            dataframe,

            x=y,

            y=x,

            color=color,

            orientation="h",

            title=title

        )

    else:

        fig = px.bar(

            dataframe,

            x=x,

            y=y,

            color=color,

            title=title

        )

    fig.update_layout(

        height=420,

        margin=dict(

            l=20,

            r=20,

            t=60,

            b=20

        )

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )


# ==========================================================
# LINE CHART
# ==========================================================

def line_chart(

    dataframe,

    x,

    y,

    title,

    color=None,

    markers=True

):

    fig = px.line(

        dataframe,

        x=x,

        y=y,

        color=color,

        markers=markers,

        title=title

    )

    fig.update_layout(

        height=420

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )


# ==========================================================
# PIE CHART
# ==========================================================

def pie_chart(

    dataframe,

    names,

    values,

    title

):

    fig = px.pie(

        dataframe,

        names=names,

        values=values,

        title=title,

        hole=0.45

    )

    fig.update_layout(

        height=420

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )


# ==========================================================
# SCATTER CHART
# ==========================================================

def scatter_chart(

    dataframe,

    x,

    y,

    title,

    color=None,

    size=None,

    hover_name=None

):

    fig = px.scatter(

        dataframe,

        x=x,

        y=y,

        color=color,

        size=size,

        hover_name=hover_name,

        title=title

    )

    fig.update_layout(

        height=420

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )


# ==========================================================
# BOX PLOT
# ==========================================================

def box_plot(

    dataframe,

    x,

    y,

    title,

    color=None

):

    fig = px.box(

        dataframe,

        x=x,

        y=y,

        color=color,

        title=title

    )

    fig.update_layout(

        height=420

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )


# ==========================================================
# HISTOGRAM
# ==========================================================

def histogram(

    dataframe,

    x,

    title,

    color=None

):

    fig = px.histogram(

        dataframe,

        x=x,

        color=color,

        title=title

    )

    fig.update_layout(

        height=420

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )


# ==========================================================
# DATA TABLE
# ==========================================================

def data_table(

    dataframe,

    height=450

):

    st.dataframe(

        dataframe,

        use_container_width=True,

        height=height

    )