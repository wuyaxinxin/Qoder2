# 始终生效

import plotly.graph_objects as go
from datetime import datetime


def create_sales_chart(data):
    """
    创建Plotly交互式销量曲线图
    
    参数:
        data (dict): 包含销量数据的字典
        
    返回:
        str: Plotly图表的HTML代码
    """
    dates = [item['date'] for item in data['data']]
    sales = [item['sales'] for item in data['data']]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=dates,
        y=sales,
        mode='lines',
        name='A100销量',
        line=dict(color='#76b900', width=2),
        hovertemplate='<b>日期:</b> %{x}<br><b>销量:</b> %{y:,}台<extra></extra>'
    ))
    
    fig.update_layout(
        title={
            'text': 'NVIDIA A100 芯片全球销量趋势',
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
            title='销量 (台/日)',
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
        div_id='sales-chart',
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
    html = create_sales_chart(data)
    print("图表生成成功")