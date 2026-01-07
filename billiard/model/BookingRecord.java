// 始终生效
package billiard.model;

import java.time.LocalDateTime;

/**
 * 预订记录类
 */
public class BookingRecord {
    private String bookingId;
    private String memberId;
    private int tableNumber; // 球桌编号
    private LocalDateTime startTime;
    private LocalDateTime endTime;
    private double hourlyRate; // 每小时费用
    private double totalCost; // 总费用
    private boolean completed; // 是否完成
    private String remarks; // 备注

    public BookingRecord(String bookingId, String memberId, int tableNumber,
                         LocalDateTime startTime, LocalDateTime endTime, double hourlyRate) {
        this.bookingId = bookingId;
        this.memberId = memberId;
        this.tableNumber = tableNumber;
        this.startTime = startTime;
        this.endTime = endTime;
        this.hourlyRate = hourlyRate;
        this.totalCost = 0.0;
        this.completed = false;
        this.remarks = "";
    }

    // Getters and Setters
    public String getBookingId() {
        return bookingId;
    }

    public void setBookingId(String bookingId) {
        this.bookingId = bookingId;
    }

    public String getMemberId() {
        return memberId;
    }

    public void setMemberId(String memberId) {
        this.memberId = memberId;
    }

    public int getTableNumber() {
        return tableNumber;
    }

    public void setTableNumber(int tableNumber) {
        this.tableNumber = tableNumber;
    }

    public LocalDateTime getStartTime() {
        return startTime;
    }

    public void setStartTime(LocalDateTime startTime) {
        this.startTime = startTime;
    }

    public LocalDateTime getEndTime() {
        return endTime;
    }

    public void setEndTime(LocalDateTime endTime) {
        this.endTime = endTime;
    }

    public double getHourlyRate() {
        return hourlyRate;
    }

    public void setHourlyRate(double hourlyRate) {
        this.hourlyRate = hourlyRate;
    }

    public double getTotalCost() {
        return totalCost;
    }

    public void setTotalCost(double totalCost) {
        this.totalCost = totalCost;
    }

    public boolean isCompleted() {
        return completed;
    }

    public void setCompleted(boolean completed) {
        this.completed = completed;
    }

    public String getRemarks() {
        return remarks;
    }

    public void setRemarks(String remarks) {
        this.remarks = remarks;
    }

    // 计算使用时长（小时）
    public double calculateHours() {
        long minutes = java.time.Duration.between(startTime, endTime).toMinutes();
        return Math.ceil(minutes / 60.0);
    }

    // 完成预订并计算总费用
    public void completeBooking(double discount) {
        double hours = calculateHours();
        this.totalCost = hours * hourlyRate * (1 - discount);
        this.completed = true;
    }

    @Override
    public String toString() {
        return String.format("预订ID: %s | 会员ID: %s | 球桌: %d | 开始: %s | 结束: %s | 费用: %.2f | 状态: %s",
                bookingId, memberId, tableNumber, startTime, endTime, totalCost, completed ? "已完成" : "进行中");
    }
}
