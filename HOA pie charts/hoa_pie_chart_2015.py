import pyecharts.options as opts
from pyecharts.charts import Pie
import webbrowser
import os
from pyecharts.commons.utils import JsCode

# Prepare data for the pie chart
expenses_2015 = {
    "Administrative Expense": 4934,
    "Professional Fees": 2500,
    "Engineering": 0,
    "Insurance": 79501,
    "Management": 40189,
    "Landscaping, Grounds, and snow removal": 182945,
    "Water": 7043,
    "Interest Expense": 28756,
    "Electrical Repairs": 1774,
    "Plumbing": 1342,
    "Exterminator": 3119,
    "Exercise Equipment": 1315,
    "Cleaning": 3496,
    "Building Repairs": 5418,
    "Pool Expenses": 26119,
    "Gutters and leaders": 3450,
    "Sprinklers": 14039,
    "Hill restoration": 0,
    "Fencing": 10294,
    "Pool resurfacing": 18919,
    "Alarm Monitoring and repairs": 2329,
    "Utilities": 8028,
    "Telephone and cable": 2107,
    "Paving": 6400,
    "Mailbox replacement": 0,
    "Licenses": 315,
    "Provision for State Income Taxes": 585
}

# Income and Net Profit (Loss) data
income_data = {
    "Interest Income": 458,
    "Assessments": 58900,
    "Expense reimbursement": 32449,
    "Other Income": 645,
    "Common Charges (Note 1)": 476554,
    "Total Revenues": 568996,
    "Total Expenses": 454917,
    "Net Profit (Loss)": 114079
}

# Create a list of tuples for the data
data = list(expenses_2015.items())

# Create a Pie chart with pyecharts
pie_chart = (
    Pie()
    .add(
        "",
        data,
        radius=["40%", "60%"],
        center=["52%", "70%"],  # Move the pie chart down
        label_opts=opts.LabelOpts(
            formatter=JsCode("function(params){return params.name + ': $' + params.value.toLocaleString();}"),
            position="outside"
        ),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Expenses Distribution for 2015",
            subtitle=(
                f"Income:\n"
                f"  Interest Income: ${income_data['Interest Income']:,}\n"
                f"  Assessments: ${income_data['Assessments']:,}\n"
                f"  Expense reimbursement: ${income_data['Expense reimbursement']:,}\n"
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
file_path = 'expenses_pie_chart_2015.html'
pie_chart.render(file_path)

# Get the absolute file path
absolute_file_path = os.path.abspath(file_path)

# Open the HTML file in the default web browser
webbrowser.open('file://' + absolute_file_path)