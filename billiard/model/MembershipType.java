// 始终生效
package billiard.model;

/**
 * 会员类型枚举
 */
public enum MembershipType {
    REGULAR("普通会员", 0, 0.0, 0),
    SILVER("银卡会员", 500, 0.1, 2),
    GOLD("金卡会员", 1000, 0.2, 5),
    PLATINUM("白金会员", 2000, 0.3, 10);

    private final String name;
    private final int annualFee; // 年费
    private final double discount; // 折扣率
    private final int priorityBookingHours; // 优先预订时长（小时）

    MembershipType(String name, int annualFee, double discount, int priorityBookingHours) {
        this.name = name;
        this.annualFee = annualFee;
        this.discount = discount;
        this.priorityBookingHours = priorityBookingHours;
    }

    public String getName() {
        return name;
    }

    public int getAnnualFee() {
        return annualFee;
    }

    public double getDiscount() {
        return discount;
    }

    public int getPriorityBookingHours() {
        return priorityBookingHours;
    }
}
