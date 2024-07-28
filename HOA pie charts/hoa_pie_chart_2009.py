import pyecharts.options as opts
from pyecharts.charts import Pie
import webbrowser
import os
from pyecharts.commons.utils import JsCode

# Prepare data for the pie chart
expenses_2009 = {
    "Administrative Expense": 5833,
    "Professional Fees": 2938,
    "Insurance": 65125,
    "Management": 36050,
    "Landscaping, Grounds, and Drainage": 149733,
    "Water": 4587,
    "Interest Expense": 9258,
    "Electrical Repairs": 5577,
    "Plumbing": 1438,
    "Exterminator": 2692,
    "Speed Bumps": 0,
    "Cleaning": 5233,
    "Building Repairs": 6839,
    "Pool Expenses": 24911,
    "Gutters and leaders": 10305,
    "Sprinklers": 2288,
    "Paint and plaster": 0,
    "Alarm Monitoring and repairs": 1392,
    "Utilities": 9228,
    "Telephone and cable": 2170,
    "Seal coating": 19165,
    "Masonry": 0,
    "Licenses": 250,
    "Provision for State Income Taxes": 215
}

# Income and Net Profit (Loss) data
income_data = {
    "Interest Income": 1806,
    "Other Income": 961,
    "Common Charges (Note 1)": 427584,
    "Total Revenues": 430351,
    "Total Expenses": 365227,
    "Net Profit (Loss)": 65124
}

# Create a list of tuples for the data
data = list(expenses_2009.items())

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
            title="Expenses Distribution for 2009",
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
file_path = 'expenses_pie_chart_2009.html'
pie_chart.render(file_path)

# Get the absolute file path
absolute_file_path = os.path.abspath(file_path)

# Open the HTML file in the default web browser
webbrowser.open('file://' + absolute_file_path)