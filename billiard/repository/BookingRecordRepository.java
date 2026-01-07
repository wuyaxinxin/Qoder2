// 始终生效
package billiard.repository;

import billiard.model.BookingRecord;
import java.util.List;
import java.util.Optional;

/**
 * 预订记录仓储接口
 */
public interface BookingRecordRepository {
    /**
     * 保存预订记录
     */
    void save(BookingRecord record);

    /**
     * 根据ID查找预订记录
     */
    Optional<BookingRecord> findById(String bookingId);

    /**
     * 根据会员ID查找所有预订记录
     */
    List<BookingRecord> findByMemberId(String memberId);

    /**
     * 获取所有预订记录
     */
    List<BookingRecord> findAll();

    /**
     * 获取所有未完成的预订记录
     */
    List<BookingRecord> findActiveBookings();

    /**
     * 更新预订记录
     */
    void update(BookingRecord record);

    /**
     * 删除预订记录
     */
    boolean delete(String bookingId);
}
