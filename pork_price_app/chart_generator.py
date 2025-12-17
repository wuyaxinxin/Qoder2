# 始终生效

import plotly.graph_objects as go
from datetime import datetime


def create_price_chart(data):
    """
    创建Plotly交互式价格曲线图
    
    参数:
        data (dict): 包含价格数据的字典
        
    返回:
        str: Plotly图表的HTML代码
    """
    dates = [item['date'] for item in data['data']]
    prices = [item['price'] for item in data['data']]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=dates,
        y=prices,
        mode='lines',
        name='猪肉价格',
        line=dict(color='#1f77b4', width=2),
        hovertemplate='<b>日期:</b> %{x}<br><b>价格:</b> ¥%{y:.2f}/公斤<extra></extra>'
    ))
    
    fig.update_layout(
        title={
            'text': '国内猪肉价格走势',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 24, 'family': 'Arial, sans-serif'}
        },
        xaxis=dict(
            title='日期',
            showgrid=True,
            gridcolor='lightgray',
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1月", step="month", stepmode="backward"),
                    dict(count=3, label="3月", step="month", stepmode="backward"),
                    dict(count=6, label="6月", step="month", stepmode="backward"),
                    dict(count=1, label="1年", step="year", stepmode="backward"),
                    dict(step="all", label="全部")
                ]),
                bgcolor='white',
                activecolor='lightblue'
            ),
            rangeslider=dict(visible=True),
            type='date'
        ),
        yaxis=dict(
            title='价格 (元/公斤)',
            showgrid=True,
            gridcolor='lightgray'
        ),
        hovermode='x unified',
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(family='Arial, sans-serif', size=12),
        margin=dict(l=60, r=40, t=80, b=120),
        height=600
    )
    
    html_str = fig.to_html(
        include_plotlyjs='cdn',
        div_id='price-chart',
        config={
            'displayModeBar': True,
            'displaylogo': False,
            'modeBarButtonsToRemove': ['lasso2d', 'select2d']
        }
    )
    
    return html_str


if __name__ == '__main__':
    from data_manager import load_data
    
    data = load_data()
    html = create_price_chart(data)
    print("图表生成成功")
