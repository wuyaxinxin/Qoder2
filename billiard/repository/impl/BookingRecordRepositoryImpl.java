// 始终生效
package billiard.repository.impl;

import billiard.model.BookingRecord;
import billiard.repository.BookingRecordRepository;
import java.util.*;
import java.util.stream.Collectors;

/**
 * 预订记录仓储实现类（使用内存存储）
 */
public class BookingRecordRepositoryImpl implements BookingRecordRepository {
    private final Map<String, BookingRecord> recordStore;

    public BookingRecordRepositoryImpl() {
        this.recordStore = new HashMap<>();
    }

    @Override
    public void save(BookingRecord record) {
        if (record != null && record.getBookingId() != null) {
            recordStore.put(record.getBookingId(), record);
        }
    }

    @Override
    public Optional<BookingRecord> findById(String bookingId) {
        return Optional.ofNullable(recordStore.get(bookingId));
    }

    @Override
    public List<BookingRecord> findByMemberId(String memberId) {
        return recordStore.values().stream()
                .filter(record -> record.getMemberId().equals(memberId))
                .collect(Collectors.toList());
    }

    @Override
    public List<BookingRecord> findAll() {
        return new ArrayList<>(recordStore.values());
    }

    @Override
    public List<BookingRecord> findActiveBookings() {
        return recordStore.values().stream()
                .filter(record -> !record.isCompleted())
                .collect(Collectors.toList());
    }

    @Override
    public void update(BookingRecord record) {
        if (record != null && recordStore.containsKey(record.getBookingId())) {
            recordStore.put(record.getBookingId(), record);
        }
    }

    @Override
    public boolean delete(String bookingId) {
        return recordStore.remove(bookingId) != null;
    }
}
