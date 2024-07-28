import pyecharts.options as opts
from pyecharts.charts import Pie
import webbrowser
import os
from pyecharts.commons.utils import JsCode

# Prepare data for the pie chart
expenses_2014 = {
    "Administrative Expense": 3481,
    "Professional Fees": 5672,
    "Engineering": 4185,
    "Insurance": 82795,
    "Management": 39401,
    "Landscaping, Grounds, and snow removal": 207758,
    "Water": 8960,
    "Interest Expense": 28517,
    "Electrical Repairs": 4717,
    "Plumbing": 7621,
    "Exterminator": 3365,
    "Exercise Equipment": 1396,
    "Cleaning": 3810,
    "Building Repairs": 5764,
    "Pool Expenses": 29150,
    "Gutters and leaders": 10600,
    "Sprinklers": 9073,
    "Hill restoration": 92423,
    "Signage": 0,
    "Power washing": 0,
    "Alarm Monitoring and repairs": 1889,
    "Utilities": 9418,
    "Telephone and cable": 2409,
    "Paving": 8783,
    "Mailbox replacement": 33827,
    "Licenses": 315,
    "Provision for State Income Taxes": 585
}

# Income and Net Profit (Loss) data
income_data = {
    "Interest Income": 543,
    "Assessments": 56890,
    "Other Income": 81,
    "Common Charges (Note 1)": 460224,
    "Total Revenues": 517738,
    "Total Expenses": 605914,
    "Net Profit (Loss)": 88176
}

# Create a list of tuples for the data
data = list(expenses_2014.items())

# Create a Pie chart with pyecharts
pie_chart = (
    Pie()
    .add(
        "",
        data,
        radius=["40%", "60%"],
        center=["50%", "70%"],  # Move the pie chart down
        label_opts=opts.LabelOpts(
            formatter=JsCode("function(params){return params.name + ': $' + params.value.toLocaleString();}"),
            position="outside"
        ),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Expenses Distribution for 2014",
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
            subtitle_textstyle_opts=opts.TextStyleOpts(font_size=17, font_weight='bold')  # Increase subtitle size
        ),
        legend_opts=opts.LegendOpts(is_show=False)
    )
)

# Render the chart to a file
file_path = 'expenses_pie_chart_2014.html'
pie_chart.render(file_path)

# Get the absolute file path
absolute_file_path = os.path.abspath(file_path)

# Open the HTML file in the default web browser
webbrowser.open('file://' + absolute_file_path)