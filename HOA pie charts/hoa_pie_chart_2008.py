import pyecharts.options as opts
from pyecharts.charts import Pie
import webbrowser
import os
from pyecharts.commons.utils import JsCode

# Prepare data for the pie chart
expenses_2008 = {
    "Administrative Expense": 7484,
    "Professional Fees": 2678,
    "Insurance": 78767,
    "Management": 35000,
    "Landscaping, Grounds, and Drainage": 167214,
    "Water": 3268,
    "Interest Expense": 9278,
    "Payroll and Related Expenses": 0,
    "Electrical Repairs": 3249,
    "Plumbing": 1481,
    "Exterminator": 2692,
    "Speed Bumps": 0,
    "Cleaning": 4027,
    "Building Repairs": 7743,
    "Pool Expenses": 15378,
    "Gutters and leaders": 6880,
    "Sprinklers": 6650,
    "Paint and plaster": 2895,
    "Alarm Monitoring and repairs": 1080,
    "Utilities": 10954,
    "Telephone and cable": 1535,
    "Fencing": 0,
    "Masonry": 3758,
    "Doors, locks & glass": 0,
    "Licenses": 640,
    "Provision for State Income Taxes": 3
}

# Income and Net Profit (Loss) data
income_data = {
    "Interest Income": 1844,
    "Other Income": 912,
    "Common Charges (Note 1)": 387355,
    "Total Revenues": 390111,
    "Total Expenses": 372654,
    "Net Profit (Loss)": 17457
}

# Create a list of tuples for the data
data = list(expenses_2008.items())

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
            title="Expenses Distribution for 2008",
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
file_path = 'expenses_pie_chart_2008.html'
pie_chart.render(file_path)

# Get the absolute file path
absolute_file_path = os.path.abspath(file_path)

# Open the HTML file in the default web browser
webbrowser.open('file://' + absolute_file_path)