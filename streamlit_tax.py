import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Tax slabs data
data = {
    "Taxable Income": ["Up to Rs.2.5 lakh", "Greater than Rs.2.5 lakh to Rs.3 lakh", 
                       "Greater than Rs.3 lakh to Rs.5 lakh", "Greater than Rs.5 lakh to Rs.6 lakh",
                       "Greater than Rs.6 lakh to Rs. 9 lakh", "Greater than Rs.9 lakh to Rs.10 lakh",
                       "Greater than Rs.10 lakh to Rs.12 lakh", "Greater than Rs.12 lakh to Rs.15 lakh",
                       "Above Rs.15 lakh"],
    "Old Tax Regime": ["Exempted", "5%", "5%", "20%", "20%", "20%", "30%", "30%", "30%"],
    "New Tax Regime": ["Exempted", "Exempted", "5%", "5%", "10%", "15%", "15%", "20%", "30%"]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Function to convert percentage strings to numerical values
def convert_percentage(value):
    if value == "Exempted":
        return 0
    return int(value.strip('%'))

# Add numerical values for plotting
df['Old Tax Regime (numeric)'] = df['Old Tax Regime'].apply(convert_percentage)
df['New Tax Regime (numeric)'] = df['New Tax Regime'].apply(convert_percentage)

# Deductions not allowed under new tax regime
deductions_not_allowed = [
    "Leave Travel Allowance (LTA) for salaried employees",
    "House Rent Allowance (HRA)",
    "Children education allowance",
    "Helper allowance",
    "Interest on housing loan (Section 24)",
    "Other special allowances [Section 10(14)]",
    "Professional tax",
    "Donation to Political party/trust, etc."
]

# Deductions retained under new tax regime
deductions_retained = [
    "Retirement benefits, gratuity etc.",
    "Conveyance allowance for expenditure incurred for travelling for duties of an office",
    "Transport allowance for specially-abled people",
    "Education scholarships",
    "Retrenchment compensation",
    "Investment in Notified Pension Scheme under section 80CCD(2)",
    "Depreciation u/s 32 of the Income-tax act except additional depreciation"
]

# Function to calculate tax
def calculate_tax(income, standard_deduction, regime):
    taxable_income = income - standard_deduction
    slabs = []
    if regime == 'Old Tax Regime':
        slabs = [(250000, 0), (50000, 5), (200000, 5), (100000, 20), (300000, 20), (100000, 20), (200000, 30), (300000, 30), (float('inf'), 30)]
    else:
        slabs = [(250000, 0), (50000, 0), (200000, 5), (100000, 5), (300000, 10), (100000, 15), (200000, 15), (300000, 20), (float('inf'), 30)]
    
    tax = 0
    details = []
    for limit, rate in slabs:
        if taxable_income <= 0:
            break
        applicable_amount = min(taxable_income, limit)
        slab_tax = applicable_amount * rate / 100
        tax += slab_tax
        details.append((applicable_amount, rate, slab_tax))
        taxable_income -= applicable_amount
    
    return tax, details

# Streamlit app
st.title("Income Tax Slabs for FY 2023-24")

st.subheader("Tabular Representation")
st.dataframe(df)

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.35
index = range(len(df))

# Bar chart
bar1 = ax.bar(index, df['Old Tax Regime (numeric)'], bar_width, label='Old Tax Regime')
bar2 = ax.bar([i + bar_width for i in index], df['New Tax Regime (numeric)'], bar_width, label='New Tax Regime')

# Labels and titles
ax.set_xlabel('Taxable Income')
ax.set_ylabel('Tax Rate (%)')
ax.set_title('Comparison of Income Tax Rates: Old vs New Regime')
ax.set_xticks([i + bar_width / 2 for i in index])
ax.set_xticklabels(df['Taxable Income'], rotation=45, ha='right')
ax.legend()

# Display the plot
st.pyplot(fig)

st.subheader("Deductions Not Allowed Under the New Tax Regime")
st.write("\n".join(f"{i+1}. {item}" for i, item in enumerate(deductions_not_allowed)))

st.subheader("Deductions Retained Under the New Tax Regime")
st.write("\n".join(f"{i+1}. {item}" for i, item in enumerate(deductions_retained)))

# User input for tax calculation
st.subheader("Tax Calculation")
income = st.number_input("Enter your total income (in Rs.):", min_value=0, step=1000)
standard_deduction = st.number_input("Enter your standard deduction (in Rs.):", min_value=0, step=1000)
regime = st.selectbox("Select the tax regime:", ['Old Tax Regime', 'New Tax Regime'])

if st.button("Calculate Tax"):
    tax, details = calculate_tax(income, standard_deduction, regime)
    st.write(f"The calculated tax under the {regime} is Rs. {tax:.2f}")

    st.subheader("Tax Calculation Details")
    for i, (amount, rate, slab_tax) in enumerate(details):
        st.write(f"Slab {i+1}: Income - Rs. {amount}, Rate - {rate}%, Tax - Rs. {slab_tax:.2f}")
