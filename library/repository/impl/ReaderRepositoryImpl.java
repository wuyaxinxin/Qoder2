// 始终生效
// 模型决策

package library.repository.impl;

import library.model.Reader;
import library.repository.ReaderRepository;
import java.util.*;
import java.util.stream.Collectors;

/**
 * 读者数据访问实现类
 * 使用内存HashMap存储读者数据
 */
public class ReaderRepositoryImpl implements ReaderRepository {
    
    // 使用HashMap存储读者数据，key为读者编号，value为读者对象
    private final Map<String, Reader> readerStorage = new HashMap<>();
    
    @Override
    public boolean add(Reader reader) {
        if (reader == null || reader.getReaderId() == null) {
            return false;
        }
        
        // 检查读者编号是否已存在
        if (readerStorage.containsKey(reader.getReaderId())) {
            return false;
        }
        
        readerStorage.put(reader.getReaderId(), reader);
        return true;
    }
    
    @Override
    public boolean delete(String readerId) {
        if (readerId == null) {
            return false;
        }
        
        return readerStorage.remove(readerId) != null;
    }
    
    @Override
    public boolean update(Reader reader) {
        if (reader == null || reader.getReaderId() == null) {
            return false;
        }
        
        // 检查读者是否存在
        if (!readerStorage.containsKey(reader.getReaderId())) {
            return false;
        }
        
        readerStorage.put(reader.getReaderId(), reader);
        return true;
    }
    
    @Override
    public Optional<Reader> findById(String readerId) {
        if (readerId == null) {
            return Optional.empty();
        }
        
        return Optional.ofNullable(readerStorage.get(readerId));
    }
    
    @Override
    public List<Reader> findAll() {
        return new ArrayList<>(readerStorage.values());
    }
    
    @Override
    public List<Reader> findByName(String name) {
        if (name == null || name.trim().isEmpty()) {
            return new ArrayList<>();
        }
        
        String keyword = name.trim().toLowerCase();
        return readerStorage.values().stream()
                .filter(reader -> reader.getName().toLowerCase().contains(keyword))
                .collect(Collectors.toList());
    }
    
    @Override
    public boolean exists(String readerId) {
        if (readerId == null) {
            return false;
        }
        
        return readerStorage.containsKey(readerId);
    }
    
    @Override
    public int count() {
        return readerStorage.size();
    }
}
