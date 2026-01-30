import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Simulation Parameters based on Article Context (Year 2026)
traffic = 10000  # Monthly high-intent users visiting the trade-in page
aov = 1800       # Average Order Value for a high-performance laptop
baseline_cr = 0.04  # 4% conversion rate if the page worked perfectly
friction_cr = 0.005 # 0.5% conversion rate with the current friction (only 1 in 200 persistent users)
months = 12

# 1. Monthly Revenue Calculation
potential_monthly_rev = traffic * baseline_cr * aov
actual_monthly_rev = traffic * friction_cr * aov
monthly_loss = potential_monthly_rev - actual_monthly_rev

# 2. Yearly Impact
yearly_loss = monthly_loss * months

# 3. Create a DataFrame for different traffic scenarios
scenarios = np.linspace(5000, 20000, 4)
data = []
for t in scenarios:
    p_rev = t * baseline_cr * aov
    a_rev = t * friction_cr * aov
    loss = p_rev - a_rev
    data.append({'Monthly Traffic': int(t), 'Potential Revenue ($)': p_rev, 'Actual Revenue ($)': a_rev, 'Revenue Leakage ($)': loss})

df_scenarios = pd.DataFrame(data)

# 4. Visualization: Revenue Leakage Waterfall/Bar Chart
labels = ['Potential Revenue', 'Actual Revenue', 'Revenue Leakage']
values = [potential_monthly_rev, actual_monthly_rev, monthly_loss]
colors = ['#2ecc71', '#e74c3c', '#3498db']

plt.figure(figsize=(10, 6))
bars = plt.bar(labels, values, color=colors)
plt.title('Monthly Financial Impact of "Empty Trade-In Page" (Estimated)', fontsize=14)
plt.ylabel('Amount in USD ($)', fontsize=12)

# Adding value labels on top of bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 10000, f'${yval:,.0f}', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('revenue_leakage_analysis.png')

# 5. Customer Lifetime Value (CLV) Loss Simulation
clv_multiplier = 2.5 # Assuming a customer buys 2.5 devices over their lifetime
yearly_clv_loss = (traffic * (baseline_cr - friction_cr) * months) * (aov * clv_multiplier)

print(f"Monthly Revenue Leakage: ${monthly_loss:,.2f}")
print(f"Annual Revenue Leakage: ${yearly_loss:,.2f}")
print(f"Estimated Annual CLV Loss: ${yearly_clv_loss:,.2f}")
print(df_scenarios)
