import plotly.figure_factory as ff
import csv
import pandas as pd

df = pd.read_csv("data.csv")

#x = df["Height"].tolist()

#fig = ff.create_distplot([df["Height"].tolist()],["HEIGHT OF 18+"],show_hist= False)
fig = ff.create_distplot([df["Weight"].tolist()],["WEIGHT OF 18+"],show_hist = True)
fig.show()
print("initializing......")

