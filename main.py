from calculator import calculate_revenue_impact

df = calculate_revenue_impact(
    total_orders=10000,
    error_rate=0.05,
    aov=50,
    contact_rate=0.7,
    cost_per_contact=5,
    reshipment_rate=0.4,
    timeframe="April 2025"
)

print(df.to_string(index=False))
