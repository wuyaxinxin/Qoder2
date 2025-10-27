/*
 * 文件名: Product.java
 * 作者: 开发者
 * 创建日期: 2025-10-27
 * 版本: 1.0
 * 描述: 这是一个表示商品信息的Java类文件
 *       包含商品的基本信息和相关操作方法
 * 功能:
 *   - 存储和管理商品基本信息
 *   - 提供标准的getter/setter方法
 *   - 实现商品相关操作方法
 *   - 重写equals、hashCode和toString方法
 * 依赖: 无外部依赖,仅使用Java标准库
 * 修改记录:
 *   2025-10-27 - 初始版本创建
 */

/**
 * Product类 - 表示一个商品的基本信息
 */
public class Product {
    private String productId;
    private String productName;
    private String category;
    private double price;
    private int stockQuantity;
    private String description;
    
    /**
     * 默认构造函数
     */
    public Product() {
        this.productId = "";
        this.productName = "";
        this.category = "";
        this.price = 0.0;
        this.stockQuantity = 0;
        this.description = "";
    }
    
    /**
     * 带参数的构造函数
     * @param productId 商品ID
     * @param productName 商品名称
     * @param category 商品类别
     * @param price 价格
     * @param stockQuantity 库存数量
     * @param description 商品描述
     */
    public Product(String productId, String productName, String category, 
                   double price, int stockQuantity, String description) {
        this.productId = productId;
        this.productName = productName;
        this.category = category;
        this.price = price;
        this.stockQuantity = stockQuantity;
        this.description = description;
    }
    
    /**
     * 获取商品ID
     * @return 商品ID
     */
    public String getProductId() {
        return productId;
    }
    
    /**
     * 设置商品ID
     * @param productId 商品ID
     */
    public void setProductId(String productId) {
        this.productId = productId;
    }
    
    /**
     * 获取商品名称
     * @return 商品名称
     */
    public String getProductName() {
        return productName;
    }
    
    /**
     * 设置商品名称
     * @param productName 商品名称
     */
    public void setProductName(String productName) {
        this.productName = productName;
    }
    
    /**
     * 获取商品类别
     * @return 商品类别
     */
    public String getCategory() {
        return category;
    }
    
    /**
     * 设置商品类别
     * @param category 商品类别
     */
    public void setCategory(String category) {
        this.category = category;
    }
    
    /**
     * 获取价格
     * @return 价格
     */
    public double getPrice() {
        return price;
    }
    
    /**
     * 设置价格
     * @param price 价格
     */
    public void setPrice(double price) {
        if (price >= 0) {
            this.price = price;
        }
    }
    
    /**
     * 获取库存数量
     * @return 库存数量
     */
    public int getStockQuantity() {
        return stockQuantity;
    }
    
    /**
     * 设置库存数量
     * @param stockQuantity 库存数量
     */
    public void setStockQuantity(int stockQuantity) {
        if (stockQuantity >= 0) {
            this.stockQuantity = stockQuantity;
        }
    }
    
    /**
     * 获取商品描述
     * @return 商品描述
     */
    public String getDescription() {
        return description;
    }
    
    /**
     * 设置商品描述
     * @param description 商品描述
     */
    public void setDescription(String description) {
        this.description = description;
    }
    
    /**
     * 检查商品是否有库存
     * @return 如果有库存返回true，否则返回false
     */
    public boolean isInStock() {
        return stockQuantity > 0;
    }
    
    /**
     * 减少库存数量
     * @param quantity 要减少的数量
     * @return 如果减少成功返回true，否则返回false
     */
    public boolean reduceStock(int quantity) {
        if (quantity > 0 && quantity <= stockQuantity) {
            stockQuantity -= quantity;
            return true;
        }
        return false;
    }
    
    /**
     * 增加库存数量
     * @param quantity 要增加的数量
     * @return 如果增加成功返回true，否则返回false
     */
    public boolean addStock(int quantity) {
        if (quantity > 0) {
            stockQuantity += quantity;
            return true;
        }
        return false;
    }
    
    /**
     * 获取商品信息描述
     * @return 商品信息字符串
     */
    public String getProductDescription() {
        return String.format("商品ID: %s, 商品名称: %s, 类别: %s, 价格: %.2f元, 库存: %d", 
                           productId, productName, category, price, stockQuantity);
    }
    
    @Override
    public String toString() {
        return "Product{" +
                "productId='" + productId + '\'' +
                ", productName='" + productName + '\'' +
                ", category='" + category + '\'' +
                ", price=" + price +
                ", stockQuantity=" + stockQuantity +
                ", description='" + description + '\'' +
                '}';
    }
    
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Product product = (Product) obj;
        return productId.equals(product.productId);
    }
    
    @Override
    public int hashCode() {
        return productId.hashCode();
    }
}