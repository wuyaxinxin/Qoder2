#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件名: data_manager.py
作者: 开发者
创建日期: 2025-10-13
版本: 1.0
描述: 数据管理模块
      提供数据持久化、导入导出、备份恢复等功能
"""

import json
import os
import shutil
from datetime import datetime
from typing import Dict, List, Any, Optional
from pathlib import Path


class DataManager:
    """数据管理器类"""
    
    def __init__(self, data_dir: str = "data"):
        """
        初始化数据管理器
        
        Args:
            data_dir (str): 数据目录路径
        """
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        
        # 子目录
        self.backups_dir = self.data_dir / "backups"
        self.exports_dir = self.data_dir / "exports"
        self.logs_dir = self.data_dir / "logs"
        
        # 创建子目录
        for dir_path in [self.backups_dir, self.exports_dir, self.logs_dir]:
            dir_path.mkdir(exist_ok=True)
    
    def save_json(self, data: Dict[str, Any], filename: str) -> bool:
        """
        保存数据为JSON文件
        
        Args:
            data (Dict[str, Any]): 要保存的数据
            filename (str): 文件名
            
        Returns:
            bool: 保存成功返回True，否则返回False
        """
        try:
            file_path = self.data_dir / filename
            
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2, default=str)
            
            self._log_operation(f"保存数据到 {filename}")
            return True
            
        except Exception as e:
            self._log_operation(f"保存数据失败 {filename}: {e}", level="ERROR")
            return False
    
    def load_json(self, filename: str) -> Optional[Dict[str, Any]]:
        """
        从JSON文件加载数据
        
        Args:
            filename (str): 文件名
            
        Returns:
            Optional[Dict[str, Any]]: 加载的数据，失败时返回None
        """
        try:
            file_path = self.data_dir / filename
            
            if not file_path.exists():
                self._log_operation(f"文件不存在: {filename}", level="WARNING")
                return None
            
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            self._log_operation(f"加载数据从 {filename}")
            return data
            
        except Exception as e:
            self._log_operation(f"加载数据失败 {filename}: {e}", level="ERROR")
            return None
    
    def backup_file(self, filename: str, backup_name: str = None) -> bool:
        """
        备份文件
        
        Args:
            filename (str): 源文件名
            backup_name (str): 备份文件名，默认自动生成
            
        Returns:
            bool: 备份成功返回True，否则返回False
        """
        try:
            source_path = self.data_dir / filename
            
            if not source_path.exists():
                self._log_operation(f"备份失败：源文件不存在 {filename}", level="ERROR")
                return False
            
            if backup_name is None:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                file_stem = Path(filename).stem
                file_suffix = Path(filename).suffix
                backup_name = f"{file_stem}_backup_{timestamp}{file_suffix}"
            
            backup_path = self.backups_dir / backup_name
            shutil.copy2(source_path, backup_path)
            
            self._log_operation(f"备份文件：{filename} -> {backup_name}")
            return True
            
        except Exception as e:
            self._log_operation(f"备份失败 {filename}: {e}", level="ERROR")
            return False
    
    def restore_backup(self, backup_name: str, target_filename: str) -> bool:
        """
        从备份恢复文件
        
        Args:
            backup_name (str): 备份文件名
            target_filename (str): 目标文件名
            
        Returns:
            bool: 恢复成功返回True，否则返回False
        """
        try:
            backup_path = self.backups_dir / backup_name
            target_path = self.data_dir / target_filename
            
            if not backup_path.exists():
                self._log_operation(f"恢复失败：备份文件不存在 {backup_name}", level="ERROR")
                return False
            
            shutil.copy2(backup_path, target_path)
            
            self._log_operation(f"恢复文件：{backup_name} -> {target_filename}")
            return True
            
        except Exception as e:
            self._log_operation(f"恢复失败 {backup_name}: {e}", level="ERROR")
            return False
    
    def export_data(self, data: Dict[str, Any], export_name: str, 
                   format_type: str = 'json') -> bool:
        """
        导出数据到指定格式
        
        Args:
            data (Dict[str, Any]): 要导出的数据
            export_name (str): 导出文件名（不含扩展名）
            format_type (str): 导出格式（json/csv）
            
        Returns:
            bool: 导出成功返回True，否则返回False
        """
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{export_name}_{timestamp}.{format_type}"
            
            if format_type.lower() == 'json':
                return self._export_json(data, filename)
            elif format_type.lower() == 'csv':
                return self._export_csv(data, filename)
            else:
                self._log_operation(f"不支持的导出格式: {format_type}", level="ERROR")
                return False
                
        except Exception as e:
            self._log_operation(f"导出失败: {e}", level="ERROR")
            return False
    
    def _export_json(self, data: Dict[str, Any], filename: str) -> bool:
        """导出为JSON格式"""
        try:
            file_path = self.exports_dir / filename
            
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2, default=str)
            
            self._log_operation(f"导出JSON: {filename}")
            return True
            
        except Exception as e:
            self._log_operation(f"导出JSON失败: {e}", level="ERROR")
            return False
    
    def _export_csv(self, data: Dict[str, Any], filename: str) -> bool:
        """导出为CSV格式"""
        try:
            import csv
            
            file_path = self.exports_dir / filename
            
            # 假设数据结构为 {'students': {student_id: student_data}}
            if 'students' in data:
                students_data = data['students']
                
                with open(file_path, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    
                    # 写入表头
                    headers = ['学号', '姓名', '年龄', '专业', '创建时间', '平均成绩', '科目数']
                    writer.writerow(headers)
                    
                    # 写入数据
                    for student_id, student_info in students_data.items():
                        scores = student_info.get('scores', {})
                        avg_score = sum(scores.values()) / len(scores) if scores else 0
                        
                        row = [
                            student_info.get('student_id', ''),
                            student_info.get('name', ''),
                            student_info.get('age', ''),
                            student_info.get('major', ''),
                            student_info.get('created_time', '')[:10],  # 只取日期部分
                            f"{avg_score:.2f}" if avg_score > 0 else "无成绩",
                            len(scores)
                        ]
                        writer.writerow(row)
                
                self._log_operation(f"导出CSV: {filename}")
                return True
            else:
                self._log_operation("数据格式不支持CSV导出", level="ERROR")
                return False
                
        except Exception as e:
            self._log_operation(f"导出CSV失败: {e}", level="ERROR")
            return False
    
    def get_file_list(self, directory: str = None) -> List[str]:
        """
        获取指定目录下的文件列表
        
        Args:
            directory (str): 目录名（backups/exports/logs），默认为主数据目录
            
        Returns:
            List[str]: 文件名列表
        """
        try:
            if directory is None:
                target_dir = self.data_dir
            elif directory == 'backups':
                target_dir = self.backups_dir
            elif directory == 'exports':
                target_dir = self.exports_dir
            elif directory == 'logs':
                target_dir = self.logs_dir
            else:
                target_dir = self.data_dir / directory
            
            if not target_dir.exists():
                return []
            
            files = [f.name for f in target_dir.iterdir() if f.is_file()]
            return sorted(files)
            
        except Exception as e:
            self._log_operation(f"获取文件列表失败: {e}", level="ERROR")
            return []
    
    def delete_file(self, filename: str, directory: str = None) -> bool:
        """
        删除文件
        
        Args:
            filename (str): 文件名
            directory (str): 目录名，默认为主数据目录
            
        Returns:
            bool: 删除成功返回True，否则返回False
        """
        try:
            if directory is None:
                file_path = self.data_dir / filename
            elif directory == 'backups':
                file_path = self.backups_dir / filename
            elif directory == 'exports':
                file_path = self.exports_dir / filename
            elif directory == 'logs':
                file_path = self.logs_dir / filename
            else:
                file_path = self.data_dir / directory / filename
            
            if file_path.exists():
                file_path.unlink()
                self._log_operation(f"删除文件: {filename}")
                return True
            else:
                self._log_operation(f"文件不存在: {filename}", level="WARNING")
                return False
                
        except Exception as e:
            self._log_operation(f"删除文件失败 {filename}: {e}", level="ERROR")
            return False
    
    def get_file_info(self, filename: str) -> Optional[Dict[str, Any]]:
        """
        获取文件信息
        
        Args:
            filename (str): 文件名
            
        Returns:
            Optional[Dict[str, Any]]: 文件信息字典，失败时返回None
        """
        try:
            file_path = self.data_dir / filename
            
            if not file_path.exists():
                return None
            
            stat = file_path.stat()
            
            info = {
                'filename': filename,
                'size': stat.st_size,
                'created_time': datetime.fromtimestamp(stat.st_ctime),
                'modified_time': datetime.fromtimestamp(stat.st_mtime),
                'is_file': file_path.is_file(),
                'absolute_path': str(file_path.absolute())
            }
            
            return info
            
        except Exception as e:
            self._log_operation(f"获取文件信息失败 {filename}: {e}", level="ERROR")
            return None
    
    def cleanup_old_backups(self, keep_days: int = 30) -> int:
        """
        清理旧的备份文件
        
        Args:
            keep_days (int): 保留天数
            
        Returns:
            int: 清理的文件数量
        """
        try:
            cutoff_time = datetime.now().timestamp() - (keep_days * 24 * 3600)
            deleted_count = 0
            
            for backup_file in self.backups_dir.iterdir():
                if backup_file.is_file():
                    if backup_file.stat().st_mtime < cutoff_time:
                        backup_file.unlink()
                        deleted_count += 1
                        self._log_operation(f"清理旧备份: {backup_file.name}")
            
            if deleted_count > 0:
                self._log_operation(f"清理完成，删除了 {deleted_count} 个旧备份文件")
            
            return deleted_count
            
        except Exception as e:
            self._log_operation(f"清理备份失败: {e}", level="ERROR")
            return 0
    
    def _log_operation(self, message: str, level: str = "INFO"):
        """
        记录操作日志
        
        Args:
            message (str): 日志消息
            level (str): 日志级别
        """
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"[{timestamp}] [{level}] {message}\n"
            
            # 写入日志文件
            log_file = self.logs_dir / f"data_manager_{datetime.now().strftime('%Y%m%d')}.log"
            
            with open(log_file, 'a', encoding='utf-8') as f:
                f.write(log_entry)
                
        except Exception:
            # 日志记录失败时不抛出异常，避免影响主要功能
            pass