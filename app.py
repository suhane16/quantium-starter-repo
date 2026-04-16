import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

df = pd.read_csv("formatted_output.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

app = Dash(__name__)

app.layout = html.Div(
    style={
        "backgroundColor": "#f4f7fb",
        "minHeight": "100vh",
        "padding": "30px",
        "fontFamily": "Arial, sans-serif",
    },
    children=[
        html.Div(
            style={
                "maxWidth": "1100px",
                "margin": "0 auto",
                "backgroundColor": "white",
                "padding": "30px",
                "borderRadius": "16px",
                "boxShadow": "0 8px 24px rgba(0,0,0,0.08)",
            },
            children=[
                html.H1(
                    "Pink Morsels Sales Visualiser",
                    id="app-title",
                    style={
                        "textAlign": "center",
                        "color": "#1f3b73",
                        "marginBottom": "10px",
                    },
                ),
                html.P(
                    "Explore sales over time and filter by region.",
                    style={
                        "textAlign": "center",
                        "color": "#5b657a",
                        "marginBottom": "25px",
                    },
                ),
                html.Label(
                    "Select Region:",
                    style={
                        "fontWeight": "bold",
                        "fontSize": "16px",
                        "color": "#1f3b73",
                    },
                ),
                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                    style={"marginTop": "10px", "marginBottom": "25px"},
                    inputStyle={"marginRight": "6px", "marginLeft": "12px"},
                    labelStyle={"color": "#344055", "fontSize": "15px"},
                ),
                dcc.Graph(id="sales-line-chart"),
            ],
        )
    ],
)


@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df.copy()
    else:
        filtered_df = df[df["Region"].str.lower() == selected_region]

    fig = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        title=f"Pink Morsels Sales Over Time - {selected_region.title()}",
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales",
        plot_bgcolor="#edf2f9",
        paper_bgcolor="white",
        font=dict(color="#1f2d3d"),
        title_font=dict(size=22),
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)