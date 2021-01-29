from bokeh.io import output_file, show
from bokeh.layouts import gridplot
from bokeh.plotting import figure
import pandas as pd
from bokeh.transform import cumsum
from bokeh.palettes import Category20c
from math import pi

output_file("layout_grid_convenient.html")

x = list(range(11))
y0 = x
y1 = [10 - i for i in x]
y2 = [abs(i - 5) for i in x]

# create three plots
s1 = figure(background_fill_color="#fafafa",)
s1.circle(x, y0, size=12, alpha=0.8, color="#53777a")

s2 = figure(background_fill_color="#fafafa",x_range=s1.x_range, y_range=s1.y_range)
s2.triangle(x, y1, size=12, alpha=0.8, color="#c02942")

s3 = figure(background_fill_color="#fafafa",x_range=s1.x_range, y_range=s1.y_range)
s3.square(x, y2, size=12, alpha=0.8, color="#d95b43")
TOOLS = "box_select,lasso_select,help"
p = figure(title="simple line example", x_axis_label='x', y_axis_label='y',x_range=s1.x_range, y_range=s1.y_range,tools=TOOLS)
p.line(x, y1, legend_label="Temp.", line_width=2)

z = figure(x_range=s1.x_range, y_range=s1.y_range)
z.vbar(x=[1, 2, 3], width=0.5, bottom=0,
       top=[1.2, 2.5, 3.7], color="firebrick")


x = {
    'United States': 157,
    'United Kingdom': 93,
    'Japan': 89,
    'China': 63,
    'Germany': 44,
    'India': 42,
    'Italy': 40,
    'Australia': 35,
    'Brazil': 32,
    'France': 31,
    'Taiwan': 31,
    'Spain': 29
}

data = pd.Series(x).reset_index(name='value').rename(columns={'index':'country'})
data['angle'] = data['value']/data['value'].sum() * 2*pi
data['color'] = Category20c[len(x)]
pi = figure(plot_height=350, title="Pie Chart", toolbar_location=None,
           tools="hover", tooltips="@country: @value", x_range=(-0.5, 1.0))
pi.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='country', source=data)
pi.axis.axis_label=None
pi.axis.visible=False
pi.grid.grid_line_color = None


# make a grid
grid = gridplot([s1, s2,s3,p,z,pi], ncols=3 ,  plot_width=550, plot_height=440)
show(grid)