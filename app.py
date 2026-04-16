import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

df = pd.read_csv("formatted_output.csv")

df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

fig = px.line(
    df,
    x="Date",
    y="Sales",
    title="Pink Morsels Sales Over Time"
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Sales"
)

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsels Sales Visualiser"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)