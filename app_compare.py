import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="AI Brand Comparison", layout="centered")

st.title("🏷️ AI-Based Brand Comparison Dashboard")

# ----------- DATA -----------
def get_brand_data(brand):
    data = {
        "nike": [
            {"name": "Nike Air Max", "price": 120, "rating": 4.5},
            {"name": "Nike Revolution", "price": 80, "rating": 4.2},
            {"name": "Nike Pegasus", "price": 150, "rating": 4.7}
        ],
        "puma": [
            {"name": "Puma RS-X", "price": 90, "rating": 4.1},
            {"name": "Puma Flyer", "price": 70, "rating": 4.0},
            {"name": "Puma Velocity", "price": 110, "rating": 4.3}
        ],
        "adidas": [
            {"name": "Adidas Ultraboost", "price": 140, "rating": 4.6},
            {"name": "Adidas Runfalcon", "price": 75, "rating": 4.1},
            {"name": "Adidas Duramo", "price": 95, "rating": 4.2}
        ]
    }
    return data.get(brand.lower(), [])

# ----------- ANALYSIS -----------
def analyze(data):
    if not data:
        return 0, 0

    prices = [item["price"] for item in data]
    ratings = [item["rating"] for item in data]

    avg_price = sum(prices) / len(prices)
    avg_rating = sum(ratings) / len(ratings)

    return avg_price, avg_rating

# ----------- AI COMPARISON -----------
def ai_compare(p1, r1, p2, r2, b1, b2):
    if r1 > r2 and p1 <= p2:
        return f"{b1.upper()} offers better value for money."
    elif r2 > r1 and p2 <= p1:
        return f"{b2.upper()} offers better value for money."
    elif r1 > r2:
        return f"{b1.upper()} has better quality but is more expensive."
    elif r2 > r1:
        return f"{b2.upper()} is more affordable but slightly lower in rating."
    else:
        return "Both brands offer similar value."

# ----------- USER INPUT -----------
st.subheader("🔍 Select Brands")

brand1 = st.selectbox("Select Brand 1", ["nike", "puma", "adidas"])
brand2 = st.selectbox("Select Brand 2", ["nike", "puma", "adidas"], index=1)

# ----------- BUTTON -----------
if st.button("Compare Brands"):

    data1 = get_brand_data(brand1)
    data2 = get_brand_data(brand2)

    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)

    # 📊 TABLES
    st.subheader(f"📊 {brand1.upper()} Data")
    st.dataframe(df1, use_container_width=True)

    st.subheader(f"📊 {brand2.upper()} Data")
    st.dataframe(df2, use_container_width=True)

    # 📈 ANALYSIS
    p1, r1 = analyze(data1)
    p2, r2 = analyze(data2)

    st.subheader("📈 Comparison Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(f"{brand1.upper()} Avg Price", f"${p1:.2f}")
        st.metric(f"{brand1.upper()} Avg Rating", f"{r1:.2f}")

    with col2:
        st.metric(f"{brand2.upper()} Avg Price", f"${p2:.2f}")
        st.metric(f"{brand2.upper()} Avg Rating", f"{r2:.2f}")

    # 🍩 DONUT CHART (PRICE)
    st.subheader("💰 Price Distribution")

    price_df = pd.DataFrame({
        "Brand": [brand1.upper(), brand2.upper()],
        "Avg Price": [p1, p2]
    })

    fig_price = px.pie(
        price_df,
        names="Brand",
        values="Avg Price",
        hole=0.5,
        color_discrete_sequence=px.colors.sequential.RdBu
    )

    st.plotly_chart(fig_price, use_container_width=True)

    # ⭐ RADAR CHART
    st.subheader("📊 Overall Performance")

    fig_radar = go.Figure()

    fig_radar.add_trace(go.Scatterpolar(
        r=[p1, r1],
        theta=["Price", "Rating"],
        fill='toself',
        name=brand1.upper()
    ))

    fig_radar.add_trace(go.Scatterpolar(
        r=[p2, r2],
        theta=["Price", "Rating"],
        fill='toself',
        name=brand2.upper()
    ))

    fig_radar.update_layout(
        polar=dict(radialaxis=dict(visible=True)),
        showlegend=True
    )

    st.plotly_chart(fig_radar, use_container_width=True)

    # 📈 LINE CHART
    st.subheader("📈 Comparison Trend")

    line_df = pd.DataFrame({
        "Metric": ["Price", "Rating"],
        brand1.upper(): [p1, r1],
        brand2.upper(): [p2, r2]
    })

    fig_line = px.line(
        line_df,
        x="Metric",
        y=[brand1.upper(), brand2.upper()],
        markers=True
    )

    st.plotly_chart(fig_line, use_container_width=True)

    # 🏆 AI VERDICT
    st.subheader("🏆 AI Comparison Verdict")

    result = ai_compare(p1, r1, p2, r2, brand1, brand2)
    st.success(result)