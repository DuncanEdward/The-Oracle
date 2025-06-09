
# 🌌 Luna Lira: Finviz-Filtered IPO Analyzer

**Luna Lira** is a Streamlit-powered financial-astrology app that integrates IPO launch data and Finviz screener exports with planetary transit analysis using Swiss Ephemeris.

---

## 🚀 Features

### 📥 Data Upload
- Upload **IPO CSV** (must contain `Ticker` and `Date`)
- Upload **Finviz Export CSV** (must contain `Ticker`)
- Automatic ticker matching

### 🎯 Ticker Selection
- Choose from matched tickers for focused analysis

### 🔧 Aspect Configuration
- Customizable scores for aspects (Conjunction, Trine, etc.)
- Adjustable orbs (± degrees)
- Preloaded with recommended default settings

### 🪐 Astrology Engine
- Uses Swiss Ephemeris for planetary calculations
- Compares transit planets with:
  - IPO date planetary positions
  - Fixed NYSE natal positions

### 📅 Time Range Selection
- Set start/end date
- Choose time of day for accurate transit calculations

### 🔍 Score Filtering
- Filter aspects by minimum score value

### 📊 Visualization
- **Aspect tables** for IPO and NYSE alignments
- **Score heatmap** to identify high-impact days

---

## 🛠 Technologies

- `streamlit`
- `pandas`
- `swisseph`
- `matplotlib` / `seaborn`

---

## 🔮 Potential Use Cases

- Astro-financial research
- Energetic market timing
- Backtesting transit-based trading ideas

---

## 📦 Future Enhancements

- Export to CSV
- Auto-run analysis on upload
- Best ticker/day ranking
- Multi-day score trends

---

## 🧠 How to Run

```bash
pip install streamlit pandas swisseph matplotlib seaborn
streamlit run Mercury_5_cleaned_final.py
```

---

## 📂 File Structure

- `Mercury_5_cleaned_final.py` — Streamlit frontend
- `astro_analysis.py` — planetary and aspect computation backend

---

Happy Astro-Trading! 🌠
