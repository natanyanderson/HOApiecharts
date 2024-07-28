import pyecharts.options as opts
from pyecharts.charts import Pie
import webbrowser
import os
from pyecharts.commons.utils import JsCode

# Prepare data for the pie chart
expenses_2020 = {
    "Office expenses": 6244,
    "Professional Fees": 3201,
    "Management": 44368,
    "Water": 14491,
    "Utilities": 8822,
    "Insurance": 110011,
    "Landscaping, Grounds, & Snow": 223891,
    "Equipment": 325,
    "Plumbing, Sewers, and Drains": 639,
    "Exterminating": 2717,
    "Gutters": 3450,
    "Pool Expenses": 21543,
    "Electrical": 0,
    "Paving": 13276,
    "Janitorial": 1465,
    "Fence": 14275,
    "Other repairs and maintenance": 12705,
    "Corporate Taxes": 645,
}

# Income and Net Profit (Loss) data
income_data = {
    "Assessments": 82528,
    "HOA dues": 574464,
    "Interest income": 1874,
    "Other revenue": 3704,
    "Total Revenue": 662570,
    "Total Expenses": 482068,
    "Income from operations": 180502,
    "Interest expense on loan": 13933,
    "Major repairs - Lighting Project": 1840,
    "Major repairs - Pool furniture": 0,
    "Net Profit (Loss)": 164729
}

# Create a list of tuples for the data
data = list(expenses_2020.items())

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
            title="Expenses Distribution for 2020",
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
                f"  Major repairs - Lighting Project: ${income_data['Major repairs - Lighting Project']:,}\n"
                f"  Major repairs - Pool furniture: ${income_data['Major repairs - Pool furniture']:,}\n\n"
                f"Net Profit (Loss): ${income_data['Net Profit (Loss)']:,}"
            ),
            title_textstyle_opts=opts.TextStyleOpts(font_size=20, font_weight='bold'),
            subtitle_textstyle_opts=opts.TextStyleOpts(font_size=15, font_weight='bold')  # Increase subtitle size
        ),
        legend_opts=opts.LegendOpts(is_show=False)
    )
)

# Render the chart to a file
file_path = 'expenses_pie_chart_2020.html'
pie_chart.render(file_path)

# Get the absolute file path
absolute_file_path = os.path.abspath(file_path)

# Open the HTML file in the default web browser
webbrowser.open('file://' + absolute_file_path)