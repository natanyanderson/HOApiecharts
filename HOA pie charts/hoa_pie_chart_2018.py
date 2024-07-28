import pyecharts.options as opts
from pyecharts.charts import Pie
import webbrowser
import os
from pyecharts.commons.utils import JsCode

# Prepare data for the pie chart
expenses_2018 = {
    "Office expenses": 4903,
    "Professional Fees": 2951,
    "Management": 42231,
    "Water": 12347,
    "Utilities": 10291,
    "Insurance": 107288,
    "Landscaping, Grounds, & Snow": 222359,
    "Equipment": 7457,
    "Plumbing, Sewers, and Drains": 15602,
    "Exterminating": 2468,
    "Gutters": 6900,
    "Pool Expenses": 36861,
    "Electrical": 4041,
    "Paving": 6362,
    "Janitorial": 5867,
    "Fence": 14594,
    "Other repairs and maintenance": 6999,
    "Corporate Taxes": 642,
}

# Income and Net Profit (Loss) data
income_data = {
    "Assessments": 81081,
    "HOA dues": 509184,
    "Interest income": 1879,
    "Other revenue": 346,
    "Total Revenue": 592490,
    "Total Expenses": 510163,
    "Income from operations": 82327,
    "Interest expense on loan": 20317,
    "Major repairs - Drainage": 25448,
    "Major repairs - Water Meter Pit": 13300,
    "Net Profit (Loss)": 23262
}

# Create a list of tuples for the data
data = list(expenses_2018.items())

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
            title="Expenses Distribution for 2018",
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
                f"  Major repairs - Drainage: ${income_data['Major repairs - Drainage']:,}\n"
                f"  Major repairs - Water Meter Pit: ${income_data['Major repairs - Water Meter Pit']:,}\n\n"
                f"Net Profit (Loss): ${income_data['Net Profit (Loss)']:,}"
            ),
            title_textstyle_opts=opts.TextStyleOpts(font_size=20, font_weight='bold'),
            subtitle_textstyle_opts=opts.TextStyleOpts(font_size=16, font_weight='bold')  # Increase subtitle size
        ),
        legend_opts=opts.LegendOpts(is_show=False)
    )
)

# Render the chart to a file
file_path = 'expenses_pie_chart_2018.html'
pie_chart.render(file_path)

# Get the absolute file path
absolute_file_path = os.path.abspath(file_path)

# Open the HTML file in the default web browser
webbrowser.open('file://' + absolute_file_path)