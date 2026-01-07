// 始终生效
package billiard.repository;

import billiard.model.Member;
import java.util.List;
import java.util.Optional;

/**
 * 会员仓储接口
 */
public interface MemberRepository {
    /**
     * 保存会员
     */
    void save(Member member);

    /**
     * 根据ID查找会员
     */
    Optional<Member> findById(String memberId);

    /**
     * 根据手机号查找会员
     */
    Optional<Member> findByPhone(String phone);

    /**
     * 获取所有会员
     */
    List<Member> findAll();

    /**
     * 删除会员
     */
    boolean delete(String memberId);

    /**
     * 更新会员
     */
    void update(Member member);
}
