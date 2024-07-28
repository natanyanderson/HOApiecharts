import pyecharts.options as opts
from pyecharts.charts import Pie
import webbrowser
import os
from pyecharts.commons.utils import JsCode

# Prepare data for the pie chart
expenses_2019 = {
    "Office expenses": 6278,
    "Professional Fees": 3001,
    "Management": 43076,
    "Water": 9395,
    "Utilities": 10315,
    "Insurance": 108901,
    "Landscaping, Grounds, & Snow": 211999,
    "Equipment": 542,
    "Plumbing, Sewers, and Drains": 295,
    "Exterminating": 2925,
    "Gutters": 6900,
    "Pool Expenses": 30127,
    "Electrical": 1556,
    "Paving": 3194,
    "Janitorial": 10293,
    "Fence": 12151,
    "Other repairs and maintenance": 11628,
    "Corporate Taxes": 643,
}

# Income and Net Profit (Loss) data
income_data = {
    "Assessments": 82528,
    "HOA dues": 541824,
    "Interest income": 3428,
    "Other revenue": 0,
    "Total Revenue": 627780,
    "Total Expenses": 473219,
    "Income from operations": 154561,
    "Interest expense on loan": 17189,
    "Major repairs - Drainage": 0,
    "Major repairs - Lighting Project": 8776,
    "Major repairs - Water Meter Pit": 0,
    "Major repairs - Pool furniture": 17018,
    "Net Profit (Loss)": 111578
}

# Create a list of tuples for the data
data = list(expenses_2019.items())

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
            title="Expenses Distribution for 2019",
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
                f"  Major repairs - Lighting Project: ${income_data['Major repairs - Lighting Project']:,}\n"
                f"  Major repairs - Water Meter Pit: ${income_data['Major repairs - Water Meter Pit']:,}\n"
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
file_path = 'expenses_pie_chart_2019.html'
pie_chart.render(file_path)

# Get the absolute file path
absolute_file_path = os.path.abspath(file_path)

# Open the HTML file in the default web browser
webbrowser.open('file://' + absolute_file_path)