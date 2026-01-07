// 始终生效
package billiard.service;

import billiard.model.Member;
import billiard.model.MembershipType;
import java.util.List;

/**
 * 会员服务接口
 */
public interface MemberService {
    /**
     * 注册新会员
     */
    String registerMember(String name, String phone, String email);

    /**
     * 查找会员
     */
    Member findMember(String memberId);

    /**
     * 会员充值
     */
    boolean rechargeMember(String memberId, double amount);

    /**
     * 升级会员等级
     */
    boolean upgradeMembership(String memberId, MembershipType newType);

    /**
     * 停用会员
     */
    boolean deactivateMember(String memberId);

    /**
     * 激活会员
     */
    boolean activateMember(String memberId);

    /**
     * 获取所有会员
     */
    List<Member> getAllMembers();

    /**
     * 根据手机号查找会员
     */
    Member findMemberByPhone(String phone);

    /**
     * 查询会员余额
     */
    double getMemberBalance(String memberId);
}
