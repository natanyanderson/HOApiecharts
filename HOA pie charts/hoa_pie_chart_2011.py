import pyecharts.options as opts
from pyecharts.charts import Pie
import webbrowser
import os
from pyecharts.commons.utils import JsCode

# Prepare data for the pie chart
expenses_2011 = {
    "Administrative Expense": 4632,
    "Professional Fees": 13379,
    "Engineering": 27242,
    "Insurance": 88662,
    "Management": 38246,
    "Landscaping, Grounds, and Drainage": 197991,
    "Water": 6530,
    "Interest Expense": 8929,
    "Electrical Repairs": 12580,
    "Plumbing": 3785,
    "Exterminator": 2742,
    "Exercise Equipment": 1449,
    "Cleaning": 4922,
    "Building Repairs": 12963,
    "Pool Expenses": 22039,
    "Gutters and leaders": 6900,
    "Sprinklers": 10752,
    "Paint and plaster": 1717,
    "Alarm Monitoring and repairs": 1574,
    "Utilities": 7998,
    "Telephone and cable": 1583,
    "Seal coating": 0,
    "Licenses": 318,
    "Provision for State Income Taxes": 375
}

# Income and Net Profit (Loss) data
income_data = {
    "Interest Income": 862,
    "Other Income": 705,
    "Common Charges (Note 1)": 443904,
    "Total Revenues": 445471,
    "Total Expenses": 477308,
    "Net Profit (Loss)": 31837
}

# Create a list of tuples for the data
data = list(expenses_2011.items())

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
            title="Expenses Distribution for 2011",
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
file_path = 'expenses_pie_chart_2011.html'
pie_chart.render(file_path)

# Get the absolute file path
absolute_file_path = os.path.abspath(file_path)

# Open the HTML file in the default web browser
webbrowser.open('file://' + absolute_file_path)