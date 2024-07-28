import pyecharts.options as opts
from pyecharts.charts import Pie
import webbrowser
import os
from pyecharts.commons.utils import JsCode

# Prepare data for the pie chart
expenses_2010 = {
    "Administrative Expense": 5589,
    "Professional Fees": 4132,
    "Insurance": 84785,
    "Management": 37132,
    "Landscaping, Grounds, and Drainage": 164982,
    "Water": 10441,
    "Interest Expense": 9207,
    "Electrical Repairs": 4621,
    "Plumbing": 3542,
    "Exterminator": 2692,
    "Exercise Equipment": 5154,
    "Cleaning": 4820,
    "Building Repairs": 7173,
    "Pool Expenses": 19125,
    "Gutters and leaders": 10350,
    "Sprinklers": 4271,
    "Paint and plaster": 1083,
    "Alarm Monitoring and repairs": 1540,
    "Utilities": 9079,
    "Telephone and cable": 1763,
    "Seal coating": 5502,
    "Licenses": 310,
    "Provision for State Income Taxes": 290
}

# Income and Net Profit (Loss) data
income_data = {
    "Interest Income": 1655,
    "Other Income": 206,
    "Common Charges (Note 1)": 427584,
    "Total Revenues": 429445,
    "Total Expenses": 397583,
    "Net Profit (Loss)": 31862
}

# Create a list of tuples for the data
data = list(expenses_2010.items())

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
            title="Expenses Distribution for 2010",
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
file_path = 'expenses_pie_chart_2010.html'
pie_chart.render(file_path)

# Get the absolute file path
absolute_file_path = os.path.abspath(file_path)

# Open the HTML file in the default web browser
webbrowser.open('file://' + absolute_file_path)