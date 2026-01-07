// 始终生效
package billiard.repository.impl;

import billiard.model.Member;
import billiard.repository.MemberRepository;
import java.util.*;
import java.util.stream.Collectors;

/**
 * 会员仓储实现类（使用内存存储）
 */
public class MemberRepositoryImpl implements MemberRepository {
    private final Map<String, Member> memberStore;

    public MemberRepositoryImpl() {
        this.memberStore = new HashMap<>();
    }

    @Override
    public void save(Member member) {
        if (member != null && member.getMemberId() != null) {
            memberStore.put(member.getMemberId(), member);
        }
    }

    @Override
    public Optional<Member> findById(String memberId) {
        return Optional.ofNullable(memberStore.get(memberId));
    }

    @Override
    public Optional<Member> findByPhone(String phone) {
        return memberStore.values().stream()
                .filter(member -> member.getPhone().equals(phone))
                .findFirst();
    }

    @Override
    public List<Member> findAll() {
        return new ArrayList<>(memberStore.values());
    }

    @Override
    public boolean delete(String memberId) {
        return memberStore.remove(memberId) != null;
    }

    @Override
    public void update(Member member) {
        if (member != null && memberStore.containsKey(member.getMemberId())) {
            memberStore.put(member.getMemberId(), member);
        }
    }
}
