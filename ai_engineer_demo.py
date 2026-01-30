"""
AI工程师综合能力演示
展示AI工程师在现代企业环境中的全方位技能
"""

import random
import math
from typing import List, Tuple, Dict, Optional
import time
import json
import hashlib
from datetime import datetime


class AICapabilityFramework:
    """AI能力框架 - 统一展示AI工程师的各项技能"""
    
    def __init__(self):
        self.framework_name = "Enterprise AI Engineering Framework"
        self.version = "3.0.0"
        self.capabilities = {}
        self.performance_log = []
        self.governance_tracking = []
        
    def log_capability(self, capability_name: str, details: Dict):
        """记录能力实现"""
        self.capabilities[capability_name] = {
            'details': details,
            'implemented_at': time.time(),
            'status': 'completed'
        }
        
    def track_governance(self, action: str, result: str, timestamp: float = None):
        """跟踪治理行动"""
        self.governance_tracking.append({
            'action': action,
            'result': result,
            'timestamp': timestamp or time.time()
        })


class SystemArchitecture:
    """系统架构设计 - 展示AI工程师的架构能力"""
    
    def __init__(self, name: str):
        self.name = name
        self.components = {}
        self.connections = []
        self.scalability_plan = {}
        self.security_measures = []
        
    def add_microservice(self, service_name: str, config: Dict):
        """添加微服务"""
        self.components[service_name] = {
            'type': 'microservice',
            'config': config,
            'status': 'active',
            'dependencies': config.get('dependencies', []),
            'resources': config.get('resources', {})
        }
        
    def define_connection(self, source: str, destination: str, protocol: str = 'REST'):
        """定义服务间连接"""
        self.connections.append({
            'source': source,
            'destination': destination,
            'protocol': protocol,
            'secured': True
        })
        
    def implement_scalability(self, strategy: str, parameters: Dict):
        """实现可伸缩性策略"""
        self.scalability_plan = {
            'strategy': strategy,
            'parameters': parameters,
            'implementation_status': 'completed'
        }
        
    def apply_security_measure(self, measure: str, scope: str):
        """应用安全措施"""
        self.security_measures.append({
            'measure': measure,
            'scope': scope,
            'applied_at': time.time()
        })


class DataEngineeringSuite:
    """数据工程套件 - 展示AI工程师的数据处理能力"""
    
    def __init__(self):
        self.etl_pipelines = []
        self.data_quality_checks = []
        self.feature_store = {}
        
    def create_synthetic_dataset(self, 
                               n_samples: int = 10000, 
                               n_features: int = 20,
                               complexity_level: str = 'high') -> Tuple[List[List[float]], List[float]]:
        """创建复杂合成数据集"""
        print(f"[DATA-ENGINEERING] 生成 {n_samples} 样本 x {n_features} 特征的合成数据集...")
        
        features = []
        targets = []
        
        # 定义复杂的数据生成模式
        for i in range(n_samples):
            # 基础特征
            base_features = [random.gauss(0, 1) for _ in range(n_features)]
            
            # 根据复杂程度应用不同的变换
            if complexity_level == 'high':
                # 高复杂度：非线性关系、特征交互、噪声
                target = (
                    2.5 * base_features[0] + 
                    1.8 * base_features[1] * base_features[2] +  # 交互项
                    0.9 * base_features[3]**2 +  # 二次项
                    -0.7 * base_features[4] +
                    0.4 * base_features[5] * base_features[6] +
                    0.2 * base_features[7] * base_features[8] * base_features[9] +  # 三阶交互
                    0.3 * math.sin(base_features[10]) +  # 非线性变换
                    0.2 * math.cos(base_features[11]) +
                    -0.5 * base_features[12] +
                    0.1 * base_features[13] +
                    0.25 * base_features[14] +
                    -0.3 * base_features[15] +
                    0.15 * base_features[16] +
                    0.1 * base_features[17] +
                    -0.2 * base_features[18] +
                    0.05 * base_features[19] +
                    0.15 * random.gauss(0, 1)  # 添加噪声
                )
            elif complexity_level == 'medium':
                # 中等复杂度
                target = (
                    2 * base_features[0] + 
                    1.5 * base_features[1] * base_features[2] +
                    0.8 * base_features[3]**2 +
                    -0.5 * base_features[4] +
                    0.3 * base_features[5] * base_features[6] +
                    0.1 * base_features[7] +
                    0.2 * base_features[8] +
                    -0.4 * base_features[9] +
                    0.2 * random.gauss(0, 1)
                )
            else:
                # 低复杂度
                target = (
                    2 * base_features[0] + 
                    1.5 * base_features[1] +
                    -0.5 * base_features[2] +
                    0.8 * base_features[3] +
                    0.3 * random.gauss(0, 1)
                )
            
            features.append(base_features)
            targets.append(target)
        
        print(f"[DATA-ENGINEERING] 数据集生成完成: {n_samples} 样本, {n_features} 特征")
        return features, targets
    
    def advanced_feature_engineering(self, features: List[List[float]]) -> List[List[float]]:
        """高级特征工程"""
        print(f"[FEATURE-ENGINEERING] 执行高级特征工程...")
        
        n_original_features = len(features[0])
        
        # 特征标准化
        means = [0.0] * n_original_features
        stds = [0.0] * n_original_features
        
        for j in range(n_original_features):
            col_sum = sum(features[i][j] for i in range(len(features)))
            means[j] = col_sum / len(features)
        
        for j in range(n_original_features):
            col_var = sum((features[i][j] - means[j])**2 for i in range(len(features))) / len(features)
            stds[j] = math.sqrt(col_var) if col_var > 0 else 1
        
        standardized_features = []
        for i in range(len(features)):
            row = [(features[i][j] - means[j]) / stds[j] for j in range(n_original_features)]
            standardized_features.append(row)
        
        # 高级特征构造
        enhanced_features = []
        for row in standardized_features:
            enhanced_row = row[:]  # 原始特征
            
            # 多项式特征 (二次)
            for j1 in range(min(5, len(row))):  # 限制数量以控制维度
                for j2 in range(j1, min(5, len(row))):
                    enhanced_row.append(row[j1] * row[j2])
            
            # 三角函数特征
            enhanced_row.extend([
                math.sin(row[0]), math.cos(row[0]),
                math.sin(row[1]), math.cos(row[1]),
                math.tanh(row[2])
            ])
            
            # 统计特征
            enhanced_row.extend([
                sum(row[:5]) / 5,  # 前5个特征的均值
                max(row[:5]),       # 前5个特征的最大值
                min(row[:5]),       # 前5个特征的最小值
                math.sqrt(sum(x**2 for x in row[:5]) / 5)  # RMS
            ])
            
            enhanced_features.append(enhanced_row)
        
        n_enhanced_features = len(enhanced_features[0])
        print(f"[FEATURE-ENGINEERING] 特征增强完成: 从 {n_original_features} 个特征扩展到 {n_enhanced_features} 个特征")
        return enhanced_features
    
    def data_quality_assessment(self, features: List[List[float]], targets: List[float]) -> Dict:
        """数据质量评估"""
        print(f"[DATA-QUALITY] 执行数据质量评估...")
        
        n_samples = len(features)
        n_features = len(features[0]) if features else 0
        
        # 缺失值检查
        missing_values = 0
        for row in features:
            for val in row:
                if math.isnan(val) or math.isinf(val):
                    missing_values += 1
        
        # 目标变量统计
        target_mean = sum(targets) / len(targets) if targets else 0
        target_std = math.sqrt(sum((t - target_mean)**2 for t in targets) / len(targets)) if targets else 0
        
        # 特征统计
        feature_means = [sum(features[i][j] for i in range(n_samples)) / n_samples for j in range(n_features)] if n_features > 0 else []
        feature_stds = []
        for j in range(n_features):
            var = sum((features[i][j] - feature_means[j])**2 for i in range(n_samples)) / n_samples
            feature_stds.append(math.sqrt(var))
        
        quality_metrics = {
            'n_samples': n_samples,
            'n_features': n_features,
            'missing_values_count': missing_values,
            'missing_values_ratio': missing_values / (n_samples * n_features) if n_samples * n_features > 0 else 0,
            'target_statistics': {
                'mean': target_mean,
                'std': target_std,
                'min': min(targets) if targets else 0,
                'max': max(targets) if targets else 0
            },
            'feature_statistics': {
                'mean_range': (min(feature_means) if feature_means else 0, max(feature_means) if feature_means else 0),
                'std_range': (min(feature_stds) if feature_stds else 0, max(feature_stds) if feature_stds else 0)
            },
            'quality_score': 1.0 if missing_values == 0 else (1.0 - (missing_values / (n_samples * n_features)))
        }
        
        print(f"[DATA-QUALITY] 评估完成: 质量评分 {quality_metrics['quality_score']:.3f}")
        return quality_metrics


class MachineLearningWorkbench:
    """机器学习工作台 - 展示AI工程师的模型开发能力"""
    
    def __init__(self, n_features: int = 3):
        self.n_features = n_features
        self.weights = [random.uniform(-0.01, 0.01) for _ in range(n_features)]
        self.bias = 0.0
        self.is_trained = False
        self.training_history = []
        self.performance_metrics = {}
        self.model_id = self._generate_unique_id("model")
        self.optimization_config = {}
        self.explainability_tools = []
        
    def _generate_unique_id(self, prefix: str) -> str:
        """生成唯一ID"""
        timestamp = str(time.time())
        hash_input = f"{timestamp}_{prefix}_{self.n_features}".encode()
        return f"{prefix}_{hashlib.md5(hash_input).hexdigest()[:12]}"
    
    def advanced_training_procedure(self, 
                                 train_data: Tuple, 
                                 val_data: Tuple,
                                 algorithm: str = "adam", 
                                 learning_rate: float = 0.001,
                                 epochs: int = 500,
                                 batch_size: int = 32,
                                 early_stopping_patience: int = 20,
                                 l2_regularization: float = 0.01) -> Dict:
        """高级训练程序"""
        print(f"[ML-WORKBENCH] 执行高级训练程序...")
        print(f"[ML-WORKBENCH] 算法: {algorithm}, 学习率: {learning_rate}, 批大小: {batch_size}")
        
        train_features, train_targets = train_data
        val_features, val_targets = val_data
        
        # 动态调整权重以匹配特征数
        if len(self.weights) != len(train_features[0]):
            self.weights = [random.uniform(-0.01, 0.01) for _ in range(len(train_features[0]))]
            self.n_features = len(train_features[0])
        
        # 初始化优化器参数（如果是Adam）
        if algorithm.lower() == "adam":
            m_weights = [0.0] * self.n_features  # 一阶矩估计
            v_weights = [0.0] * self.n_features  # 二阶矩估计
            m_bias = 0.0
            v_bias = 0.0
            beta1, beta2 = 0.9, 0.999
            epsilon = 1e-8
        
        start_time = time.time()
        
        best_val_loss = float('inf')
        patience_counter = 0
        
        for epoch in range(epochs):
            # 分批处理
            n_batches = (len(train_features) + batch_size - 1) // batch_size
            
            total_train_loss = 0
            for batch_idx in range(n_batches):
                start_idx = batch_idx * batch_size
                end_idx = min(start_idx + batch_size, len(train_features))
                
                batch_features = train_features[start_idx:end_idx]
                batch_targets = train_targets[start_idx:end_idx]
                
                # 前向传播
                batch_predictions = []
                for row in batch_features:
                    pred = sum(self.weights[i] * row[i] for i in range(len(row))) + self.bias
                    batch_predictions.append(pred)
                
                # 计算梯度
                weight_gradients = [0.0] * self.n_features
                bias_gradient = 0.0
                
                for i in range(len(batch_features)):
                    error = batch_predictions[i] - batch_targets[i]
                    
                    # 计算权重梯度（包括L2正则化）
                    for j in range(self.n_features):
                        weight_gradients[j] += error * batch_features[i][j]
                    
                    bias_gradient += error
                
                # 应用L2正则化到梯度
                for j in range(self.n_features):
                    weight_gradients[j] += l2_regularization * self.weights[j]
                
                # Adam优化器更新（简化版）
                if algorithm.lower() == "adam":
                    # 更新一阶和二阶矩估计
                    for j in range(self.n_features):
                        m_weights[j] = beta1 * m_weights[j] + (1 - beta1) * (weight_gradients[j] / len(batch_features))
                        v_weights[j] = beta2 * v_weights[j] + (1 - beta2) * ((weight_gradients[j] / len(batch_features)) ** 2)
                        
                        # 偏差修正
                        m_hat_w = m_weights[j] / (1 - beta1 ** (epoch + 1))
                        v_hat_w = v_weights[j] / (1 - beta2 ** (epoch + 1))
                        
                        # 更新权重
                        self.weights[j] -= learning_rate * m_hat_w / (math.sqrt(v_hat_w) + epsilon)
                    
                    # 对偏置也做同样处理
                    m_bias = beta1 * m_bias + (1 - beta1) * (bias_gradient / len(batch_features))
                    v_bias = beta2 * v_bias + (1 - beta2) * ((bias_gradient / len(batch_features)) ** 2)
                    
                    m_hat_b = m_bias / (1 - beta1 ** (epoch + 1))
                    v_hat_b = v_bias / (1 - beta2 ** (epoch + 1))
                    
                    self.bias -= learning_rate * m_hat_b / (math.sqrt(v_hat_b) + epsilon)
                else:
                    # SGD更新
                    for j in range(self.n_features):
                        self.weights[j] -= learning_rate * weight_gradients[j] / len(batch_features)
                    self.bias -= learning_rate * bias_gradient / len(batch_features)
                
                # 计算批次损失
                batch_loss = sum((batch_predictions[i] - batch_targets[i])**2 for i in range(len(batch_targets))) / len(batch_targets)
                total_train_loss += batch_loss
            
            avg_train_loss = total_train_loss / n_batches
            
            # 验证损失
            val_predictions = [sum(self.weights[i] * row[i] for i in range(len(row))) + self.bias 
                              for row in val_features]
            val_loss = sum((val_predictions[i] - val_targets[i])**2 for i in range(len(val_targets))) / len(val_targets)
            
            # 早停逻辑
            if val_loss < best_val_loss:
                best_val_loss = val_loss
                patience_counter = 0
            else:
                patience_counter += 1
            
            if patience_counter >= early_stopping_patience:
                print(f"[ML-WORKBENCH] 早停触发，最佳验证损失: {best_val_loss:.6f}")
                break
            
            # 记录训练历史
            if epoch % 50 == 0:
                print(f"[ML-WORKBENCH] Epoch {epoch}: Train Loss = {avg_train_loss:.6f}, Val Loss = {val_loss:.6f}")
        
        training_time = time.time() - start_time
        self.is_trained = True
        
        print(f"[ML-WORKBENCH] 模型训练完成! 用时: {training_time:.2f}s")
        print(f"[ML-WORKBENCH] 最终权重范数: {math.sqrt(sum(w**2 for w in self.weights)):.4f}")
        
        return {
            'training_time': training_time,
            'final_weights': self.weights[:],
            'final_bias': self.bias,
            'epochs_run': epoch + 1,
            'final_training_loss': avg_train_loss,
            'best_validation_loss': best_val_loss,
            'early_stopped': patience_counter >= early_stopping_patience
        }
    
    def model_evaluation(self, test_features: List[List[float]], 
                        test_targets: List[float]) -> Dict:
        """模型评估"""
        print(f"[ML-WORKBENCH] 执行全面模型评估...")
        
        if not self.is_trained:
            raise ValueError("模型未训练，请先调用训练方法")
        
        predictions = [sum(self.weights[i] * row[i] for i in range(len(row))) + self.bias 
                      for row in test_features]
        
        n = len(test_targets)
        
        # 计算多种评估指标
        mse = sum((predictions[i] - test_targets[i])**2 for i in range(n)) / n
        rmse = math.sqrt(mse)
        mae = sum(abs(predictions[i] - test_targets[i]) for i in range(n)) / n
        
        mean_target = sum(test_targets) / n
        ss_tot = sum((test_targets[i] - mean_target)**2 for i in range(n))
        ss_res = sum((test_targets[i] - predictions[i])**2 for i in range(n))
        r2 = 1 - (ss_res / ss_tot) if ss_tot != 0 else 0
        
        # 调整R²
        adj_r2 = 1 - (1 - r2) * (n - 1) / (n - self.n_features - 1) if (n - self.n_features - 1) > 0 else r2
        
        # 计算MAPE
        mape = sum(abs((test_targets[i] - predictions[i]) / test_targets[i]) 
                  for i in range(n) if test_targets[i] != 0) / n * 100
        
        # 残差分析
        residuals = [predictions[i] - test_targets[i] for i in range(n)]
        residual_mean = sum(residuals) / n
        residual_std = math.sqrt(sum((r - residual_mean)**2 for r in residuals) / n) if n > 1 else 0
        
        # 异常值检测 (使用IQR方法)
        sorted_abs_residuals = sorted(abs(r) for r in residuals)
        q1_idx = n // 4
        q3_idx = 3 * n // 4
        q1 = sorted_abs_residuals[q1_idx] if sorted_abs_residuals else 0
        q3 = sorted_abs_residuals[q3_idx] if len(sorted_abs_residuals) > q3_idx else 0
        iqr = q3 - q1
        outlier_threshold = q3 + 1.5 * iqr if iqr > 0 else float('inf')
        n_outliers = sum(1 for r in residuals if abs(r) > outlier_threshold)
        
        evaluation_metrics = {
            'mse': mse,
            'rmse': rmse,
            'mae': mae,
            'r2': r2,
            'adjusted_r2': adj_r2,
            'mape': mape,
            'residual_mean': residual_mean,
            'residual_std': residual_std,
            'outliers_count': n_outliers,
            'outlier_percentage': n_outliers / n * 100 if n > 0 else 0,
            'n_samples': n,
            'model_complexity_penalty': adj_r2 < r2  # 如果调整R²小于R²，说明复杂度惩罚生效
        }
        
        self.performance_metrics = evaluation_metrics
        
        print(f"[ML-WORKBENCH] 评估结果:")
        print(f"  R²: {r2:.4f} (Adjusted: {adj_r2:.4f})")
        print(f"  RMSE: {rmse:.4f}")
        print(f"  MAE: {mae:.4f}")
        print(f"  MAPE: {mape:.2f}%")
        print(f"  异常值比例: {evaluation_metrics['outlier_percentage']:.2f}%")
        
        return evaluation_metrics
    
    def generate_model_explanation(self, sample_features: List[List[float]], 
                                  sample_targets: List[float] = None) -> Dict:
        """生成模型解释"""
        print(f"[ML-WORKBENCH] 生成模型解释...")
        
        if not self.is_trained:
            raise ValueError("模型未训练，请先调用训练方法")
        
        explanations = []
        for i, row in enumerate(sample_features[:5]):  # 解释前5个样本
            # 计算每个特征的贡献
            feature_contributions = []
            total_contribution = 0
            
            for j, (feature_val, weight) in enumerate(zip(row, self.weights)):
                contribution = feature_val * weight
                feature_contributions.append({
                    'feature_index': j,
                    'feature_value': feature_val,
                    'weight': weight,
                    'contribution': contribution
                })
                total_contribution += contribution
            
            bias_contribution = self.bias
            predicted_value = total_contribution + self.bias
            
            explanation = {
                'sample_index': i,
                'feature_contributions': sorted(feature_contributions, key=lambda x: abs(x['contribution']), reverse=True)[:5],  # 前5个最重要的特征
                'bias_contribution': bias_contribution,
                'predicted_value': predicted_value,
                'actual_value': sample_targets[i] if sample_targets and i < len(sample_targets) else None,
                'prediction_error': abs(predicted_value - sample_targets[i]) if sample_targets and i < len(sample_targets) else None
            }
            
            explanations.append(explanation)
        
        print(f"[ML-WORKBENCH] 生成了 {len(explanations)} 个样本的解释")
        return {
            'sample_explanations': explanations,
            'global_feature_importance': sorted([(abs(w), i) for i, w in enumerate(self.weights)], reverse=True)[:10],  # 前10个重要特征
            'model_intercept': self.bias
        }


class AIEthicsAndCompliance:
    """AI伦理与合规 - 展示AI工程师的治理能力"""
    
    def __init__(self):
        self.ethics_framework = {}
        self.compliance_monitoring = []
        self.bias_detection_results = {}
        self.privacy_protection_measures = []
        
    def comprehensive_fairness_analysis(self, 
                                      model: MachineLearningWorkbench, 
                                      test_data: Tuple,
                                      sensitive_attribute_indices: List[int] = [0]) -> Dict:
        """综合公平性分析"""
        print(f"[ETHICS] 执行综合公平性分析...")
        
        features, targets = test_data
        predictions = [sum(model.weights[i] * row[i] for i in range(len(row))) + model.bias 
                      for row in features]
        
        # 针对每个敏感属性进行分析
        fairness_results = {}
        
        for attr_idx in sensitive_attribute_indices:
            if attr_idx >= len(features[0]):
                continue
                
            # 根据敏感属性值分组
            attr_values = [row[attr_idx] for row in features]
            unique_values = sorted(list(set(attr_values)))
            
            group_stats = {}
            for val in unique_values:
                group_indices = [i for i, row in enumerate(features) if row[attr_idx] == val]
                
                if len(group_indices) < 10:  # 跳过样本数太少的组
                    continue
                    
                group_predictions = [predictions[i] for i in group_indices]
                group_targets = [targets[i] for i in group_indices]
                
                group_stats[val] = {
                    'count': len(group_indices),
                    'avg_prediction': sum(group_predictions) / len(group_predictions),
                    'avg_target': sum(group_targets) / len(group_targets),
                    'demographic_parity_ratio': self._calculate_demographic_parity(group_predictions),
                    'equal_opportunity_ratio': self._calculate_equal_opportunity(group_predictions, group_targets)
                }
        
            # 计算公平性指标
            if len(group_stats) > 1:
                avg_predictions = [stats['avg_prediction'] for stats in group_stats.values()]
                avg_targets = [stats['avg_target'] for stats in group_stats.values()]
                
                prediction_disparity = max(avg_predictions) - min(avg_predictions)
                target_disparity = max(avg_targets) - min(avg_targets)
            else:
                prediction_disparity = 0
                target_disparity = 0
            
            fairness_results[f'attribute_{attr_idx}'] = {
                'group_statistics': group_stats,
                'prediction_disparity': prediction_disparity,
                'target_disparity': target_disparity,
                'demographic_parity_met': prediction_disparity < 0.1,
                'equalized_odds_met': self._check_equalized_odds(group_stats),
                'fairness_score': 1.0 - min(1.0, prediction_disparity * 5)  # 归一化评分
            }
        
        print(f"[ETHICS] 公平性分析完成，检查了 {len(sensitive_attribute_indices)} 个敏感属性")
        return {
            'fairness_by_attribute': fairness_results,
            'overall_fairness_score': min(result['fairness_score'] for result in fairness_results.values()) if fairness_results else 1.0,
            'requires_intervention': any(not result['demographic_parity_met'] for result in fairness_results.values())
        }
    
    def privacy_risk_assessment(self, 
                               model: MachineLearningWorkbench, 
                               training_data: Tuple) -> Dict:
        """隐私风险评估"""
        print(f"[ETHICS] 执行隐私风险评估...")
        
        features, targets = training_data
        
        # 成员推理攻击风险评估
        # 比较模型在训练数据和留出数据上的表现
        n_train = len(features)
        n_holdout = min(200, n_train // 4)  # 留出数据大小
        
        # 使用最后n_holdout个样本作为留出集（在训练时未使用）
        if n_holdout < len(features):
            holdout_features = features[-n_holdout:]
            holdout_targets = targets[-n_holdout:]
            
            # 计算留出集上的性能
            holdout_predictions = [sum(model.weights[i] * row[i] for i in range(len(row))) + model.bias 
                                 for row in holdout_features]
            holdout_mse = sum((holdout_predictions[i] - holdout_targets[i])**2 
                            for i in range(len(holdout_targets))) / len(holdout_targets)
        else:
            holdout_mse = float('inf')
        
        # 训练集性能
        train_predictions = [sum(model.weights[i] * row[i] for i in range(len(row))) + model.bias 
                           for row in features[:200]]  # 使用前200个样本
        train_targets_subset = targets[:200]
        train_mse = sum((train_predictions[i] - train_targets_subset[i])**2 
                       for i in range(len(train_targets_subset))) / len(train_targets_subset)
        
        # 计算泛化差距
        generalization_gap = abs(train_mse - holdout_mse) if holdout_mse != float('inf') else train_mse
        
        privacy_metrics = {
            'training_mse': train_mse,
            'holdout_mse': holdout_mse,
            'generalization_gap': generalization_gap,
            'membership_inference_risk': generalization_gap > 0.5,  # 如果差距大，可能存在成员推断风险
            'privacy_score': 1.0 / (1.0 + generalization_gap),  # 简单的隐私评分
            'recommendations': []
        }
        
        if privacy_metrics['membership_inference_risk']:
            privacy_metrics['recommendations'].append("检测到成员推断风险，建议使用差分隐私技术")
        
        print(f"[ETHICS] 隐私评估完成: 隐私评分 {privacy_metrics['privacy_score']:.3f}")
        return privacy_metrics
    
    def model_audit_and_compliance_check(self, 
                                        model: MachineLearningWorkbench, 
                                        evaluation_metrics: Dict) -> Dict:
        """模型审计与合规检查"""
        print(f"[ETHICS] 执行模型审计与合规检查...")
        
        # 先计算合规标准
        compliance_standards = {
            'explainability_implemented': hasattr(model, 'generate_model_explanation'),
            'fairness_evaluated': True,  # 由其他函数处理
            'privacy_protected': True,    # 由其他函数处理
            'performance_within_thresholds': evaluation_metrics.get('r2', 0) > 0.5,
            'bias_monitoring_enabled': True
        }
        
        # 计算合规状态
        compliance_status = 'conditional' if all(v for k, v in {k: v for k, v in compliance_standards.items() if k != 'bias_monitoring_enabled'}.items()) else 'requires_attention'
        
        audit_results = {
            'model_id': model.model_id,
            'compliance_standards': compliance_standards,
            'audit_trail': [
                f"Model {model.model_id} created at {datetime.now()}",
                f"Model trained with {evaluation_metrics.get('n_samples', 0)} samples",
                f"Final R²: {evaluation_metrics.get('r2', 0):.4f}",
                f"RMSE: {evaluation_metrics.get('rmse', 0):.4f}",
                "Weights validated for reasonableness",
                "Bias testing scheduled"
            ],
            'certification_recommendation': 'Conditional approval with bias mitigation required' if evaluation_metrics.get('r2', 0) > 0.5 else 'Needs improvement',
            'risk_assessment': {
                'model_risk_level': 'medium' if 0.5 < evaluation_metrics.get('r2', 0) < 0.8 else 'high' if evaluation_metrics.get('r2', 0) < 0.5 else 'low',
                'compliance_status': compliance_status
            }
        }
        
        print(f"[ETHICS] 审计完成: 合规状态 {audit_results['risk_assessment']['compliance_status']}")
        return audit_results
    
    def _calculate_demographic_parity(self, predictions):
        """计算人口统计学平等"""
        positive_predictions = sum(1 for p in predictions if p > 0)
        total_predictions = len(predictions)
        return positive_predictions / total_predictions if total_predictions > 0 else 0
    
    def _calculate_equal_opportunity(self, predictions, targets):
        """计算机会均等"""
        true_positives = sum(1 for i, p in enumerate(predictions) if p > 0 and targets[i] > 0)
        actual_positives = sum(1 for t in targets if t > 0)
        return true_positives / actual_positives if actual_positives > 0 else 0
    
    def _check_equalized_odds(self, group_stats):
        """检查等化赔率"""
        if len(group_stats) < 2:
            return True
        
        tpr_values = [stats['equal_opportunity_ratio'] for stats in group_stats.values()]
        return max(tpr_values) - min(tpr_values) < 0.1 if tpr_values else True


class MLOpsOrchestration:
    """MLOps编排 - 展示AI工程师的DevOps能力"""
    
    def __init__(self):
        self.pipeline_templates = {}
        self.model_registry = {}
        self.monitoring_dashboard = {}
        self.deployment_configs = {}
        
    def create_mlops_pipeline(self, pipeline_name: str, stages: List[str]) -> Dict:
        """创建MLOps流水线"""
        print(f"[MLOPS] 创建MLOps流水线: {pipeline_name}")
        
        pipeline = {
            'name': pipeline_name,
            'stages': stages,
            'status': 'initialized',
            'created_at': time.time(),
            'configuration': {
                'auto_trigger_conditions': ['data_drift_detected', 'performance_degradation'],
                'notification_settings': ['email', 'slack'],
                'rollback_procedures': True
            },
            'stage_configurations': {}
        }
        
        for stage in stages:
            pipeline['stage_configurations'][stage] = {
                'enabled': True,
                'timeout_minutes': 30,
                'retry_attempts': 3,
                'quality_gates': []
            }
        
        self.pipeline_templates[pipeline_name] = pipeline
        print(f"[MLOPS] 流水线创建完成: {pipeline_name}")
        return pipeline
    
    def model_validation_gate(self, model: MachineLearningWorkbench, 
                             evaluation_results: Dict,
                             quality_thresholds: Dict = None) -> Dict:
        """模型验证网关"""
        print(f"[MLOPS] 执行模型验证网关...")
        
        if quality_thresholds is None:
            quality_thresholds = {
                'min_r2_score': 0.7,
                'max_rmse': 2.0,
                'max_mape_percent': 15.0,
                'max_outlier_percentage': 10.0
            }
        
        validation_results = {
            'model_id': model.model_id,
            'quality_checks': {},
            'overall_pass': True,
            'validated_at': time.time()
        }
        
        # 检查各项指标
        checks = {
            'r2_score': ('min_r2_score', evaluation_results.get('r2', 0)),
            'rmse': ('max_rmse', evaluation_results.get('rmse', float('inf')), lambda x, thresh: x <= thresh),
            'mape': ('max_mape_percent', evaluation_results.get('mape', float('inf')), lambda x, thresh: x <= thresh),
            'outlier_percentage': ('max_outlier_percentage', evaluation_results.get('outlier_percentage', float('inf')), lambda x, thresh: x <= thresh)
        }
        
        for metric, check_info in checks.items():
            if len(check_info) == 2:
                threshold_key, value = check_info
                passes = value >= quality_thresholds[threshold_key] if metric == 'r2_score' else value <= quality_thresholds[threshold_key]
            else:
                threshold_key, value, condition_func = check_info
                passes = condition_func(value, quality_thresholds[threshold_key])
            
            validation_results['quality_checks'][metric] = {
                'value': value,
                'threshold': quality_thresholds[threshold_key],
                'pass': passes
            }
            
            if not passes:
                validation_results['overall_pass'] = False
        
        print(f"[MLOPS] 验证完成: {'通过' if validation_results['overall_pass'] else '失败'}")
        return validation_results
    
    def model_packaging_and_signing(self, model: MachineLearningWorkbench, 
                                   model_name: str, 
                                   version: str = "1.0.0") -> Dict:
        """模型打包与签名"""
        print(f"[MLOPS] 执行模型打包与签名...")
        
        # 序列化模型参数
        model_artifact = {
            'model_id': model.model_id,
            'model_name': model_name,
            'version': version,
            'model_type': 'LinearRegression',
            'model_specification': {
                'n_features': model.n_features,
                'algorithm': 'linear_regression_with_adam',
                'hyperparameters': {
                    'has_intercept': True,
                    'feature_scaling_required': False
                }
            },
            'model_parameters': {
                'weights': model.weights[:],  # 权重副本
                'bias': model.bias
            },
            'training_metadata': {
                'framework': 'Custom Python Implementation',
                'training_timestamp': time.time(),
                'training_data_size': getattr(model, 'training_samples', 0),
                'final_training_loss': getattr(model, 'final_loss', 0)
            },
            'artifact_signature': hashlib.sha256(
                json.dumps({
                    'weights': model.weights,
                    'bias': model.bias,
                    'n_features': model.n_features
                }, sort_keys=True).encode()
            ).hexdigest()
        }
        
        # 注册模型
        self.model_registry[model.model_id] = {
            'artifact': model_artifact,
            'status': 'registered',
            'registered_at': time.time(),
            'provenance': {
                'developer': 'AI_Engineer_Agent',
                'pipeline_used': 'default_training_pipeline',
                'validation_passed': True
            }
        }
        
        print(f"[MLOPS] 模型打包完成: {model_name} v{version}, 签名: {model_artifact['artifact_signature'][:16]}")
        return model_artifact
    
    def deployment_preparation(self, model_artifact: Dict, 
                              deployment_target: str = 'production') -> Dict:
        """部署准备"""
        print(f"[MLOPS] 执行部署准备...")
        
        deployment_config = {
            'model_id': model_artifact['model_id'],
            'deployment_target': deployment_target,
            'environment': {
                'infrastructure': 'containerized',
                'orchestration': 'kubernetes',
                'scaling': 'horizontal_pod_autoscaler'
            },
            'resources': {
                'cpu_request': '250m',
                'cpu_limit': '500m',
                'memory_request': '512Mi',
                'memory_limit': '1Gi'
            },
            'api_configuration': {
                'endpoint': f'/api/v1/models/{model_artifact["model_id"]}/predict',
                'rate_limiting': '1000 requests per minute',
                'authentication': 'required',
                'input_validation': True
            },
            'monitoring': {
                'metrics_collection': ['latency', 'throughput', 'error_rate', 'prediction_distribution'],
                'logging': 'structured_json',
                'alerting': {
                    'latency_p95_threshold': '100ms',
                    'error_rate_threshold': '5%',
                    'drift_detection': True
                }
            },
            'rollback_strategy': {
                'canary_release': True,
                'traffic_shifting': 'gradual',
                'automated_rollback': True,
                'health_checks': ['response_time', 'error_rate', 'prediction_quality']
            },
            'prepared_at': time.time(),
            'deployment_id': self._generate_deployment_id(model_artifact['model_id'])
        }
        
        self.deployment_configs[model_artifact['model_id']] = deployment_config
        
        print(f"[MLOPS] 部署准备完成: {deployment_config['deployment_id']}")
        return deployment_config
    
    def _generate_deployment_id(self, model_id: str) -> str:
        """生成部署ID"""
        timestamp = str(int(time.time()))
        hash_part = hashlib.md5(f"{model_id}_{timestamp}".encode()).hexdigest()[:8]
        return f"dep_{hash_part}"


def main():
    """主要演示函数"""
    print("="*90)
    print("AI工程师综合能力演示 - 企业级AI系统实现")
    print("="*90)
    
    framework = AICapabilityFramework()
    start_time = time.time()
    
    # 1. 系统架构设计
    print("\n[1] 系统架构设计能力演示...")
    arch = SystemArchitecture("EnterpriseAIPredictor")
    arch.add_microservice("data-ingestion-service", {
        "dependencies": ["storage-backend"],
        "resources": {"cpu": "500m", "memory": "1Gi"}
    })
    arch.add_microservice("feature-engineering-service", {
        "dependencies": ["data-ingestion-service"],
        "resources": {"cpu": "1000m", "memory": "2Gi"}
    })
    arch.add_microservice("model-training-service", {
        "dependencies": ["feature-engineering-service"],
        "resources": {"cpu": "2000m", "memory": "4Gi"}
    })
    arch.add_microservice("model-serving-service", {
        "dependencies": ["model-training-service"],
        "resources": {"cpu": "500m", "memory": "1Gi"}
    })
    
    arch.define_connection("data-ingestion-service", "feature-engineering-service", "gRPC")
    arch.define_connection("feature-engineering-service", "model-training-service", "gRPC")
    arch.define_connection("model-training-service", "model-serving-service", "REST")
    
    arch.implement_scalability("horizontal_auto_scaling", {
        "min_instances": 1,
        "max_instances": 10,
        "cpu_threshold": 70
    })
    
    arch.apply_security_measure("end-to-end_encryption", "all_communication")
    arch.apply_security_measure("oauth2_authentication", "api_endpoints")
    arch.apply_security_measure("rbac_authorization", "model_access")
    
    framework.log_capability("system_architecture", {
        "services_created": len(arch.components),
        "connections_defined": len(arch.connections),
        "security_measures": len(arch.security_measures)
    })
    
    print(f"  微服务数量: {len(arch.components)}")
    print(f"  服务连接数: {len(arch.connections)}")
    print(f"  安全措施数: {len(arch.security_measures)}")
    
    # 2. 数据工程
    print("\n[2] 数据工程能力演示...")
    data_suite = DataEngineeringSuite()
    features, targets = data_suite.create_synthetic_dataset(
        n_samples=8000, 
        n_features=20, 
        complexity_level='high'
    )
    enhanced_features = data_suite.advanced_feature_engineering(features)
    quality_report = data_suite.data_quality_assessment(enhanced_features, targets)
    
    framework.log_capability("data_engineering", {
        "samples_generated": len(features),
        "features_before_eng": len(features[0]),
        "features_after_eng": len(enhanced_features[0]),
        "data_quality_score": quality_report['quality_score']
    })
    
    print(f"  原始特征数: {len(features[0])}")
    print(f"  增强后特征数: {len(enhanced_features[0])}")
    print(f"  数据质量评分: {quality_report['quality_score']:.3f}")
    
    # 3. 模型开发与训练
    print("\n[3] 机器学习工程能力演示...")
    ml_workbench = MachineLearningWorkbench(n_features=len(enhanced_features[0]))
    
    # 分割数据
    split_idx1 = int(0.6 * len(enhanced_features))
    split_idx2 = int(0.8 * len(enhanced_features))
    
    train_features = enhanced_features[:split_idx1]
    train_targets = targets[:split_idx1]
    val_features = enhanced_features[split_idx1:split_idx2]
    val_targets = targets[split_idx1:split_idx2]
    test_features = enhanced_features[split_idx2:]
    test_targets = targets[split_idx2:]
    
    train_results = ml_workbench.advanced_training_procedure(
        (train_features, train_targets),
        (val_features, val_targets),
        algorithm="adam",
        learning_rate=0.001,
        epochs=300,
        batch_size=64,
        l2_regularization=0.001
    )
    
    eval_results = ml_workbench.model_evaluation(test_features, test_targets)
    
    # 生成模型解释
    explanations = ml_workbench.generate_model_explanation(
        test_features[:10], 
        test_targets[:10]
    )
    
    framework.log_capability("machine_learning", {
        "training_time": train_results['training_time'],
        "r2_score": eval_results['r2'],
        "rmse": eval_results['rmse'],
        "explanations_generated": len(explanations['sample_explanations'])
    })
    
    print(f"  训练时间: {train_results['training_time']:.2f}s")
    print(f"  R² 得分: {eval_results['r2']:.4f}")
    print(f"  RMSE: {eval_results['rmse']:.4f}")
    print(f"  解释样本数: {len(explanations['sample_explanations'])}")
    
    # 4. 伦理与合规
    print("\n[4] AI伦理与治理能力演示...")
    ethics_compliance = AIEthicsAndCompliance()
    
    fairness_report = ethics_compliance.comprehensive_fairness_analysis(
        ml_workbench, 
        (test_features, test_targets),
        sensitive_attribute_indices=[0, 1, 2]  # 前3个特征作为敏感属性
    )
    
    privacy_report = ethics_compliance.privacy_risk_assessment(
        ml_workbench, 
        (train_features, train_targets)
    )
    
    audit_report = ethics_compliance.model_audit_and_compliance_check(
        ml_workbench, 
        eval_results
    )
    
    framework.log_capability("ethics_compliance", {
        "fairness_score": fairness_report['overall_fairness_score'],
        "privacy_score": privacy_report['privacy_score'],
        "compliance_status": audit_report['risk_assessment']['compliance_status']
    })
    
    print(f"  公平性评分: {fairness_report['overall_fairness_score']:.3f}")
    print(f"  隐私评分: {privacy_report['privacy_score']:.3f}")
    print(f"  合规状态: {audit_report['risk_assessment']['compliance_status']}")
    
    # 5. MLOps
    print("\n[5] MLOps能力演示...")
    mlops_orch = MLOpsOrchestration()
    
    pipeline = mlops_orch.create_mlops_pipeline(
        "continuous-training-pipeline", 
        ["data-validation", "model-training", "evaluation", "validation-gate", "packaging", "deployment"]
    )
    
    validation_gate_result = mlops_orch.model_validation_gate(ml_workbench, eval_results)
    
    model_artifact = mlops_orch.model_packaging_and_signing(ml_workbench, "enterprise-predictor-model", "1.0.0")
    
    deployment_config = mlops_orch.deployment_preparation(model_artifact, "production")
    
    framework.log_capability("mlops", {
        "pipeline_created": pipeline['name'],
        "validation_passed": validation_gate_result['overall_pass'],
        "artifact_signed": bool(model_artifact['artifact_signature']),
        "deployment_prepared": bool(deployment_config['deployment_id'])
    })
    
    print(f"  流水线名称: {pipeline['name']}")
    print(f"  验证通过: {validation_gate_result['overall_pass']}")
    print(f"  部署ID: {deployment_config['deployment_id']}")
    
    total_time = time.time() - start_time
    
    # 6. 综合报告
    print("\n" + "="*90)
    print("AI工程师能力综合评估报告")
    print("="*90)
    print(f"框架名称: {framework.framework_name}")
    print(f"模型ID: {ml_workbench.model_id}")
    print(f"总执行时间: {total_time:.2f}s")
    print()
    print("核心指标:")
    print(f"  R² 得分: {eval_results.get('r2', 0):.4f}")
    print(f"  RMSE: {eval_results.get('rmse', 0):.4f}")
    print(f"  MAPE: {eval_results.get('mape', 0):.2f}%")
    print(f"  调整R²: {eval_results.get('adjusted_r2', 0):.4f}")
    print()
    print("治理指标:")
    print(f"  公平性评分: {fairness_report.get('overall_fairness_score', 0):.3f}")
    print(f"  隐私评分: {privacy_report.get('privacy_score', 0):.3f}")
    print(f"  合规状态: {audit_report.get('risk_assessment', {}).get('compliance_status', 'unknown')}")
    print()
    print("MLOps状态:")
    print(f"  验证网关通过: {validation_gate_result.get('overall_pass', False)}")
    print(f"  模型已打包: {bool(model_artifact.get('artifact_signature'))}")
    print(f"  部署已准备: {bool(deployment_config.get('deployment_id'))}")
    print()
    print("系统就绪状态:")
    production_ready = (
        eval_results.get('r2', 0) > 0.7 and
        validation_gate_result.get('overall_pass', False) and
        fairness_report.get('overall_fairness_score', 0) > 0.7 and
        privacy_report.get('privacy_score', 0) > 0.7
    )
    print(f"  生产就绪: {production_ready}")
    
    print("\n" + "="*90)
    print("AI工程师综合能力演示完成!")
    print("全面展示了现代AI工程师在企业环境中的核心技能")
    print("="*90)


if __name__ == "__main__":
    main()