# 始终生效

import requests
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime


def fetch_bitcoin_data(days=1825):
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    params = {
        "vs_currency": "usd",
        "days": days
    }
    
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    data = response.json()
    
    prices = data["prices"]
    df = pd.DataFrame(prices, columns=["timestamp", "price"])
    df["date"] = pd.to_datetime(df["timestamp"], unit="ms")
    
    return df


def create_bitcoin_chart(df):
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=df["date"],
        y=df["price"],
        mode="lines",
        name="Bitcoin Price",
        line=dict(color="#f7931a", width=2),
        hovertemplate="<b>日期:</b> %{x|%Y-%m-%d}<br><b>价格:</b> $%{y:,.2f}<extra></extra>"
    ))
    
    fig.update_layout(
        title={
            "text": "比特币近五年价格走势",
            "x": 0.5,
            "xanchor": "center",
            "font": {"size": 24, "family": "Arial, sans-serif"}
        },
        xaxis=dict(
            title="日期",
            showgrid=True,
            gridcolor="lightgray",
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1月", step="month", stepmode="backward"),
                    dict(count=3, label="3月", step="month", stepmode="backward"),
                    dict(count=6, label="6月", step="month", stepmode="backward"),
                    dict(count=1, label="1年", step="year", stepmode="backward"),
                    dict(count=3, label="3年", step="year", stepmode="backward"),
                    dict(count=5, label="5年", step="year", stepmode="backward"),
                    dict(step="all", label="全部")
                ]),
                bgcolor="white",
                activecolor="lightblue"
            ),
            rangeslider=dict(visible=True),
            type="date"
        ),
        yaxis=dict(
            title="价格 (USD)",
            showgrid=True,
            gridcolor="lightgray",
            tickformat="$,.0f"
        ),
        hovermode="x unified",
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(family="Arial, sans-serif", size=12),
        margin=dict(l=80, r=40, t=80, b=120),
        height=600
    )
    
    return fig


def main():
    print("正在获取比特币价格数据...")
    df = fetch_bitcoin_data()
    print(f"获取到 {len(df)} 条数据")
    
    print("正在生成图表...")
    fig = create_bitcoin_chart(df)
    
    output_file = "bitcoin_price_chart.html"
    fig.write_html(
        output_file,
        include_plotlyjs="cdn",
        config={
            "displayModeBar": True,
            "displaylogo": False,
            "modeBarButtonsToRemove": ["lasso2d", "select2d"]
        }
    )
    print(f"图表已保存至: {output_file}")


if __name__ == "__main__":
    main()
