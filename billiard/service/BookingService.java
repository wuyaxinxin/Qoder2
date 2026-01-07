// 始终生效
package billiard.service;

import billiard.model.BookingRecord;
import java.time.LocalDateTime;
import java.util.List;

/**
 * 预订服务接口
 */
public interface BookingService {
    /**
     * 创建预订
     */
    String createBooking(String memberId, int tableNumber, LocalDateTime startTime, LocalDateTime endTime);

    /**
     * 完成预订并结算
     */
    boolean completeBooking(String bookingId);

    /**
     * 取消预订
     */
    boolean cancelBooking(String bookingId);

    /**
     * 查询会员的所有预订记录
     */
    List<BookingRecord> getMemberBookings(String memberId);

    /**
     * 查询所有活动预订
     */
    List<BookingRecord> getActiveBookings();

    /**
     * 查询所有预订记录
     */
    List<BookingRecord> getAllBookings();

    /**
     * 查询预订详情
     */
    BookingRecord getBookingDetails(String bookingId);
}
