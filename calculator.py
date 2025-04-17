import pandas as pd

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
    reshipment_cost = reshipments * aov * 2  # Double cost due to reshipment
    
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
