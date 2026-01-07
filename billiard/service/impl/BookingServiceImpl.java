// 始终生效
package billiard.service.impl;

import billiard.model.BookingRecord;
import billiard.model.Member;
import billiard.repository.BookingRecordRepository;
import billiard.repository.MemberRepository;
import billiard.service.BookingService;
import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;
import java.util.UUID;

/**
 * 预订服务实现类
 */
public class BookingServiceImpl implements BookingService {
    private final BookingRecordRepository bookingRepository;
    private final MemberRepository memberRepository;
    private static final double HOURLY_RATE = 80.0; // 默认每小时费用

    public BookingServiceImpl(BookingRecordRepository bookingRepository, MemberRepository memberRepository) {
        this.bookingRepository = bookingRepository;
        this.memberRepository = memberRepository;
    }

    @Override
    public String createBooking(String memberId, int tableNumber, LocalDateTime startTime, LocalDateTime endTime) {
        // 验证会员
        Optional<Member> memberOpt = memberRepository.findById(memberId);
        if (!memberOpt.isPresent()) {
            System.out.println("会员不存在！");
            return null;
        }

        Member member = memberOpt.get();
        if (!member.isActive()) {
            System.out.println("会员未激活，无法预订！");
            return null;
        }

        // 验证时间
        if (startTime.isAfter(endTime)) {
            System.out.println("开始时间不能晚于结束时间！");
            return null;
        }

        // 生成预订ID
        String bookingId = "B" + UUID.randomUUID().toString().substring(0, 8).toUpperCase();
        
        // 创建预订记录
        BookingRecord booking = new BookingRecord(bookingId, memberId, tableNumber, 
                                                   startTime, endTime, HOURLY_RATE);
        bookingRepository.save(booking);
        
        // 更新会员预订次数
        member.setTotalBookings(member.getTotalBookings() + 1);
        memberRepository.update(member);
        
        System.out.println("预订成功！预订ID: " + bookingId);
        return bookingId;
    }

    @Override
    public boolean completeBooking(String bookingId) {
        Optional<BookingRecord> bookingOpt = bookingRepository.findById(bookingId);
        if (!bookingOpt.isPresent()) {
            System.out.println("预订记录不存在！");
            return false;
        }

        BookingRecord booking = bookingOpt.get();
        if (booking.isCompleted()) {
            System.out.println("预订已完成！");
            return false;
        }

        // 获取会员信息以应用折扣
        Optional<Member> memberOpt = memberRepository.findById(booking.getMemberId());
        if (!memberOpt.isPresent()) {
            System.out.println("会员不存在！");
            return false;
        }

        Member member = memberOpt.get();
        double discount = member.getMembershipType().getDiscount();
        
        // 完成预订并计算费用
        booking.completeBooking(discount);
        
        // 从会员余额扣费
        if (!member.deduct(booking.getTotalCost())) {
            System.out.println("余额不足！需要: " + booking.getTotalCost() + ", 当前余额: " + member.getBalance());
            return false;
        }
        
        // 更新记录
        bookingRepository.update(booking);
        memberRepository.update(member);
        
        System.out.println("预订已完成！费用: " + booking.getTotalCost() + ", 剩余余额: " + member.getBalance());
        return true;
    }

    @Override
    public boolean cancelBooking(String bookingId) {
        Optional<BookingRecord> bookingOpt = bookingRepository.findById(bookingId);
        if (!bookingOpt.isPresent()) {
            System.out.println("预订记录不存在！");
            return false;
        }

        BookingRecord booking = bookingOpt.get();
        if (booking.isCompleted()) {
            System.out.println("预订已完成，无法取消！");
            return false;
        }

        bookingRepository.delete(bookingId);
        System.out.println("预订已取消");
        return true;
    }

    @Override
    public List<BookingRecord> getMemberBookings(String memberId) {
        return bookingRepository.findByMemberId(memberId);
    }

    @Override
    public List<BookingRecord> getActiveBookings() {
        return bookingRepository.findActiveBookings();
    }

    @Override
    public List<BookingRecord> getAllBookings() {
        return bookingRepository.findAll();
    }

    @Override
    public BookingRecord getBookingDetails(String bookingId) {
        return bookingRepository.findById(bookingId).orElse(null);
    }
}
