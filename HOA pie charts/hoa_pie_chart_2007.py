import pyecharts.options as opts
from pyecharts.charts import Pie
import webbrowser
import os
from pyecharts.commons.utils import JsCode

# Prepare data for the pie chart
expenses_2007 = {
    "Administrative Expense": 11680,
    "Professional Fees": 4799,
    "Insurance": 78819,
    "Management": 34576,
    "Landscaping, Grounds, and Drainage": 175462,
    "Water": 13179,
    "Interest Expense": 9384,
    "Payroll and Related Expenses": 11325,
    "Electrical Repairs": 1981,
    "Plumbing": 2478,
    "Exterminator": 2575,
    "Speed Bumps": 781,
    "Cleaning": 3780,
    "Building Repairs": 4222,
    "Pool Expenses": 6250,
    "Gutters and leaders": 13209,
    "Driveways": 0,
    "Settlement costs": 0,
    "Alarm Monitoring and repairs": 2720,
    "Utilities": 10338,
    "Telephone and cable": 1560,
    "Fencing": 4776,
    "Masonry": 11819,
    "Doors, locks & glass": 1613,
    "Licenses": 250,
    "Provision for State Income Taxes": 237
}

# Income and Net Profit (Loss) data
income_data = {
    "Interest Income": 2865,
    "Other Income": 328,
    "Settlement with Sponsor": 0,
    "Common Charges (Note 1)": 387355,
    "Total Revenues": 390548,
    "Total Expenses": 407813,
    "Net Profit (Loss)": 17265
}

# Create a list of tuples for the data
data = list(expenses_2007.items())

# Create a Pie chart with pyecharts
pie_chart = (
    Pie()
    .add(
        "",
        data,
        radius=["40%", "70%"],
        center=["60%", "65%"],  # Move the pie chart down
        label_opts=opts.LabelOpts(
            formatter=JsCode("function(params){return params.name + ': $' + params.value.toLocaleString();}"),
            position="outside"
        ),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Expenses Distribution for 2007",
            subtitle=(
                f"Income:\n"
                f"  Interest Income: ${income_data['Interest Income']:,}\n"
                f"  Other Income: ${income_data['Other Income']:,}\n"
                f"  Settlement with Sponsor: ${income_data['Settlement with Sponsor']:,}\n"
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
file_path = 'expenses_pie_chart_2007.html'
pie_chart.render(file_path)

# Get the absolute file path
absolute_file_path = os.path.abspath(file_path)

# Open the HTML file in the default web browser
webbrowser.open('file://' + absolute_file_path)