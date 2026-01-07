// 始终生效
package billiard;

import billiard.model.BookingRecord;
import billiard.model.Member;
import billiard.model.MembershipType;
import billiard.repository.BookingRecordRepository;
import billiard.repository.MemberRepository;
import billiard.repository.impl.BookingRecordRepositoryImpl;
import billiard.repository.impl.MemberRepositoryImpl;
import billiard.service.BookingService;
import billiard.service.MemberService;
import billiard.service.impl.BookingServiceImpl;
import billiard.service.impl.MemberServiceImpl;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.List;
import java.util.Scanner;

/**
 * 台球俱乐部会员管理系统主类
 */
public class BilliardClubSystem {
    private final MemberService memberService;
    private final BookingService bookingService;
    private final Scanner scanner;
    private final DateTimeFormatter formatter;

    public BilliardClubSystem() {
        // 初始化仓储
        MemberRepository memberRepository = new MemberRepositoryImpl();
        BookingRecordRepository bookingRepository = new BookingRecordRepositoryImpl();
        
        // 初始化服务
        this.memberService = new MemberServiceImpl(memberRepository);
        this.bookingService = new BookingServiceImpl(bookingRepository, memberRepository);
        this.scanner = new Scanner(System.in);
        this.formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");
    }

    public void start() {
        System.out.println("========================================");
        System.out.println("    欢迎使用台球俱乐部会员管理系统");
        System.out.println("========================================");
        
        boolean running = true;
        while (running) {
            showMainMenu();
            int choice = getIntInput("请选择操作: ");
            
            switch (choice) {
                case 1:
                    memberManagementMenu();
                    break;
                case 2:
                    bookingManagementMenu();
                    break;
                case 3:
                    queryMenu();
                    break;
                case 0:
                    running = false;
                    System.out.println("感谢使用，再见！");
                    break;
                default:
                    System.out.println("无效选项，请重试！");
            }
        }
        scanner.close();
    }

    private void showMainMenu() {
        System.out.println("\n========== 主菜单 ==========");
        System.out.println("1. 会员管理");
        System.out.println("2. 预订管理");
        System.out.println("3. 查询统计");
        System.out.println("0. 退出系统");
        System.out.println("============================");
    }

    private void memberManagementMenu() {
        while (true) {
            System.out.println("\n========== 会员管理 ==========");
            System.out.println("1. 注册新会员");
            System.out.println("2. 会员充值");
            System.out.println("3. 升级会员等级");
            System.out.println("4. 查看会员信息");
            System.out.println("5. 激活/停用会员");
            System.out.println("0. 返回主菜单");
            System.out.println("==============================");
            
            int choice = getIntInput("请选择操作: ");
            
            switch (choice) {
                case 1:
                    registerNewMember();
                    break;
                case 2:
                    rechargeMember();
                    break;
                case 3:
                    upgradeMembership();
                    break;
                case 4:
                    viewMemberInfo();
                    break;
                case 5:
                    toggleMemberStatus();
                    break;
                case 0:
                    return;
                default:
                    System.out.println("无效选项，请重试！");
            }
        }
    }

    private void bookingManagementMenu() {
        while (true) {
            System.out.println("\n========== 预订管理 ==========");
            System.out.println("1. 创建新预订");
            System.out.println("2. 完成预订并结算");
            System.out.println("3. 取消预订");
            System.out.println("4. 查看预订详情");
            System.out.println("0. 返回主菜单");
            System.out.println("==============================");
            
            int choice = getIntInput("请选择操作: ");
            
            switch (choice) {
                case 1:
                    createNewBooking();
                    break;
                case 2:
                    completeBooking();
                    break;
                case 3:
                    cancelBooking();
                    break;
                case 4:
                    viewBookingDetails();
                    break;
                case 0:
                    return;
                default:
                    System.out.println("无效选项，请重试！");
            }
        }
    }

    private void queryMenu() {
        while (true) {
            System.out.println("\n========== 查询统计 ==========");
            System.out.println("1. 查看所有会员");
            System.out.println("2. 查看会员预订记录");
            System.out.println("3. 查看所有活动预订");
            System.out.println("4. 查看所有预订记录");
            System.out.println("0. 返回主菜单");
            System.out.println("==============================");
            
            int choice = getIntInput("请选择操作: ");
            
            switch (choice) {
                case 1:
                    viewAllMembers();
                    break;
                case 2:
                    viewMemberBookings();
                    break;
                case 3:
                    viewActiveBookings();
                    break;
                case 4:
                    viewAllBookings();
                    break;
                case 0:
                    return;
                default:
                    System.out.println("无效选项，请重试！");
            }
        }
    }

    // 会员管理功能实现
    private void registerNewMember() {
        System.out.println("\n--- 注册新会员 ---");
        String name = getStringInput("姓名: ");
        String phone = getStringInput("手机号: ");
        String email = getStringInput("邮箱: ");
        
        String memberId = memberService.registerMember(name, phone, email);
        if (memberId != null) {
            System.out.println("注册成功！会员ID: " + memberId);
        }
    }

    private void rechargeMember() {
        System.out.println("\n--- 会员充值 ---");
        String memberId = getStringInput("会员ID: ");
        double amount = getDoubleInput("充值金额: ");
        
        memberService.rechargeMember(memberId, amount);
    }

    private void upgradeMembership() {
        System.out.println("\n--- 升级会员等级 ---");
        String memberId = getStringInput("会员ID: ");
        
        System.out.println("可选等级:");
        System.out.println("1. 银卡会员 (年费: 500, 折扣: 10%)");
        System.out.println("2. 金卡会员 (年费: 1000, 折扣: 20%)");
        System.out.println("3. 白金会员 (年费: 2000, 折扣: 30%)");
        
        int choice = getIntInput("选择等级: ");
        MembershipType newType = null;
        
        switch (choice) {
            case 1:
                newType = MembershipType.SILVER;
                break;
            case 2:
                newType = MembershipType.GOLD;
                break;
            case 3:
                newType = MembershipType.PLATINUM;
                break;
            default:
                System.out.println("无效选择！");
                return;
        }
        
        memberService.upgradeMembership(memberId, newType);
    }

    private void viewMemberInfo() {
        System.out.println("\n--- 查看会员信息 ---");
        String memberId = getStringInput("会员ID: ");
        Member member = memberService.findMember(memberId);
        
        if (member != null) {
            System.out.println("\n会员详情:");
            System.out.println(member);
            System.out.println("加入日期: " + member.getJoinDate());
            System.out.println("会员到期日: " + member.getMembershipExpiryDate());
            System.out.println("总预订次数: " + member.getTotalBookings());
        } else {
            System.out.println("会员不存在！");
        }
    }

    private void toggleMemberStatus() {
        System.out.println("\n--- 激活/停用会员 ---");
        String memberId = getStringInput("会员ID: ");
        Member member = memberService.findMember(memberId);
        
        if (member != null) {
            System.out.println("当前状态: " + (member.isActive() ? "激活" : "未激活"));
            int choice = getIntInput("1-激活 2-停用: ");
            
            if (choice == 1) {
                memberService.activateMember(memberId);
            } else if (choice == 2) {
                memberService.deactivateMember(memberId);
            }
        } else {
            System.out.println("会员不存在！");
        }
    }

    // 预订管理功能实现
    private void createNewBooking() {
        System.out.println("\n--- 创建新预订 ---");
        String memberId = getStringInput("会员ID: ");
        int tableNumber = getIntInput("球桌编号: ");
        
        System.out.println("开始时间 (格式: yyyy-MM-dd HH:mm)");
        String startTimeStr = getStringInput("开始时间: ");
        System.out.println("结束时间 (格式: yyyy-MM-dd HH:mm)");
        String endTimeStr = getStringInput("结束时间: ");
        
        try {
            LocalDateTime startTime = LocalDateTime.parse(startTimeStr, formatter);
            LocalDateTime endTime = LocalDateTime.parse(endTimeStr, formatter);
            
            String bookingId = bookingService.createBooking(memberId, tableNumber, startTime, endTime);
            if (bookingId != null) {
                System.out.println("预订成功！预订ID: " + bookingId);
            }
        } catch (Exception e) {
            System.out.println("时间格式错误！");
        }
    }

    private void completeBooking() {
        System.out.println("\n--- 完成预订并结算 ---");
        String bookingId = getStringInput("预订ID: ");
        bookingService.completeBooking(bookingId);
    }

    private void cancelBooking() {
        System.out.println("\n--- 取消预订 ---");
        String bookingId = getStringInput("预订ID: ");
        bookingService.cancelBooking(bookingId);
    }

    private void viewBookingDetails() {
        System.out.println("\n--- 查看预订详情 ---");
        String bookingId = getStringInput("预订ID: ");
        BookingRecord booking = bookingService.getBookingDetails(bookingId);
        
        if (booking != null) {
            System.out.println("\n预订详情:");
            System.out.println(booking);
            System.out.println("备注: " + booking.getRemarks());
        } else {
            System.out.println("预订不存在！");
        }
    }

    // 查询统计功能实现
    private void viewAllMembers() {
        System.out.println("\n========== 所有会员 ==========");
        List<Member> members = memberService.getAllMembers();
        
        if (members.isEmpty()) {
            System.out.println("暂无会员");
        } else {
            for (Member member : members) {
                System.out.println(member);
            }
            System.out.println("总计: " + members.size() + " 位会员");
        }
    }

    private void viewMemberBookings() {
        System.out.println("\n--- 查看会员预订记录 ---");
        String memberId = getStringInput("会员ID: ");
        List<BookingRecord> bookings = bookingService.getMemberBookings(memberId);
        
        if (bookings.isEmpty()) {
            System.out.println("该会员暂无预订记录");
        } else {
            for (BookingRecord booking : bookings) {
                System.out.println(booking);
            }
            System.out.println("总计: " + bookings.size() + " 条记录");
        }
    }

    private void viewActiveBookings() {
        System.out.println("\n========== 活动预订 ==========");
        List<BookingRecord> bookings = bookingService.getActiveBookings();
        
        if (bookings.isEmpty()) {
            System.out.println("暂无活动预订");
        } else {
            for (BookingRecord booking : bookings) {
                System.out.println(booking);
            }
            System.out.println("总计: " + bookings.size() + " 条记录");
        }
    }

    private void viewAllBookings() {
        System.out.println("\n========== 所有预订记录 ==========");
        List<BookingRecord> bookings = bookingService.getAllBookings();
        
        if (bookings.isEmpty()) {
            System.out.println("暂无预订记录");
        } else {
            for (BookingRecord booking : bookings) {
                System.out.println(booking);
            }
            System.out.println("总计: " + bookings.size() + " 条记录");
        }
    }

    // 输入工具方法
    private String getStringInput(String prompt) {
        System.out.print(prompt);
        return scanner.nextLine().trim();
    }

    private int getIntInput(String prompt) {
        while (true) {
            try {
                System.out.print(prompt);
                String input = scanner.nextLine().trim();
                return Integer.parseInt(input);
            } catch (NumberFormatException e) {
                System.out.println("请输入有效的数字！");
            }
        }
    }

    private double getDoubleInput(String prompt) {
        while (true) {
            try {
                System.out.print(prompt);
                String input = scanner.nextLine().trim();
                return Double.parseDouble(input);
            } catch (NumberFormatException e) {
                System.out.println("请输入有效的数字！");
            }
        }
    }

    public static void main(String[] args) {
        BilliardClubSystem system = new BilliardClubSystem();
        system.start();
    }
}
