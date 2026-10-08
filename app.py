import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page config (must be first Streamlit call) ---
st.set_page_config(
    page_title="Dashboard App",
    page_icon="📊",
    layout="wide",
)

st.title("Dashboard App")
st.caption("Interactive category explorer")


# --- Cached data loader ---
@st.cache_data
def load_data() -> pd.DataFrame:
    return pd.DataFrame({
        "category": ["A", "B", "C", "D"],
        "values": [10, 20, 30, 40],
    })

data = load_data()

# --- Sidebar controls ---
with st.sidebar:
    st.header("Filters")
    categories = data["category"].unique().tolist()
    selected = st.multiselect(
        "Choose categories:",
        options=categories,
        default=categories,
    )
    show_all = st.checkbox("Show all in chart", value=True)

# --- Filter ---
filtered = data if show_all else data[data["category"].isin(selected)]

# --- Main layout in two columns ---
col_chart, col_stats = st.columns([3, 1])

with col_chart:
    if filtered.empty:
        st.warning("No data matches your selection.")
    else:
        fig = px.bar(
            filtered,
            x="category",
            y="values",
            title="My Chart",
            color="category",
        )
        fig.update_layout(showlegend=False, margin=dict(t=40, b=10))
        st.plotly_chart(fig, use_container_width=True)

with col_stats:
    total = int(filtered["values"].sum()) if not filtered.empty else 0
    avg = float(filtered["values"].mean()) if not filtered.empty else 0.0
    st.metric("Total", total)
    st.metric("Average", f"{avg:.1f}")

# --- Raw data expander ---
with st.expander("View raw data"):
    st.dataframe(filtered, use_container_width=True)