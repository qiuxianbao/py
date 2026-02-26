"""
安装日志包
pip install logging

"""

import json
import sys
from typing import Any
import logging

class LogFormat:
    @staticmethod
    def format_print(data: Any, title: str = "Log Output", width: int = 50):

        # 配置日志格式
        logging.basicConfig(
            level=logging.DEBUG,  # debug和info的默认不会打印
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        """
        格式化打印数据
        :param data: 要打印的数据
        :param title: 标题
        :param width: 边框宽度
        """
        logging.info(f"{'=' * width} {title} {'=' * width}")
        
        if isinstance(data, (dict, list)):
            # 如果是字典或列表，使用JSON美化输出
            logging.info(json.dumps(data, indent=2, ensure_ascii=False))
        else:
            logging.info(data)

        logging.info(f"{'=' * ( 2 + width * 2 + len(title))}\n")

if __name__ == '__main__':
    LogFormat.format_print("hello world")
    LogFormat.format_print("content", "Title")
    LogFormat.format_print({"name": "张三", "age": 18}, "JSON")