# json_config_updater.py
import os
import json
import logging
from typing import Dict, List

logger = logging.getLogger("JSONConfigUpdater")

class JSONConfigUpdater:
    """专门用于更新JSON配置中CPU字段的工具类"""
    
    @staticmethod
    def _ensure_dist_dir(output_path: str):
        """确保输出目录存在，不存在则创建"""
        dist_dir = os.path.dirname(output_path)
        if not os.path.exists(dist_dir):
            os.makedirs(dist_dir, exist_ok=True)
            logger.info(f"已创建目录: {dist_dir}")

    @staticmethod
    def load_json_template(template_path: str = None) -> Dict:
        """加载固定JSON模板（优先使用指定路径，否则使用默认固定结构）"""
        # 如果指定了模板路径，尝试加载
        if template_path and os.path.exists(template_path):
            try:
                with open(template_path, 'r') as f:
                    return json.load(f)
            except Exception as e:
                logger.warning(f"加载指定模板失败，使用默认模板: {str(e)}")
        
        # 默认返回你的固定结构模板（仅cpus字段后续动态更新）
        return {
            "arch": "arm64",
            "name": "rtthread",
            "zone_id": 1,
            "cpus": [2,3],
            "memory_regions": [
                {
                    "type": "ram",
                    "physical_start": "0x40008000",
                    "virtual_start":  "0x40008000",
                    "size": "0x10000000"
                },
                {
                    "type": "io",
                    "physical_start": "0xFD5F8000",
                    "virtual_start":  "0xFD5F8000",
                    "size": "0x1000"
                },
                {
                    "type": "io",
                    "physical_start": "0xfeb50000",
                    "virtual_start":  "0xfeb50000",
                    "size": "0x10000"
                },
                {
                    "type": "io",
                    "physical_start": "0xfeb60000",
                    "virtual_start":  "0xfeb60000",
                    "size": "0x10000"
                },
                {
                    "type": "io",
                    "physical_start": "0xfeba0000",
                    "virtual_start":  "0xfeba0000",
                    "size": "0x10000"
                },
                {
                    "type": "io",
                    "physical_start": "0xFD7C0000",
                    "virtual_start":  "0xFD7C0000",
                    "size": "0x10000"
                },
                {
                    "type": "io",
                    "physical_start": "0xfe660000",
                    "virtual_start":  "0xfe660000",
                    "size": "0x20000"
                },
                {
                    "type": "io",
                    "physical_start": "0xfeae0000",
                    "virtual_start":  "0xfeae0000",
                    "size": "0x1000"
                },
                {
                    "type": "io",
                    "physical_start": "0xfea70000",
                    "virtual_start":  "0xfea70000",
                    "size": "0x10000"
                },
                {
                    "type": "io",
                    "physical_start": "0xfd5fa000",
                    "virtual_start":  "0xfd5fa000",
                    "size": "0x4000"
                },
                {
                    "type": "virtio",
                    "physical_start": "0xff9e0000",
                    "virtual_start":  "0xff9e0000",
                    "size": "0x1000"
                },
                {
                    "type": "io",
                    "physical_start": "0xFD890000",
                    "virtual_start":  "0xFD890000",
                    "size": "0x10000"
                }
            ],
            "interrupts": [366, 326, 80, 375, 363],
            "ivc_configs": [],
            "kernel_filepath": "./zone1rt/rtthread.bin",
            "dtb_filepath": "./zone1rt/zone1-linux.dtb",
            "kernel_load_paddr": "0x40008000",
            "dtb_load_paddr":   "0x40000000",
            "entry_point":      "0x40008000",
            "arch_config": {
                "gic_version": "v3",
                "gicd_base": "0xfe600000",
                "gicd_size": "0x10000",
                "gicr_base": "0xfe680000",
                "gicr_size": "0x10000"
            }
        }
    
    @staticmethod
    def update_cpu_field(json_config: Dict, cpus: List[int]) -> Dict:
        """仅更新JSON配置中的cpus字段"""
        if not isinstance(cpus, list) or not all(isinstance(c, int) for c in cpus):
            logger.error("无效的CPU配置，必须是整数列表")
            return json_config
            
        # 仅更新cpus字段，其他字段保持不变
        json_config["cpus"] = cpus
        logger.info(f"已更新CPU配置为: {cpus}")
        return json_config
    
    @staticmethod
    def save_updated_json(json_config: Dict, output_path: str) -> bool:
        """保存更新后的JSON配置文件"""
        try:
            with open(output_path, 'w') as f:
                json.dump(json_config, f, indent=4)
            logger.info(f"更新后的JSON配置已保存到: {output_path}")
            return True
        except Exception as e:
            logger.error(f"保存JSON配置失败: {str(e)}")
            return False