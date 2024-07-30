import pyecharts.options as opts
from pyecharts.charts import Pie
import webbrowser
import os
from pyecharts.commons.utils import JsCode

# Prepare data for the pie chart
expenses_2005 = {
    "Administrative Expense": 7517,
    "Professional Fees": 3393,
    "Insurance": 74282,
    "Management": 32591,
    "Landscaping, Grounds, and Drainage": 136659,
    "Supplies": 591,
    "Water": 4587,
    "Interest Expense": 9652,
    "Payroll and Related Expenses": 10182,
    "Electrical Repairs": 1924,
    "Plumbing": 972,
    "Exterminator": 3426,
    "Speed Bumps": 2635,
    "Cleaning": 7112,
    "Building Repairs": 2612,
    "Pool Expenses": 8736,
    "Gutters and leaders": 3277,
    "Alarm Monitoring and repairs": 5510,
    "Utilities": 9558,
    "Telephone": 1554,
    "Licenses": 250,
    "Provision for State Income Taxes": 31
}

# Income and Net Profit (Loss) data
income_data = {
    "Interest Income": 361,
    "Other Income": 672,
    "Assessments": 40800,
    "Common Charges (Note 1)": 358160,
    "Total Revenues": 399993,
    "Total Expenses": 337051,
    "Net Profit (Loss)": 72942
}

# Create a list of tuples for the data
data = list(expenses_2005.items())

# Create a Pie chart with pyecharts
pie_chart = (
    Pie()
    .add(
        "",
        data,
        radius=["40%", "70%"],
        center=["60%", "64%"],  # Move the pie chart down
        label_opts=opts.LabelOpts(
            formatter=JsCode("function(params){return params.name + ': $' + params.value.toLocaleString();}"),
            position="outside"
        ),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Expenses Distribution for 2005",
            subtitle=(
                f"Income:\n"
                f"  Interest Income: ${income_data['Interest Income']:,}\n"
                f"  Other Income: ${income_data['Other Income']:,}\n"
                f"  Assessments: ${income_data['Assessments']:,}\n"
                f"  Common Charges (Note 1): ${income_data['Common Charges (Note 1)']:,}\n"
                f"  Total Revenues: ${income_data['Total Revenues']:,}\n\n"
                f"Total Expenses: ${income_data['Total Expenses']:,}\n"
                f"Net Profit (Loss): ${income_data['Net Profit (Loss)']:,}"
            ),
            title_textstyle_opts=opts.TextStyleOpts(font_size=20, font_weight='bold'),
            subtitle_textstyle_opts=opts.TextStyleOpts(font_size=16, font_weight='bold')  # Increase subtitle size
        ),
        legend_opts=opts.LegendOpts(is_show=False)
    )
)

# Render the chart to a file
file_path = 'expenses_pie_chart_2005.html'
pie_chart.render(file_path)

# Get the absolute file path
absolute_file_path = os.path.abspath(file_path)

# Open the HTML file in the default web browser
webbrowser.open('file://' + absolute_file_path)