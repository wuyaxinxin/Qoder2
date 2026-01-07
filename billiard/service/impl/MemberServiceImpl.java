// 始终生效
package billiard.service.impl;

import billiard.model.Member;
import billiard.model.MembershipType;
import billiard.repository.MemberRepository;
import billiard.service.MemberService;
import java.util.List;
import java.util.Optional;
import java.util.UUID;

/**
 * 会员服务实现类
 */
public class MemberServiceImpl implements MemberService {
    private final MemberRepository memberRepository;

    public MemberServiceImpl(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }

    @Override
    public String registerMember(String name, String phone, String email) {
        // 检查手机号是否已注册
        Optional<Member> existingMember = memberRepository.findByPhone(phone);
        if (existingMember.isPresent()) {
            System.out.println("该手机号已注册！");
            return null;
        }

        // 生成会员ID
        String memberId = "M" + UUID.randomUUID().toString().substring(0, 8).toUpperCase();
        
        // 创建新会员
        Member newMember = new Member(memberId, name, phone, email);
        memberRepository.save(newMember);
        
        System.out.println("会员注册成功！会员ID: " + memberId);
        return memberId;
    }

    @Override
    public Member findMember(String memberId) {
        return memberRepository.findById(memberId).orElse(null);
    }

    @Override
    public boolean rechargeMember(String memberId, double amount) {
        Optional<Member> memberOpt = memberRepository.findById(memberId);
        if (memberOpt.isPresent()) {
            Member member = memberOpt.get();
            member.recharge(amount);
            memberRepository.update(member);
            System.out.println("充值成功！当前余额: " + member.getBalance());
            return true;
        }
        System.out.println("会员不存在！");
        return false;
    }

    @Override
    public boolean upgradeMembership(String memberId, MembershipType newType) {
        Optional<Member> memberOpt = memberRepository.findById(memberId);
        if (memberOpt.isPresent()) {
            Member member = memberOpt.get();
            
            // 检查余额是否足够支付年费
            int annualFee = newType.getAnnualFee();
            if (member.getBalance() < annualFee) {
                System.out.println("余额不足！需要年费: " + annualFee);
                return false;
            }
            
            // 扣除年费并升级
            member.deduct(annualFee);
            member.upgradeMembership(newType);
            memberRepository.update(member);
            
            System.out.println("升级成功！当前等级: " + newType.getName());
            return true;
        }
        System.out.println("会员不存在！");
        return false;
    }

    @Override
    public boolean deactivateMember(String memberId) {
        Optional<Member> memberOpt = memberRepository.findById(memberId);
        if (memberOpt.isPresent()) {
            Member member = memberOpt.get();
            member.setActive(false);
            memberRepository.update(member);
            System.out.println("会员已停用");
            return true;
        }
        return false;
    }

    @Override
    public boolean activateMember(String memberId) {
        Optional<Member> memberOpt = memberRepository.findById(memberId);
        if (memberOpt.isPresent()) {
            Member member = memberOpt.get();
            member.setActive(true);
            memberRepository.update(member);
            System.out.println("会员已激活");
            return true;
        }
        return false;
    }

    @Override
    public List<Member> getAllMembers() {
        return memberRepository.findAll();
    }

    @Override
    public Member findMemberByPhone(String phone) {
        return memberRepository.findByPhone(phone).orElse(null);
    }

    @Override
    public double getMemberBalance(String memberId) {
        Optional<Member> memberOpt = memberRepository.findById(memberId);
        return memberOpt.map(Member::getBalance).orElse(0.0);
    }
}
