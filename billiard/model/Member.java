// 始终生效
package billiard.model;

import java.time.LocalDate;

/**
 * 会员类
 */
public class Member {
    private String memberId;
    private String name;
    private String phone;
    private String email;
    private MembershipType membershipType;
    private LocalDate joinDate;
    private LocalDate membershipExpiryDate;
    private double balance; // 账户余额
    private int totalBookings; // 总预订次数
    private boolean active; // 是否激活

    public Member(String memberId, String name, String phone, String email) {
        this.memberId = memberId;
        this.name = name;
        this.phone = phone;
        this.email = email;
        this.membershipType = MembershipType.REGULAR;
        this.joinDate = LocalDate.now();
        this.membershipExpiryDate = LocalDate.now().plusYears(1);
        this.balance = 0.0;
        this.totalBookings = 0;
        this.active = true;
    }

    // Getters and Setters
    public String getMemberId() {
        return memberId;
    }

    public void setMemberId(String memberId) {
        this.memberId = memberId;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public MembershipType getMembershipType() {
        return membershipType;
    }

    public void setMembershipType(MembershipType membershipType) {
        this.membershipType = membershipType;
    }

    public LocalDate getJoinDate() {
        return joinDate;
    }

    public void setJoinDate(LocalDate joinDate) {
        this.joinDate = joinDate;
    }

    public LocalDate getMembershipExpiryDate() {
        return membershipExpiryDate;
    }

    public void setMembershipExpiryDate(LocalDate membershipExpiryDate) {
        this.membershipExpiryDate = membershipExpiryDate;
    }

    public double getBalance() {
        return balance;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }

    public int getTotalBookings() {
        return totalBookings;
    }

    public void setTotalBookings(int totalBookings) {
        this.totalBookings = totalBookings;
    }

    public boolean isActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }

    // 充值
    public void recharge(double amount) {
        if (amount > 0) {
            this.balance += amount;
        }
    }

    // 扣费
    public boolean deduct(double amount) {
        if (amount > 0 && this.balance >= amount) {
            this.balance -= amount;
            return true;
        }
        return false;
    }

    // 升级会员
    public void upgradeMembership(MembershipType newType) {
        this.membershipType = newType;
        this.membershipExpiryDate = LocalDate.now().plusYears(1);
    }

    // 检查会员是否过期
    public boolean isExpired() {
        return LocalDate.now().isAfter(membershipExpiryDate);
    }

    @Override
    public String toString() {
        return String.format("会员ID: %s | 姓名: %s | 等级: %s | 余额: %.2f | 状态: %s",
                memberId, name, membershipType.getName(), balance, active ? "激活" : "未激活");
    }
}
