import pyecharts.options as opts
from pyecharts.charts import Pie
import webbrowser
import os
from pyecharts.commons.utils import JsCode

# Prepare data for the pie chart
expenses_2022 = {
    "Office expenses": 1738,
    "HOA dues expense": 449232,
    "HOA assessments": 58880,
    "Professional fees": 3333,
    "Utilities": 626,
    "Insurance": 4159,
    "Sprinklers": 9428,
    "Powerwashing & Deck staining": 13579,
    "Window wells": 137210,
    "Walkway": 0,
    "Roof": 7143,
    "Other repairs and maintenance": 2242,
    "Corporate Taxes": 650
}

# Income and Net Profit (Loss) data
income_data = {
    "Common Charges": 112990,
    "Assessments": 41240,
    "Assessments - Road Fund": 17640,
    "Late Fees": 1700,
    "Chargeback Income": 195,
    "Interest Income": 3025,
    "HOA dues income": 449232,
    "Other revenue": 978,
    "Total revenue": 627000,
    "Total expenses": 688220,
    "Income from operations": 61220,
    "Net Profit (Loss)": 61220
}

# Create a list of tuples for the data
data = list(expenses_2022.items())

# Create a Pie chart with pyecharts
pie_chart = (
    Pie()
    .add(
        "",
        data,
        radius=["40%", "60%"],
        center=["61%", "70%"],  # Move the pie chart down
        label_opts=opts.LabelOpts(
            formatter=JsCode("function(params){return params.name + ': $' + params.value.toLocaleString();}"),
            position="outside"
        ),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Expenses Distribution for 2022",
            subtitle=(
                f"Revenue:\n"
                f"  Common Charges: ${income_data['Common Charges']:,}\n"
                f"  Assessments: ${income_data['Assessments']:,}\n"
                f"  Assessments - Road Fund: ${income_data['Assessments - Road Fund']:,}\n"
                f"  Late Fees: ${income_data['Late Fees']:,}\n"
                f"  Chargeback Income: ${income_data['Chargeback Income']:,}\n"
                f"  Interest Income: ${income_data['Interest Income']:,}\n"
                f"  HOA dues income: ${income_data['HOA dues income']:,}\n"
                f"  Other revenue: ${income_data['Other revenue']:,}\n\n"
                f"Total revenue: ${income_data['Total revenue']:,}\n"
                f"Total expenses: ${income_data['Total expenses']:,}\n"
                f"Income from operations: ${income_data['Income from operations']:,}\n"
                f"Net Profit (Loss): ${income_data['Net Profit (Loss)']:,}"
            ),
            title_textstyle_opts=opts.TextStyleOpts(font_size=20, font_weight='bold'),
            subtitle_textstyle_opts=opts.TextStyleOpts(font_size=16, font_weight='bold')  # Increase subtitle size
        ),
        legend_opts=opts.LegendOpts(is_show=False)
    )
)

# Render the chart to a file
file_path = 'expenses_pie_chart_2022.html'
pie_chart.render(file_path)

# Get the absolute file path
absolute_file_path = os.path.abspath(file_path)

# Open the HTML file in the default web browser
webbrowser.open('file://' + absolute_file_path)