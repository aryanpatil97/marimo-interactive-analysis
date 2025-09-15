# analysis.py
# 23f1000968@ds.study.iitm.ac.in  <-- Required email for grader

import marimo as mo

__generated_with__ = "0.6.14"
app = mo.App()
# Cell 1: Define interactive slider widget
# This cell creates the input control for our analysis
# The slider's value will influence computations in later cells
@app.cell
def slider_cell():
    slider = mo.ui.slider(start=1, stop=10, step=1, label="Select multiplier")
    slider
    return slider

# Cell 2: Define data and dependency on slider
# The result here depends on the slider value from Cell 1
@app.cell
def data_cell(slider):
    base_data = list(range(1, 6))  # Our dataset: 1 to 5
    multiplied_data = [x * slider.value for x in base_data]
    return base_data, multiplied_data

# Cell 3: Dynamic Markdown output
# Shows the relationship between base data and multiplied data
@app.cell
def markdown_cell(base_data, multiplied_data, slider):
    mo.md(f"""
    ## Data Analysis Report
    **Multiplier chosen:** {slider.value}

    **Base data:** {base_data}  
    **Multiplied data:** {multiplied_data}

    {'📈' * slider.value}  (Visual indicator proportional to multiplier)
    """)
    return

if __name__ == "__main__":
    app.run()
