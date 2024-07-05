from flask import Flask, render_template, request, jsonify
import pandas as pd
import plotly.express as px
import plotly.io as pio

app = Flask(__name__)

# Tax slab rates for Old Regime
old_tax_slabs = [
    (250000, 0.00),
    (500000, 0.05),
    (1000000, 0.20),
    (float('inf'), 0.30)
]

# Tax slab rates for New Regime (Before Budget 2023)
new_tax_slabs_before_2023 = [
    (250000, 0.00),
    (500000, 0.05),
    (750000, 0.10),
    (1000000, 0.15),
    (1250000, 0.20),
    (1500000, 0.25),
    (float('inf'), 0.30)
]

# Tax slab rates for New Regime (After Budget 2023)
new_tax_slabs_after_2023 = [
    (300000, 0.00),
    (600000, 0.05),
    (900000, 0.10),
    (1200000, 0.15),
    (1500000, 0.20),
    (float('inf'), 0.30)
]

def calculate_tax(income, tax_slabs):
    tax = 0
    previous_slab_limit = 0
    effective_tax = []
    for slab_limit, rate in tax_slabs:
        if income > slab_limit:
            taxable_income = slab_limit - previous_slab_limit
            tax += taxable_income * rate
            effective_tax.append((slab_limit, rate * 100, taxable_income * rate))
            previous_slab_limit = slab_limit
        else:
            taxable_income = income - previous_slab_limit
            tax += taxable_income * rate
            effective_tax.append((income, rate * 100, taxable_income * rate))
            break
    return tax, effective_tax

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            data = request.get_json()
            income = float(data['income'])
            std_deduction = float(data.get('std_deduction', 50000))
            nps_contribution = float(data.get('nps_contribution', 50000))
            regime = data.get('regime', 'new_after_2023')  # default to new regime after 2023

            # Select tax slabs based on regime
            if regime == 'old':
                tax_slabs = old_tax_slabs
            elif regime == 'new_before_2023':
                tax_slabs = new_tax_slabs_before_2023
            else:
                tax_slabs = new_tax_slabs_after_2023

            # Adjust income based on standard deduction and NPS contribution
            adjusted_income = income - std_deduction - nps_contribution
            tax, effective_tax = calculate_tax(adjusted_income, tax_slabs)

            tax_summary = [{"range": f"Up to ₹{slab}", "rate": rate, "effectiveTax": f"₹{tax:.2f}"} for slab, rate, tax in effective_tax]
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
    return render_template('newtaxcal.html')

@app.route('/visualize', methods=['POST'])
def visualize():
    try:
        data = request.get_json()
        income = float(data['income'])
        std_deduction = float(data.get('std_deduction', 50000))
        nps_contribution = float(data.get('nps_contribution', 50000))
        regime = data.get('regime', 'new_after_2023')  # default to new regime after 2023

        # Select tax slabs based on regime
        if regime == 'old':
            tax_slabs = old_tax_slabs
            ranges_labels = ["Up to ₹2.5 lakhs", "₹2.5 lakhs to ₹5 lakhs", "₹5 lakhs to ₹10 lakhs", "Above ₹10 lakhs"]
        elif regime == 'new_before_2023':
            tax_slabs = new_tax_slabs_before_2023
            ranges_labels = ["Up to ₹2.5 lakhs", "₹2.5 lakhs to ₹5 lakhs", "₹5 lakhs to ₹7.5 lakhs", 
                             "₹7.5 lakhs to ₹10 lakhs", "₹10 lakhs to ₹12.5 lakhs", "₹12.5 lakhs to ₹15 lakhs", "Above ₹15 lakhs"]
        else:
            tax_slabs = new_tax_slabs_after_2023
            ranges_labels = ["Up to ₹3 lakhs", "₹3 lakhs to ₹6 lakhs", "₹6 lakhs to ₹9 lakhs", 
                             "₹9 lakhs to ₹12 lakhs", "₹12 lakhs to ₹15 lakhs", "Above ₹15 lakhs"]

        adjusted_income = income - std_deduction - nps_contribution
        tax, effective_tax = calculate_tax(adjusted_income, tax_slabs)

        data = {
            "Income Range": ranges_labels,
            "Tax Rate": [rate for _, rate, _ in effective_tax],
            "Effective Tax": [tax for _, _, tax in effective_tax]
        }

        df = pd.DataFrame(data)
        fig = px.bar(df, x="Income Range", y="Effective Tax", title="Effective Tax per Income Range", labels={"Effective Tax": "Tax Amount in ₹"})
        graphJSON = pio.to_json(fig)

        # Effective Tax Rate Visualization
        total_effective_tax = sum([tax for _, _, tax in effective_tax])
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
