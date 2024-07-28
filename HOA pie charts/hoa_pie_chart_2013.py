import pyecharts.options as opts
from pyecharts.charts import Pie
import webbrowser
import os
from pyecharts.commons.utils import JsCode

# Prepare data for the pie chart
expenses_2013 = {
    "Administrative Expense": 4499,
    "Professional Fees": 11950,
    "Engineering": 0,
    "Insurance": 100387,
    "Management": 38246,
    "Landscaping, Grounds, and Drainage": 179452,
    "Water": 8325,
    "Interest Expense": 10565,
    "Electrical Repairs": 6519,
    "Plumbing": 2617,
    "Exterminator": 2548,
    "Exercise Equipment": 1288,
    "Cleaning": 3988,
    "Building Repairs": 11408,
    "Pool Expenses": 23967,
    "Gutters and leaders": 8290,
    "Sprinklers": 4391,
    "Hill restoration": 622420,
    "Signage": 6815,
    "Power washing": 8041,
    "Alarm Monitoring and repairs": 1080,
    "Utilities": 7880,
    "Telephone and cable": 1853,
    "Licenses": 336,
    "Provision for State Income Taxes": 347
}

# Income and Net Profit (Loss) data
income_data = {
    "Interest Income": 323,
    "Assessments": 169548,
    "Other Income": 100,
    "Common Charges (Note 1)": 460224,
    "Total Revenues": 630195,
    "Total Expenses": 1067212,
    "Net Profit (Loss)": 437017
}

# Create a list of tuples for the data
data = list(expenses_2013.items())

# Create a Pie chart with pyecharts
pie_chart = (
    Pie()
    .add(
        "",
        data,
        radius=["40%", "60%"],
        center=["50%", "70%"],  # Move the pie chart down
        label_opts=opts.LabelOpts(
            formatter=JsCode("function(params){return params.name + ': $' + params.value.toLocaleString();}"),
            position="outside"
        ),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Expenses Distribution for 2013",
            subtitle=(
                f"Income:\n"
                f"  Interest Income: ${income_data['Interest Income']:,}\n"
                f"  Assessments: ${income_data['Assessments']:,}\n"
                f"  Other Income: ${income_data['Other Income']:,}\n"
                f"  Common Charges (Note 1): ${income_data['Common Charges (Note 1)']:,}\n"
                f"  Total Revenues: ${income_data['Total Revenues']:,}\n\n"
                f"Total Expenses: ${income_data['Total Expenses']:,}\n"
                f"Net Profit (Loss): ${income_data['Net Profit (Loss)']:,}"
            ),
            title_textstyle_opts=opts.TextStyleOpts(font_size=20, font_weight='bold'),
            subtitle_textstyle_opts=opts.TextStyleOpts(font_size=16, font_weight='bold')  # Increase subtitle size
        ),
        legend_opts=opts.LegendOpts(is_show=False)
    )
)

# Render the chart to a file
file_path = 'expenses_pie_chart_2013.html'
pie_chart.render(file_path)

# Get the absolute file path
absolute_file_path = os.path.abspath(file_path)

# Open the HTML file in the default web browser
webbrowser.open('file://' + absolute_file_path)