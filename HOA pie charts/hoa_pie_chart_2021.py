import pyecharts.options as opts
from pyecharts.charts import Pie
import webbrowser
import os
from pyecharts.commons.utils import JsCode

# Prepare data for the pie chart
expenses_2021 = {
    "Office expenses": 8143,
    "Professional Fees": 11023,
    "Management": 44810,
    "Water": 15824,
    "Utilities": 11210,
    "Insurance": 96476,
    "Landscaping, Grounds, & Snow": 253273,
    "Equipment": 0,
    "Plumbing, Sewers, and Drains": 4000,
    "Exterminating": 2717,
    "Gutters": 6900,
    "Pool Expenses": 22626,
    "Electrical": 929,
    "Paving": 5067,
    "Janitorial": 4065,
    "Fence": 30226,
    "Other repairs and maintenance": 10945,
    "Corporate Taxes": 647,
}

# Income and Net Profit (Loss) data
income_data = {
    "Assessments": 82528,
    "HOA dues": 598944,
    "Interest income": 558,
    "Other revenue": 0,
    "Total Revenue": 682030,
    "Total Expenses": 528881,
    "Income from operations": 153149,
    "Interest expense on loan": 10415,
    "Major repairs - Lighting Project": 0,
    "Net Profit (Loss)": 142734
}

# Create a list of tuples for the data
data = list(expenses_2021.items())

# Create a Pie chart with pyecharts
pie_chart = (
    Pie()
    .add(
        "",
        data,
        radius=["40%", "60%"],
        center=["66%", "70%"],  # Move the pie chart down
        label_opts=opts.LabelOpts(
            formatter=JsCode("function(params){return params.name + ': $' + params.value.toLocaleString();}"),
            position="outside"
        ),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Expenses Distribution for 2021",
            subtitle=(
                f"Revenue:\n"
                f"  Assessments: ${income_data['Assessments']:,}\n"
                f"  HOA dues: ${income_data['HOA dues']:,}\n"
                f"  Interest Income: ${income_data['Interest income']:,}\n"
                f"  Other revenue: ${income_data['Other revenue']:,}\n"
                f"  Total Revenue: ${income_data['Total Revenue']:,}\n\n"
                f"Total Expenses: ${income_data['Total Expenses']:,}\n\n"
                f"Income from operations:\n"
                f"  Interest expense on loan: ${income_data['Interest expense on loan']:,}\n"
                f"  Major repairs - Lighting Project: ${income_data['Major repairs - Lighting Project']:,}\n\n"
                f"Net Profit (Loss): ${income_data['Net Profit (Loss)']:,}"
            ),
            title_textstyle_opts=opts.TextStyleOpts(font_size=20, font_weight='bold'),
            subtitle_textstyle_opts=opts.TextStyleOpts(font_size=18, font_weight='bold')  # Increase subtitle size
        ),
        legend_opts=opts.LegendOpts(is_show=False)
    )
)

# Render the chart to a file
file_path = 'expenses_pie_chart_2021.html'
pie_chart.render(file_path)

# Get the absolute file path
absolute_file_path = os.path.abspath(file_path)

# Open the HTML file in the default web browser
webbrowser.open('file://' + absolute_file_path)