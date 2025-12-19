<%-- 
  始终生效
  自由万岁
  京东首页风格演示页面
  运行环境: Apache Tomcat 9.0+
--%>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%!
    public class Product {
        public String name;
        public double price;
        public double originalPrice;
        public String imageUrl;
        public String tag;
        
        public Product(String name, double price, double originalPrice, String imageUrl, String tag) {
            this.name = name;
            this.price = price;
            this.originalPrice = originalPrice;
            this.imageUrl = imageUrl;
            this.tag = tag;
        }
    }
%>
<%
    String[] categories = {
        "家用电器", "手机通讯", "电脑办公", "家居家装",
        "男装女装", "鞋靴箱包", "运动户外", "食品生鲜",
        "美妆护肤", "母婴玩具", "图书音像", "医药保健"
    };
    
    Product[] products = {
        new Product("Apple iPhone 15 Pro Max 256GB 原色钛金属", 9999.00, 10999.00, "https://via.placeholder.com/220x220/f5f5f5/333333?text=iPhone15", "自营"),
        new Product("华为 HUAWEI Mate 60 Pro 12GB+512GB 雅丹黑", 6999.00, 7999.00, "https://via.placeholder.com/220x220/f5f5f5/333333?text=Mate60", "自营"),
        new Product("小米14 Ultra 徕卡光学Summilux镜头 16GB+512GB", 6499.00, 6999.00, "https://via.placeholder.com/220x220/f5f5f5/333333?text=Mi14", "自营"),
        new Product("联想ThinkPad X1 Carbon 2024款 i7-1365U 16GB", 12999.00, 14999.00, "https://via.placeholder.com/220x220/f5f5f5/333333?text=ThinkPad", "自营"),
        new Product("戴森 Dyson V15 Detect 无绳吸尘器 激光探测", 4990.00, 5990.00, "https://via.placeholder.com/220x220/f5f5f5/333333?text=Dyson", "自营"),
        new Product("索尼 PlayStation 5 光驱版 国行游戏机", 3899.00, 4299.00, "https://via.placeholder.com/220x220/f5f5f5/333333?text=PS5", "自营"),
        new Product("海尔 Leader 滚筒洗衣机 10公斤 全自动变频", 2299.00, 2999.00, "https://via.placeholder.com/220x220/f5f5f5/333333?text=Haier", "自营"),
        new Product("格力 GREE 新一级能效 变频冷暖空调 1.5匹", 3599.00, 4299.00, "https://via.placeholder.com/220x220/f5f5f5/333333?text=Gree", "自营"),
        new Product("雅诗兰黛 小棕瓶精华液 100ml 修护保湿", 1080.00, 1350.00, "https://via.placeholder.com/220x220/f5f5f5/333333?text=EsteeLauder", "自营"),
        new Product("茅台 飞天53度 500ml 酱香型白酒", 1499.00, 1699.00, "https://via.placeholder.com/220x220/f5f5f5/333333?text=Moutai", "自营")
    };
%>
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>京东(JD.COM)-正品低价、品质保障、配送及时、轻松购物！</title>
    <style>
        :root {
            --jd-red: #e1251b;
            --jd-red-dark: #c91623;
            --text-primary: #333333;
            --text-secondary: #666666;
            --text-light: #999999;
            --bg-gray: #f5f5f5;
            --border-color: #e4e4e4;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: "Microsoft YaHei", "PingFang SC", "Helvetica Neue", Arial, sans-serif;
            font-size: 12px;
            color: var(--text-primary);
            background-color: var(--bg-gray);
            min-width: 1200px;
        }
        
        a {
            text-decoration: none;
            color: inherit;
        }
        
        a:hover {
            color: var(--jd-red);
        }
        
        .container {
            width: 1200px;
            margin: 0 auto;
        }
        
        .header-top {
            background-color: #e3e4e5;
            height: 30px;
            line-height: 30px;
            font-size: 12px;
            color: var(--text-secondary);
        }
        
        .header-top .container {
            display: flex;
            justify-content: space-between;
        }
        
        .header-top-left a,
        .header-top-right a {
            margin: 0 10px;
            color: var(--text-secondary);
        }
        
        .header-main {
            background-color: #fff;
            height: 100px;
            border-bottom: 2px solid var(--jd-red);
        }
        
        .header-main .container {
            display: flex;
            align-items: center;
            height: 100%;
        }
        
        .logo {
            width: 190px;
            height: 60px;
            display: flex;
            align-items: center;
        }
        
        .logo-text {
            font-size: 36px;
            font-weight: bold;
            color: var(--jd-red);
            font-style: italic;
        }
        
        .logo-slogan {
            font-size: 10px;
            color: var(--jd-red);
            margin-left: 5px;
        }
        
        .search-box {
            flex: 1;
            margin: 0 50px;
        }
        
        .search-form {
            display: flex;
            height: 36px;
        }
        
        .search-input {
            flex: 1;
            height: 36px;
            border: 2px solid var(--jd-red);
            border-right: none;
            padding: 0 10px;
            font-size: 14px;
            outline: none;
        }
        
        .search-btn {
            width: 80px;
            height: 36px;
            background-color: var(--jd-red);
            border: none;
            color: #fff;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        
        .search-btn:hover {
            background-color: var(--jd-red-dark);
        }
        
        .hot-words {
            margin-top: 8px;
        }
        
        .hot-words a {
            margin-right: 10px;
            color: var(--text-light);
        }
        
        .hot-words a:first-child {
            color: var(--jd-red);
        }
        
        .header-cart {
            width: 160px;
            height: 36px;
            border: 1px solid #e4e4e4;
            display: flex;
            align-items: center;
            justify-content: center;
            background-color: #fff;
            cursor: pointer;
            transition: border-color 0.3s;
        }
        
        .header-cart:hover {
            border-color: var(--jd-red);
        }
        
        .cart-icon {
            color: var(--jd-red);
            margin-right: 5px;
            font-size: 16px;
        }
        
        .cart-count {
            background-color: var(--jd-red);
            color: #fff;
            padding: 0 5px;
            border-radius: 8px;
            font-size: 10px;
            margin-left: 5px;
        }
        
        .nav-bar {
            background-color: #fff;
            height: 35px;
            border-bottom: 1px solid var(--border-color);
        }
        
        .nav-bar .container {
            display: flex;
            align-items: center;
            height: 100%;
        }
        
        .nav-all {
            width: 210px;
            height: 35px;
            line-height: 35px;
            background-color: var(--jd-red);
            color: #fff;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
        }
        
        .nav-links {
            display: flex;
            margin-left: 20px;
        }
        
        .nav-links a {
            padding: 0 15px;
            font-size: 14px;
            font-weight: bold;
            height: 35px;
            line-height: 35px;
        }
        
        .main-section {
            margin-top: 10px;
        }
        
        .main-section .container {
            display: flex;
            position: relative;
        }
        
        .category-menu {
            width: 210px;
            background-color: rgba(0, 0, 0, 0.75);
            position: absolute;
            left: 0;
            top: 0;
            z-index: 100;
            height: 420px;
        }
        
        .category-item {
            height: 35px;
            line-height: 35px;
            padding: 0 20px;
            color: #fff;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: background-color 0.2s;
        }
        
        .category-item:hover {
            background-color: var(--jd-red);
        }
        
        .category-arrow {
            font-size: 10px;
        }
        
        .banner-section {
            width: 100%;
            height: 420px;
            position: relative;
            overflow: hidden;
        }
        
        .carousel {
            width: 100%;
            height: 420px;
            position: relative;
        }
        
        .carousel-inner {
            width: 100%;
            height: 100%;
            position: relative;
        }
        
        .carousel-item {
            position: absolute;
            width: 100%;
            height: 100%;
            opacity: 0;
            transition: opacity 0.5s ease-in-out;
        }
        
        .carousel-item.active {
            opacity: 1;
        }
        
        .carousel-item img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        
        .carousel-indicators {
            position: absolute;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            gap: 10px;
            z-index: 10;
        }
        
        .carousel-indicator {
            width: 30px;
            height: 6px;
            background-color: rgba(255, 255, 255, 0.5);
            cursor: pointer;
            border-radius: 3px;
            transition: background-color 0.3s;
        }
        
        .carousel-indicator.active,
        .carousel-indicator:hover {
            background-color: #fff;
        }
        
        .carousel-arrow {
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            width: 40px;
            height: 70px;
            background-color: rgba(0, 0, 0, 0.3);
            color: #fff;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            cursor: pointer;
            opacity: 0;
            transition: opacity 0.3s;
            z-index: 10;
        }
        
        .carousel:hover .carousel-arrow {
            opacity: 1;
        }
        
        .carousel-arrow:hover {
            background-color: rgba(0, 0, 0, 0.5);
        }
        
        .carousel-arrow.prev {
            left: 210px;
        }
        
        .carousel-arrow.next {
            right: 0;
        }
        
        .products-section {
            margin-top: 20px;
            padding: 20px 0;
        }
        
        .section-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }
        
        .section-title {
            font-size: 22px;
            font-weight: bold;
            color: var(--text-primary);
        }
        
        .section-more {
            color: var(--text-light);
        }
        
        .products-grid {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 15px;
        }
        
        .product-card {
            background-color: #fff;
            padding: 15px;
            transition: box-shadow 0.3s, transform 0.3s;
            cursor: pointer;
        }
        
        .product-card:hover {
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.15);
            transform: translateY(-3px);
        }
        
        .product-img {
            width: 100%;
            height: 200px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 10px;
        }
        
        .product-img img {
            max-width: 100%;
            max-height: 100%;
            object-fit: contain;
        }
        
        .product-name {
            height: 36px;
            line-height: 18px;
            overflow: hidden;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            line-clamp: 2;
            -webkit-box-orient: vertical;
            font-size: 12px;
            color: var(--text-primary);
            margin-bottom: 10px;
        }
        
        .product-price {
            display: flex;
            align-items: baseline;
            gap: 8px;
        }
        
        .price-current {
            color: var(--jd-red);
            font-size: 18px;
            font-weight: bold;
        }
        
        .price-original {
            color: var(--text-light);
            text-decoration: line-through;
            font-size: 12px;
        }
        
        .product-tag {
            display: inline-block;
            background-color: var(--jd-red);
            color: #fff;
            padding: 2px 5px;
            font-size: 10px;
            margin-top: 8px;
            border-radius: 2px;
        }
        
        .footer {
            background-color: #fff;
            margin-top: 30px;
            padding: 30px 0;
            border-top: 1px solid var(--border-color);
        }
        
        .footer-links {
            display: flex;
            justify-content: center;
            gap: 30px;
            margin-bottom: 20px;
        }
        
        .footer-links a {
            color: var(--text-secondary);
        }
        
        .footer-copyright {
            text-align: center;
            color: var(--text-light);
            font-size: 12px;
        }
        
        @media (max-width: 1199px) {
            body {
                min-width: 992px;
            }
            .container {
                width: 992px;
            }
            .products-grid {
                grid-template-columns: repeat(4, 1fr);
            }
        }
        
        @media (max-width: 991px) {
            body {
                min-width: 768px;
            }
            .container {
                width: 768px;
            }
            .category-menu {
                display: none;
            }
            .carousel-arrow.prev {
                left: 0;
            }
            .products-grid {
                grid-template-columns: repeat(3, 1fr);
            }
        }
        
        @media (max-width: 767px) {
            body {
                min-width: 100%;
            }
            .container {
                width: 100%;
                padding: 0 15px;
            }
            .header-main {
                height: auto;
                padding: 15px 0;
            }
            .header-main .container {
                flex-wrap: wrap;
            }
            .logo {
                width: 100%;
                justify-content: center;
                margin-bottom: 10px;
            }
            .search-box {
                width: 100%;
                margin: 0;
            }
            .header-cart {
                width: 100%;
                margin-top: 10px;
            }
            .nav-all {
                display: none;
            }
            .products-grid {
                grid-template-columns: 1fr;
            }
            .banner-section {
                height: 200px;
            }
            .carousel {
                height: 200px;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="header-top">
            <div class="container">
                <div class="header-top-left">
                    <a href="#">北京</a>
                    <a href="#">你好，请登录</a>
                    <a href="#" style="color: var(--jd-red);">免费注册</a>
                </div>
                <div class="header-top-right">
                    <a href="#">我的订单</a>
                    <a href="#">我的京东</a>
                    <a href="#">京东会员</a>
                    <a href="#">企业采购</a>
                    <a href="#">客户服务</a>
                    <a href="#">网站导航</a>
                </div>
            </div>
        </div>
        
        <div class="header-main">
            <div class="container">
                <div class="logo">
                    <span class="logo-text">JD</span>
                    <span class="logo-slogan">多快好省</span>
                </div>
                
                <div class="search-box">
                    <div class="search-form">
                        <input type="text" class="search-input" placeholder="搜索商品">
                        <button class="search-btn" onclick="alert('搜索功能演示')">搜索</button>
                    </div>
                    <div class="hot-words">
                        <a href="#">iPhone 15</a>
                        <a href="#">华为Mate60</a>
                        <a href="#">小米14</a>
                        <a href="#">笔记本电脑</a>
                        <a href="#">空调</a>
                        <a href="#">冰箱</a>
                    </div>
                </div>
                
                <div class="header-cart">
                    <span class="cart-icon">&#128722;</span>
                    <span>我的购物车</span>
                    <span class="cart-count">0</span>
                </div>
            </div>
        </div>
        
        <nav class="nav-bar">
            <div class="container">
                <div class="nav-all">全部商品分类</div>
                <div class="nav-links">
                    <a href="#">秒杀</a>
                    <a href="#">优惠券</a>
                    <a href="#">PLUS会员</a>
                    <a href="#">闪购</a>
                    <a href="#">拍卖</a>
                    <a href="#">京东超市</a>
                    <a href="#">京东生鲜</a>
                    <a href="#">京东到家</a>
                </div>
            </div>
        </nav>
    </header>
    
    <main>
        <section class="main-section">
            <div class="container">
                <div class="category-menu">
                    <% for(int i = 0; i < categories.length; i++) { %>
                    <div class="category-item">
                        <span><%= categories[i] %></span>
                        <span class="category-arrow">></span>
                    </div>
                    <% } %>
                </div>
                
                <div class="banner-section">
                    <div class="carousel" id="carousel">
                        <div class="carousel-inner">
                            <div class="carousel-item active">
                                <img src="https://via.placeholder.com/1200x420/e1251b/ffffff?text=Banner+1+-+JD+Super+Sale" alt="Banner 1">
                            </div>
                            <div class="carousel-item">
                                <img src="https://via.placeholder.com/1200x420/ff6600/ffffff?text=Banner+2+-+Electronics+Fair" alt="Banner 2">
                            </div>
                            <div class="carousel-item">
                                <img src="https://via.placeholder.com/1200x420/0066cc/ffffff?text=Banner+3+-+Fashion+Week" alt="Banner 3">
                            </div>
                            <div class="carousel-item">
                                <img src="https://via.placeholder.com/1200x420/00cc66/ffffff?text=Banner+4+-+Fresh+Food" alt="Banner 4">
                            </div>
                            <div class="carousel-item">
                                <img src="https://via.placeholder.com/1200x420/cc0066/ffffff?text=Banner+5+-+Beauty+Zone" alt="Banner 5">
                            </div>
                        </div>
                        
                        <div class="carousel-arrow prev" onclick="prevSlide()">&#10094;</div>
                        <div class="carousel-arrow next" onclick="nextSlide()">&#10095;</div>
                        
                        <div class="carousel-indicators">
                            <div class="carousel-indicator active" onclick="goToSlide(0)"></div>
                            <div class="carousel-indicator" onclick="goToSlide(1)"></div>
                            <div class="carousel-indicator" onclick="goToSlide(2)"></div>
                            <div class="carousel-indicator" onclick="goToSlide(3)"></div>
                            <div class="carousel-indicator" onclick="goToSlide(4)"></div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        
        <section class="products-section">
            <div class="container">
                <div class="section-header">
                    <h2 class="section-title">为你推荐</h2>
                    <a href="#" class="section-more">查看更多 ></a>
                </div>
                
                <div class="products-grid">
                    <% for(int i = 0; i < products.length; i++) { 
                        Product p = products[i];
                    %>
                    <div class="product-card">
                        <div class="product-img">
                            <img src="<%= p.imageUrl %>" alt="<%= p.name %>">
                        </div>
                        <div class="product-name"><%= p.name %></div>
                        <div class="product-price">
                            <span class="price-current">¥<%= String.format("%.2f", p.price) %></span>
                            <span class="price-original">¥<%= String.format("%.2f", p.originalPrice) %></span>
                        </div>
                        <span class="product-tag"><%= p.tag %></span>
                    </div>
                    <% } %>
                </div>
            </div>
        </section>
    </main>
    
    <footer class="footer">
        <div class="container">
            <div class="footer-links">
                <a href="#">关于我们</a>
                <a href="#">联系我们</a>
                <a href="#">人才招聘</a>
                <a href="#">商家入驻</a>
                <a href="#">广告服务</a>
                <a href="#">手机京东</a>
                <a href="#">友情链接</a>
                <a href="#">销售联盟</a>
            </div>
            <div class="footer-copyright">
                <p>京东首页风格演示页面 | 仅供学习交流使用</p>
            </div>
        </div>
    </footer>
    
    <script>
        var currentSlide = 0;
        var totalSlides = 5;
        var autoPlayTimer = null;
        
        function goToSlide(index) {
            var items = document.querySelectorAll('.carousel-item');
            var indicators = document.querySelectorAll('.carousel-indicator');
            
            items[currentSlide].classList.remove('active');
            indicators[currentSlide].classList.remove('active');
            
            currentSlide = index;
            if (currentSlide >= totalSlides) currentSlide = 0;
            if (currentSlide < 0) currentSlide = totalSlides - 1;
            
            items[currentSlide].classList.add('active');
            indicators[currentSlide].classList.add('active');
        }
        
        function nextSlide() {
            goToSlide(currentSlide + 1);
        }
        
        function prevSlide() {
            goToSlide(currentSlide - 1);
        }
        
        function startAutoPlay() {
            autoPlayTimer = setInterval(function() {
                nextSlide();
            }, 3000);
        }
        
        function stopAutoPlay() {
            if (autoPlayTimer) {
                clearInterval(autoPlayTimer);
                autoPlayTimer = null;
            }
        }
        
        var carousel = document.getElementById('carousel');
        carousel.addEventListener('mouseenter', stopAutoPlay);
        carousel.addEventListener('mouseleave', startAutoPlay);
        
        startAutoPlay();
    </script>
</body>
</html>
