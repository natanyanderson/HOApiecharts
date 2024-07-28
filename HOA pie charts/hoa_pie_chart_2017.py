import pyecharts.options as opts
from pyecharts.charts import Pie
import webbrowser
import os
from pyecharts.commons.utils import JsCode

# Prepare data for the pie chart
expenses_2017 = {
    "Administrative Expense": 4705,
    "Professional Fees": 2600,
    "Engineering": 300,
    "Insurance": 95220,
    "Management": 41813,
    "Landscaping, Grounds, and snow removal": 193471,
    "Water": 14040,
    "Interest Expense": 23282,
    "Electrical Repairs": 2256,
    "Plumbing": 1255,
    "Exterminator": 2692,
    "Exercise Equipment": 2003,
    "Cleaning": 5658,
    "Building Repairs": 9723,
    "Pool Expenses": 24432,
    "Gutters and leaders": 6900,
    "Fencing": 17306,
    "Alarm Monitoring and repairs": 114,
    "Utilities": 8224,
    "Telephone and cable": 2521,
    "Paving": 4724,
    "Drainage": 0,
    "Licenses": 315,
    "Provision for State Income Taxes": 640
}

# Income and Net Profit (Loss) data
income_data = {
    "Interest Income": 462,
    "Assessments": 65725,
    "Other Income": 332,
    "Common Charges (Note 1)": 509184,
    "Total Revenues": 575703,
    "Total Expenses": 464194,
    "Net Profit (Loss)": 111509
}

# Create a list of tuples for the data
data = list(expenses_2017.items())

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
            title="Expenses Distribution for 2017",
            subtitle=(
                f"Income:\n"
                f"  Interest Income: ${income_data['Interest Income']:,}\n"
                f"  Assessments: ${income_data['Assessments']:,}\n"
                f"  Other Income: ${income_data['Other Income']:,}\n"
                f"  Common Charges (Note 1): ${income_data['Common Charges (Note 1)']:,}\n"
                f"  Total Revenues: ${income_data['Total Revenues']:,}\n\n"
                f"Total Expenses: ${income_data['Total Expenses']:,}\n"
                f"Net Profit (Loss): ${income_data['Net Profit (Loss)']:,}"
            ),
            title_textstyle_opts=opts.TextStyleOpts(font_size=20, font_weight='bold'),
            subtitle_textstyle_opts=opts.TextStyleOpts(font_size=18, font_weight='bold')  # Increase subtitle size
        ),
        legend_opts=opts.LegendOpts(is_show=False)
    )
)

# Render the chart to a file
file_path = 'expenses_pie_chart_2017.html'
pie_chart.render(file_path)

# Get the absolute file path
absolute_file_path = os.path.abspath(file_path)

# Open the HTML file in the default web browser
webbrowser.open('file://' + absolute_file_path)