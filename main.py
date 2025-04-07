from unittest import defaultTestLoader
from BeautifulReport import BeautifulReport
import json

# 解析配置文件
with open('config.json', 'r', encoding='utf-8') as f:  
    config = dict(json.load(f))

# 获取测试用例目录信息
cases=config.get("cases")
start_dir=cases.get("start_dir")
pattern=cases.get("pattern")

# 获取报告信息
reports=config.get("reports")
description=reports.get("description")
filename=reports.get("filename")
report_dir=reports.get("report_dir")

# 加载测试用例 
suite=defaultTestLoader.discover(start_dir, pattern)

# 测试并生成测试报告
BeautifulReport(suites=suite).report(description, filename, report_dir)