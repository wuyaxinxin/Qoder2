# 始终生效

from flask import Flask, render_template
from pork_price_app.data_manager import load_data
from pork_price_app.chart_generator import create_price_chart

app = Flask(__name__)


@app.route('/')
def index():
    """
    主页路由,展示猪肉价格曲线图
    """
    data = load_data()
    
    chart_html = create_price_chart(data)
    
    metadata = data.get('metadata', {})
    
    return render_template(
        'index.html',
        chart_html=chart_html,
        data_source=metadata.get('source', '未知'),
        unit=metadata.get('unit', '元/公斤'),
        description=metadata.get('description', '')
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
