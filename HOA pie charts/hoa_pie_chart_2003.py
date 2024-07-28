import pyecharts.options as opts
from pyecharts.charts import Pie
import webbrowser
import os
from pyecharts.commons.utils import JsCode

# Prepare data for the pie chart
expenses_2003 = {
    "Administrative Expense": 12433,
    "Professional Fees": 3313,
    "Insurance": 56341,
    "Management": 30418,
    "Landscaping, Grounds, and Drainage": 122745,
    "Supplies": 560,
    "Water": 2429,
    "Interest Expense": 11938,
    "Payroll and Related Expenses": 9973,
    "Electrical Repairs": 0,
    "Plumbing": 608,
    "Exterminator": 2987,
    "Speed Bumps": 0,
    "Cleaning": 4938,
    "Building Repairs": 5530,
    "Pool Expenses": 6064,
    "Alarm Monitoring": 996,
    "Utilities": 8565,
    "Telephone": 1318,
    "Licenses": 61,
    "Provision for State Income Taxes": 33
}

# Income and Net Profit (Loss) data
income_data = {
    "Interest Income": 144,
    "Other Income": 353,
    "Common Charges (Note 1)": 253417,
    "Total Revenues": 253914,
    "Total Expenses": 281250,
    "Net Profit (Loss)": 27336
}

# Create a list of tuples for the data
data = list(expenses_2003.items())

# Create a Pie chart with pyecharts
pie_chart = (
    Pie()
    .add(
        "",
        data,
        radius=["40%", "70%"],
        center=["60%", "60%"],  # Move the pie chart down
        label_opts=opts.LabelOpts(
            formatter=JsCode("function(params){return params.name + ': $' + params.value.toLocaleString();}"),
            position="outside"
        ),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Expenses Distribution for 2003",
            subtitle=(
                f"Income:\n"
                f"  Interest Income: ${income_data['Interest Income']:,}\n"
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
file_path = 'expenses_pie_chart_2003.html'
pie_chart.render(file_path)

# Get the absolute file path
absolute_file_path = os.path.abspath(file_path)

# Open the HTML file in the default web browser
webbrowser.open('file://' + absolute_file_path)