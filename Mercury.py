
import streamlit as st
import pandas as pd
from datetime import datetime, time
from astro_analysis import (
    parse_uploaded_files,
    filter_matching_tickers,
    get_user_aspect_config,
    calculate_aspects_for_ticker,
    render_aspect_table,
    render_aspect_heatmap
)

st.title("🌌 Luna Lira: Finviz-Filtered IPO Analyzer")

st.markdown("Upload your IPO and Finviz files to begin.")

ipo_file = st.file_uploader("📥 Upload IPO CSV File", type=["csv"])
finviz_file = st.file_uploader("📥 Upload Finviz Export CSV", type=["csv"])

if ipo_file and finviz_file:
    ipo_df, finviz_df = parse_uploaded_files(ipo_file, finviz_file)
    st.success("✅ IPO File Sample:")
    st.write(ipo_df.head())
    st.success("✅ Finviz File Sample:")
    st.write(finviz_df.head())

    matched_df = filter_matching_tickers(ipo_df, finviz_df)
    st.success("✅ Matching IPOs with Finviz tickers:")
    st.write(matched_df)

    ticker_options = matched_df["Ticker"].unique().tolist()
    selected_tickers = st.multiselect("🎯 Select tickers to analyze", ticker_options)

    with st.sidebar:
        start_date = st.date_input("📅 Start date", datetime.today())
        end_date = st.date_input("📅 End date", datetime.today())
        time_of_day = st.time_input("⏰ Time of day", time(10, 0))

    st.subheader("🔧 Aspect Configuration")
    aspect_scores = {}
    aspect_orbs = {}

    aspect_types = ['Conjunction', 'Opposition', 'Trine', 'Sextile', 'Square',
                    'Quincunx', 'Semisextile', 'Semisquare', 'Sesquisquare']

    default_scores = {
        'Conjunction': 5, 'Opposition': -5, 'Trine': 3, 'Sextile': 2,
        'Square': -3, 'Quincunx': -1, 'Semisextile': 1,
        'Semisquare': -1, 'Sesquisquare': -1
    }

    default_orbs = {
        'Conjunction': 5, 'Opposition': 5, 'Trine': 3, 'Sextile': 3,
        'Square': 3, 'Quincunx': 2, 'Semisextile': 2,
        'Semisquare': 2, 'Sesquisquare': 2
    }

    for aspect in aspect_types:
        aspect_scores[aspect] = st.slider(
            f"{aspect} Score", -5, 5, default_scores[aspect]
        )

    for aspect in aspect_types:
        aspect_orbs[aspect] = st.slider(
            f"{aspect} Orb ±°", 1, 10, default_orbs[aspect]
        )

    aspect_config = get_user_aspect_config(aspect_orbs, aspect_scores)

    min_score = st.slider("🔍 Filters: Minimum Aspect Score", -5, 5, 1)

    if st.button("🔮 Run Analysis"):
        for ticker in selected_tickers:
            st.markdown(f"### 🔮 Aspect Analysis for {ticker}")
            try:
                result_df = calculate_aspects_for_ticker(
                    ticker, matched_df, start_date, end_date, time_of_day, aspect_config
                )
                result_df = result_df[result_df["Score"] >= min_score]
                ipo_aspects = result_df[result_df["Source"] == "IPO"]
                nyse_aspects = result_df[result_df["Source"] == "NYSE"]

                st.markdown("#### IPO Aspects")
                render_aspect_table(ipo_aspects)
                st.markdown("#### NYSE Aspects")
                render_aspect_table(nyse_aspects)

                st.markdown("#### 📈 Aspect Score Summary")
                render_aspect_heatmap(result_df)
            except Exception as e:
                st.error(f"Error analyzing {ticker}: {e}")
