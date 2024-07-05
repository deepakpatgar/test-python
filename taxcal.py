from flask import Flask, render_template, request, jsonify
import pandas as pd
import plotly.express as px
import plotly.io as pio

app = Flask(__name__)

# Tax slab rates for FY 2024-25
tax_slabs = [
    (300000, 0.00),
    (600000, 0.05),
    (900000, 0.10),
    (1200000, 0.15),
    (1500000, 0.20),
    (float('inf'), 0.30)
]

def calculate_tax(income):
    tax = 0
    previous_slab_limit = 0
    effective_tax = []
    income_ranges = [300000, 600000, 900000, 1200000, 1500000, float('inf')]
    ranges_labels = ["Up to ₹3 lakhs", "₹3 lakhs to ₹6 lakhs", "₹6 lakhs to ₹9 lakhs", 
                     "₹9 lakhs to ₹12 lakhs", "₹12 lakhs to ₹15 lakhs", "Above ₹15 lakhs"]

    for i in range(len(tax_slabs)):
        slab_limit, rate = tax_slabs[i]
        if income > slab_limit:
            taxable_income = slab_limit - previous_slab_limit
            tax += taxable_income * rate
            effective_tax.append((ranges_labels[i], rate * 100, taxable_income * rate))
            previous_slab_limit = slab_limit
        else:
            taxable_income = income - previous_slab_limit
            tax += taxable_income * rate
            effective_tax.append((ranges_labels[i], rate * 100, taxable_income * rate))
            return tax, effective_tax

    # Handle income above the last slab
    if income > tax_slabs[-1][0]:
        taxable_income = income - tax_slabs[-1][0]
        tax += taxable_income * tax_slabs[-1][1]
        effective_tax.append((ranges_labels[-1], tax_slabs[-1][1] * 100, taxable_income * tax_slabs[-1][1]))

    return tax, effective_tax

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            data = request.get_json()
            income = float(data['income'])
            std_deduction = float(data.get('std_deduction', 50000))
            nps_contribution = float(data.get('nps_contribution', 50000))
            
            # Adjust income based on standard deduction and NPS contribution
            adjusted_income = income - std_deduction - nps_contribution
            tax, effective_tax = calculate_tax(adjusted_income)

            tax_summary = [{"range": range_label, "rate": rate, "effectiveTax": f"₹{tax:.2f}"} for range_label, rate, tax in effective_tax]
            total_tax = sum(tax for _, _, tax in effective_tax)
            effective_tax_rate = (total_tax / adjusted_income) * 100 if adjusted_income > 0 else 0

            return jsonify(
                taxSummary=tax_summary,
                totalTax=total_tax,
                effectiveTaxRate=effective_tax_rate,
                adjustedIncome=adjusted_income
            )
        except (ValueError, KeyError) as e:
            return jsonify(error="Invalid input amount"), 400
    return render_template('taxcal.html')

@app.route('/visualize', methods=['POST'])
def visualize():
    try:
        data = request.get_json()
        income = float(data['income'])
        std_deduction = float(data.get('std_deduction', 50000))
        nps_contribution = float(data.get('nps_contribution', 50000))
        adjusted_income = income - std_deduction - nps_contribution
        tax, effective_tax = calculate_tax(adjusted_income)
        
        # Data for visualization
        income_ranges = [300000, 600000, 900000, 1200000, 1500000, float('inf')]
        ranges_labels = ["Up to ₹3 lakhs", "₹3 lakhs to ₹6 lakhs", "₹6 lakhs to ₹9 lakhs", 
                         "₹9 lakhs to ₹12 lakhs", "₹12 lakhs to ₹15 lakhs", "Above ₹15 lakhs"]
        rates = [0, 0.05, 0.10, 0.15, 0.20, 0.30]
        
        remaining_income = adjusted_income
        effective_tax = []
        for i, slab in enumerate(income_ranges):
            if remaining_income > 0:
                if remaining_income >= slab:
                    effective_tax.append(slab * rates[i])
                    remaining_income -= slab
                else:
                    effective_tax.append(remaining_income * rates[i])
                    remaining_income = 0
            else:
                effective_tax.append(0)

        data = {
            "Income Range": ranges_labels,
            "Tax Rate": [rate * 100 for rate in rates],
            "Effective Tax": effective_tax
        }
        
        df = pd.DataFrame(data)
        fig = px.bar(df, x="Income Range", y="Effective Tax", title="Effective Tax per Income Range", labels={"Effective Tax": "Tax Amount in ₹"})
        graphJSON = pio.to_json(fig)
        
        # Effective Tax Rate Visualization
        total_effective_tax = sum(effective_tax)
        effective_tax_rate = (total_effective_tax / adjusted_income) * 100 if adjusted_income > 0 else 0
        effective_tax_rate_data = {
            "Effective Tax Rate (%)": [effective_tax_rate]
        }
        df_rate = pd.DataFrame(effective_tax_rate_data)
        fig_rate = px.bar(df_rate, y="Effective Tax Rate (%)", title="Effective Tax Rate", labels={"Effective Tax Rate (%)": "Effective Tax Rate (%)"})
        graphJSON_rate = pio.to_json(fig_rate)
        
        # Deductions Impact Visualization
        deduction_data = {
            "Type": ["Income", "Standard Deduction", "NPS Contribution", "Taxable Income"],
            "Amount (₹)": [income, -std_deduction, -nps_contribution, adjusted_income]
        }
        df_deductions = pd.DataFrame(deduction_data)
        fig_deductions = px.bar(df_deductions, x="Type", y="Amount (₹)", title="Impact of Deductions", labels={"Amount (₹)": "Amount in ₹"})
        graphJSON_deductions = pio.to_json(fig_deductions)
        
        return jsonify(graphJSON=graphJSON, graphJSON_rate=graphJSON_rate, graphJSON_deductions=graphJSON_deductions)
    except (ValueError, KeyError) as e:
        return jsonify(error="Invalid input amount"), 400


@app.route('/history', methods=['POST'])
def history():
    try:
        data = request.get_json()
        years = ["FY 2022-23", "FY 2023-24"]
        incomes = data['incomes']
        taxes = data['taxes']
        refunds = data['refunds']
        
        df = pd.DataFrame({
            "Year": years,
            "Income": incomes,
            "Tax Deducted": taxes,
            "Refund": refunds
        })
        
        fig1 = px.bar(df, x="Year", y="Income", title="Income over the Years", labels={"Income": "Income in ₹"})
        fig2 = px.bar(df, x="Year", y="Tax Deducted", title="Tax Deducted over the Years", labels={"Tax Deducted": "Tax Deducted in ₹"})
        fig3 = px.bar(df, x="Year", y="Refund", title="Refund over the Years", labels={"Refund": "Refund in ₹"})
        
        graphs = [pio.to_json(fig1), pio.to_json(fig2), pio.to_json(fig3)]
        
        return jsonify(graphs=graphs)
    except (ValueError, KeyError) as e:
        return jsonify(error="Invalid input data"), 400

if __name__ == '__main__':
    app.run(debug=True)
