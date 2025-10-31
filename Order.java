/*
 * 文件名: Order.java
 * 作者: 开发者
 * 创建日期: 2025-10-27
 * 版本: 1.0
 * 描述: 这是一个表示订单信息的Java类文件
 *       包含订单的基本信息和相关操作方法
 * 功能:
 *   - 存储和管理订单基本信息
 *   - 提供标准的getter/setter方法
 *   - 实现订单相关的操作方法
 *   - 重写equals、hashCode和toString方法
 * 依赖: 需要Product类支持,使用Java标准库
 * 修改记录:
 *   2025-10-27 - 初始版本创建
 * 水月洞天
 */

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

/**
 * Order类 - 表示一个订单的基本信息
 */
public class Order {
    private String orderId;
    private String customerId;
    private LocalDateTime orderDate;
    private List<OrderItem> orderItems;
    private double totalAmount;
    private String status; // pending, confirmed, shipped, delivered, cancelled
    
    /**
     * 默认构造函数
     */
    public Order() {
        this.orderId = "";
        this.customerId = "";
        this.orderDate = LocalDateTime.now();
        this.orderItems = new ArrayList<>();
        this.totalAmount = 0.0;
        this.status = "pending";
    }
    
    /**
     * 带参数的构造函数
     * @param orderId 订单ID
     * @param customerId 客户ID
     */
    public Order(String orderId, String customerId) {
        this.orderId = orderId;
        this.customerId = customerId;
        this.orderDate = LocalDateTime.now();
        this.orderItems = new ArrayList<>();
        this.totalAmount = 0.0;
        this.status = "pending";
    }
    
    /**
     * 获取订单ID
     * @return 订单ID
     */
    public String getOrderId() {
        return orderId;
    }
    
    /**
     * 设置订单ID
     * @param orderId 订单ID
     */
    public void setOrderId(String orderId) {
        this.orderId = orderId;
    }
    
    /**
     * 获取客户ID
     * @return 客户ID
     */
    public String getCustomerId() {
        return customerId;
    }
    
    /**
     * 设置客户ID
     * @param customerId 客户ID
     */
    public void setCustomerId(String customerId) {
        this.customerId = customerId;
    }
    
    /**
     * 获取订单日期
     * @return 订单日期
     */
    public LocalDateTime getOrderDate() {
        return orderDate;
    }
    
    /**
     * 设置订单日期
     * @param orderDate 订单日期
     */
    public void setOrderDate(LocalDateTime orderDate) {
        this.orderDate = orderDate;
    }
    
    /**
     * 获取订单项列表
     * @return 订单项列表
     */
    public List<OrderItem> getOrderItems() {
        return new ArrayList<>(orderItems);
    }
    
    /**
     * 获取订单总金额
     * @return 订单总金额
     */
    public double getTotalAmount() {
        return totalAmount;
    }
    
    /**
     * 获取订单状态
     * @return 订单状态
     */
    public String getStatus() {
        return status;
    }
    
    /**
     * 设置订单状态
     * @param status 订单状态
     */
    public void setStatus(String status) {
        this.status = status;
    }
    
    /**
     * 添加订单项
     * @param product 商品
     * @param quantity 数量
     * @return 如果添加成功返回true，否则返回false
     */
    public boolean addOrderItem(Product product, int quantity) {
        if (product == null || quantity <= 0) {
            return false;
        }
        
        // 检查是否已存在相同商品的订单项
        for (OrderItem item : orderItems) {
            if (item.getProduct().getProductId().equals(product.getProductId())) {
                // 更新数量和小计
                item.setQuantity(item.getQuantity() + quantity);
                item.setSubtotal(item.getPrice() * item.getQuantity());
                calculateTotalAmount();
                return true;
            }
        }
        
        // 添加新的订单项
        OrderItem newItem = new OrderItem(product, quantity);
        orderItems.add(newItem);
        calculateTotalAmount();
        return true;
    }
    
    /**
     * 移除订单项
     * @param productId 商品ID
     * @return 如果移除成功返回true，否则返回false
     */
    public boolean removeOrderItem(String productId) {
        if (productId == null || productId.isEmpty()) {
            return false;
        }
        
        for (int i = 0; i < orderItems.size(); i++) {
            if (orderItems.get(i).getProduct().getProductId().equals(productId)) {
                orderItems.remove(i);
                calculateTotalAmount();
                return true;
            }
        }
        return false;
    }
    
    /**
     * 更新订单项数量
     * @param productId 商品ID
     * @param quantity 新数量
     * @return 如果更新成功返回true，否则返回false
     */
    public boolean updateOrderItemQuantity(String productId, int quantity) {
        if (productId == null || productId.isEmpty() || quantity < 0) {
            return false;
        }
        
        for (OrderItem item : orderItems) {
            if (item.getProduct().getProductId().equals(productId)) {
                if (quantity == 0) {
                    // 如果数量为0，则移除订单项
                    return removeOrderItem(productId);
                } else {
                    // 更新数量和小计
                    item.setQuantity(quantity);
                    item.setSubtotal(item.getPrice() * quantity);
                    calculateTotalAmount();
                    return true;
                }
            }
        }
        return false;
    }
    
    /**
     * 计算订单总金额
     */
    private void calculateTotalAmount() {
        totalAmount = 0.0;
        for (OrderItem item : orderItems) {
            totalAmount += item.getSubtotal();
        }
    }
    
    /**
     * 获取订单项数量
     * @return 订单项数量
     */
    public int getOrderItemCount() {
        return orderItems.size();
    }
    
    /**
     * 确认订单
     * @return 如果确认成功返回true，否则返回false
     */
    public boolean confirmOrder() {
        if (!orderItems.isEmpty() && "pending".equals(status)) {
            status = "confirmed";
            return true;
        }
        return false;
    }
    
    /**
     * 发货订单
     * @return 如果发货成功返回true，否则返回false
     */
    public boolean shipOrder() {
        if ("confirmed".equals(status)) {
            status = "shipped";
            return true;
        }
        return false;
    }
    
    /**
     * 完成订单
     * @return 如果完成成功返回true，否则返回false
     */
    public boolean deliverOrder() {
        if ("shipped".equals(status)) {
            status = "delivered";
            return true;
        }
        return false;
    }
    
    /**
     * 取消订单
     * @return 如果取消成功返回true，否则返回false
     */
    public boolean cancelOrder() {
        if ("pending".equals(status) || "confirmed".equals(status)) {
            status = "cancelled";
            return true;
        }
        return false;
    }
    
    /**
     * 获取订单信息描述
     * @return 订单信息字符串
     */
    public String getOrderDescription() {
        return String.format("订单ID: %s, 客户ID: %s, 订单日期: %s, 总金额: %.2f元, 状态: %s, 商品数量: %d", 
                           orderId, customerId, orderDate.toString(), totalAmount, status, getOrderItemCount());
    }
    
    @Override
    public String toString() {
        return "Order{" +
                "orderId='" + orderId + '\'' +
                ", customerId='" + customerId + '\'' +
                ", orderDate=" + orderDate +
                ", orderItems=" + orderItems.size() +
                ", totalAmount=" + totalAmount +
                ", status='" + status + '\'' +
                '}';
    }
    
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Order order = (Order) obj;
        return orderId.equals(order.orderId);
    }
    
    @Override
    public int hashCode() {
        return orderId.hashCode();
    }
    
    /**
     * OrderItem内部类 - 表示订单中的单项商品
     */
    public static class OrderItem {
        private Product product;
        private int quantity;
        private double price;
        private double subtotal;
        
        /**
         * 默认构造函数
         */
        public OrderItem() {
            this.product = null;
            this.quantity = 0;
            this.price = 0.0;
            this.subtotal = 0.0;
        }
        
        /**
         * 带参数的构造函数
         * @param product 商品
         * @param quantity 数量
         */
        public OrderItem(Product product, int quantity) {
            this.product = product;
            this.quantity = quantity;
            this.price = product.getPrice();
            this.subtotal = this.price * quantity;
        }
        
        /**
         * 获取商品
         * @return 商品
         */
        public Product getProduct() {
            return product;
        }
        
        /**
         * 设置商品
         * @param product 商品
         */
        public void setProduct(Product product) {
            this.product = product;
            if (product != null) {
                this.price = product.getPrice();
                this.subtotal = this.price * this.quantity;
            }
        }
        
        /**
         * 获取数量
         * @return 数量
         */
        public int getQuantity() {
            return quantity;
        }
        
        /**
         * 设置数量
         * @param quantity 数量
         */
        public void setQuantity(int quantity) {
            this.quantity = quantity;
            this.subtotal = this.price * quantity;
        }
        
        /**
         * 获取单价
         * @return 单价
         */
        public double getPrice() {
            return price;
        }
        
        /**
         * 获取小计
         * @return 小计
         */
        public double getSubtotal() {
            return subtotal;
        }
        
        /**
         * 设置小计
         * @param subtotal 小计
         */
        public void setSubtotal(double subtotal) {
            this.subtotal = subtotal;
        }
        
        @Override
        public String toString() {
            return "OrderItem{" +
                    "product=" + (product != null ? product.getProductName() : "null") +
                    ", quantity=" + quantity +
                    ", price=" + price +
                    ", subtotal=" + subtotal +
                    '}';
        }
    }
}