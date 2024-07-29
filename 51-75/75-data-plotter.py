import pandas as pd
from bokeh.plotting import output_file, show
from bokeh.plotting import figure

output_file("bokeh_plot.html")
data = pd.read_csv(r"C:\Users\ndifreke\Desktop\100-python-projects\sampledata_x_2.txt")

f = figure()

f.line(x=data["x"], y=data["y"])

show(f)