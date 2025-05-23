import streamlit as st
import pandas as pd

# --- Calculator logic ---
def calculate_revenue_impact(
    total_orders: int,
    error_rate: float,
    aov: float,
    contact_rate: float,
    cost_per_contact: float,
    reshipment_rate: float,
    timeframe: str = "N/A"
) -> pd.DataFrame:
    
    errored_orders = total_orders * error_rate
    contacts = errored_orders * contact_rate
    reshipments = errored_orders * reshipment_rate
    
    contact_cost = contacts * cost_per_contact
    reshipment_cost = reshipments * aov * 2
    
    total_impact = contact_cost + reshipment_cost

    return pd.DataFrame([{
        "Timeframe": timeframe,
        "Total Orders": total_orders,
        "Errored Orders": errored_orders,
        "Customer Contacts": contacts,
        "Reshipments": reshipments,
        "Contact Cost (£)": contact_cost,
        "Reshipment Cost (£)": reshipment_cost,
        "Total Cost Impact (£)": total_impact
    }])

# --- Streamlit UI ---
st.title("📦 Wrong dose calculator")

timeframe = st.text_input("Timeframe", value="April 2025")
total_orders = st.number_input("Total Orders", value=46000, step=100)
error_rate = st.number_input(
    "Error Rate (e.g. 0.0028 = 0.28%)",
    min_value=0.0,
    max_value=1.0,
    value=0.0028,
    step=0.0001,
    format="%.4f"
)
st.write(f"Using error rate: {error_rate:.4%}")
aov = st.number_input("Average Order Value (£)", value=120.0, step=1.0)
contact_rate = st.slider("Contact Rate (% of errored orders)", 0.0, 1.0, 0.7)
cost_per_contact = st.number_input("Cost per Contact (£)", value=2.0)
reshipment_rate = st.slider("Reshipment Rate (% of errored orders)", 0.0, 1.0, 0.4)

if st.button("Calculate Impact"):
    df = calculate_revenue_impact(
        total_orders,
        error_rate,
        aov,
        contact_rate,
        cost_per_contact,
        reshipment_rate,
        timeframe
    )
    st.success("📊 Revenue Impact Calculated:")
    st.dataframe(df)
    annualised_cost = df["Total Cost Impact (£)"].iloc[0] * 12
    st.markdown(f"### 🧮 Estimated annual cost: £{annualised_cost:,.2f}")
