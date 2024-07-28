import pyecharts.options as opts
from pyecharts.charts import Pie
import webbrowser
import os
from pyecharts.commons.utils import JsCode

# Prepare data for the pie chart
expenses_2016 = {
    "Administrative Expense": 3848,
    "Professional Fees": 2800,
    "Engineering": 4600,
    "Insurance": 91918,
    "Management": 40993,
    "Landscaping, Grounds, and snow removal": 185248,
    "Water": 13084,
    "Interest Expense": 26167,
    "Electrical Repairs": 5074,
    "Plumbing": 1827,
    "Exterminator": 3417,
    "Exercise Equipment": 1288,
    "Cleaning": 6013,
    "Building Repairs": 8643,
    "Pool Expenses": 24764,
    "Gutters and leaders": 6900,
    "Sprinklers": 0,
    "Fencing": 9105,
    "Pool resurfacing": 0,
    "Alarm Monitoring and repairs": 103,
    "Utilities": 8170,
    "Telephone and cable": 2386,
    "Paving": 4778,
    "Drainage": 5340,
    "Licenses": 315,
    "Provision for State Income Taxes": 628
}

# Income and Net Profit (Loss) data
income_data = {
    "Interest Income": 476,
    "Assessments": 57400,
    "Expense reimbursement": 0,
    "Other Income": 104,
    "Common Charges (Note 1)": 491504,
    "Total Revenues": 549484,
    "Total Expenses": 457409,
    "Net Profit (Loss)": 92075
}

# Create a list of tuples for the data
data = list(expenses_2016.items())

# Create a Pie chart with pyecharts
pie_chart = (
    Pie()
    .add(
        "",
        data,
        radius=["40%", "60%"],
        center=["52%", "70%"],  # Move the pie chart down
        label_opts=opts.LabelOpts(
            formatter=JsCode("function(params){return params.name + ': $' + params.value.toLocaleString();}"),
            position="outside"
        ),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Expenses Distribution for 2016",
            subtitle=(
                f"Income:\n"
                f"  Interest Income: ${income_data['Interest Income']:,}\n"
                f"  Assessments: ${income_data['Assessments']:,}\n"
                f"  Expense reimbursement: ${income_data['Expense reimbursement']:,}\n"
                f"  Other Income: ${income_data['Other Income']:,}\n"
                f"  Common Charges (Note 1): ${income_data['Common Charges (Note 1)']:,}\n"
                f"  Total Revenues: ${income_data['Total Revenues']:,}\n\n"
                f"Total Expenses: ${income_data['Total Expenses']:,}\n"
                f"Net Profit (Loss): ${income_data['Net Profit (Loss)']:,}"
            ),
            title_textstyle_opts=opts.TextStyleOpts(font_size=20, font_weight='bold'),
            subtitle_textstyle_opts=opts.TextStyleOpts(font_size=17, font_weight='bold')  # Increase subtitle size
        ),
        legend_opts=opts.LegendOpts(is_show=False)
    )
)

# Render the chart to a file
file_path = 'expenses_pie_chart_2016.html'
pie_chart.render(file_path)

# Get the absolute file path
absolute_file_path = os.path.abspath(file_path)

# Open the HTML file in the default web browser
webbrowser.open('file://' + absolute_file_path)