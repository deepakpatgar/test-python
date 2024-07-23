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

# Tax slab rates for New Regime (FY 2024-25)
new_tax_slabs_2024_25 = [
    (300000, 0.00),
    (700000, 0.05),
    (1000000, 0.10),
    (1200000, 0.15),
    (1500000, 0.20),
    (float('inf'), 0.30)
]

def calculate_tax(income, std_deduction, nps_contribution, regime):
    adjusted_income = income - std_deduction - nps_contribution

    if regime == 'old':
        tax_slabs = old_tax_slabs
    elif regime == 'new_before_2023':
        tax_slabs = new_tax_slabs_before_2023
    elif regime == 'new_after_2023':
        tax_slabs = new_tax_slabs_after_2023
    elif regime == 'new_2024_25':
        tax_slabs = new_tax_slabs_2024_25
    else:
        return {'error': 'Invalid tax regime selected'}

    total_tax = 0
    remaining_income = adjusted_income
    tax_summary = []

    for slab_limit, slab_rate in tax_slabs:
        if remaining_income <= 0:
            break
        taxable_amount = min(slab_limit, remaining_income)
        tax = taxable_amount * slab_rate
        tax_summary.append({
            'range': f"Up to ₹{slab_limit}",
            'rate': slab_rate * 100,
            'effectiveTax': tax
        })
        total_tax += tax
        remaining_income -= taxable_amount

    effective_tax_rate = (total_tax / adjusted_income) * 100 if adjusted_income > 0 else 0

    return {
        'adjustedIncome': adjusted_income,
        'totalTax': total_tax,
        'effectiveTaxRate': effective_tax_rate,
        'taxSummary': tax_summary
    }

@app.route('/')
def index():
    return render_template('newtaxcal2425.html')

@app.route('/', methods=['POST'])
def calculate():
    data = request.json
    income = data.get('income')
    std_deduction = data.get('std_deduction')
    nps_contribution = data.get('nps_contribution')
    regime = data.get('regime')

    if None in (income, std_deduction, nps_contribution, regime):
        return jsonify({'error': 'All fields are required'})

    tax_data = calculate_tax(income, std_deduction, nps_contribution, regime)
    return jsonify(tax_data)

@app.route('/visualize', methods=['POST'])
def visualize():
    data = request.json
    income = data.get('income')
    std_deduction = data.get('std_deduction')
    nps_contribution = data.get('nps_contribution')
    regime = data.get('regime')

    tax_data = calculate_tax(income, std_deduction, nps_contribution, regime)
    tax_summary = tax_data['taxSummary']

    tax_ranges = [item['range'] for item in tax_summary]
    tax_amounts = [item['effectiveTax'] for item in tax_summary]

    fig = px.bar(x=tax_ranges, y=tax_amounts, labels={'x': 'Income Range', 'y': 'Tax Amount'},
                 title='Tax Breakdown by Income Range')
    graphJSON = pio.to_json(fig)

    effective_tax_rates = [item['rate'] for item in tax_summary]
    fig_rate = px.pie(values=effective_tax_rates, names=tax_ranges, title='Effective Tax Rates')
    graphJSON_rate = pio.to_json(fig_rate)

    deductions = {
        'Standard Deduction': std_deduction,
        'NPS Contribution': nps_contribution
    }
    fig_deductions = px.pie(values=list(deductions.values()), names=list(deductions.keys()), title='Deductions Breakdown')
    graphJSON_deductions = pio.to_json(fig_deductions)

    return jsonify({
        'graphJSON': graphJSON,
        'graphJSON_rate': graphJSON_rate,
        'graphJSON_deductions': graphJSON_deductions
    })

if __name__ == '__main__':
    app.run(debug=True)
