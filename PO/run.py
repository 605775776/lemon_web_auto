import unittest
import os
from datetime import datetime
from PO.Common.HwTestReport import HTMLTestReport
from PO.Common.setting import Config

# 1 初始化testloader
testloader = unittest.TestLoader()

# 2 加载测试用例
dir_path = os.path.dirname(os.path.abspath(__file__))
case_path = os.path.join(dir_path, 'test_cases')
# 加载多个模块测试用例 保存到测试套件中
suite = testloader.loadTestsFromModule()
# suite2 = testloader.loadTestsFromModule(test_login)

# 添加指定的测试类 快捷键alt+enter
# suite3 = testloader.loadTestsFromTestCase(TestLogin)

# 测试套件组合
# suite_total = unittest.TestSuite()
# suite_total.addTests(suite)
# suite_total.addTests(suite2)
# suite = testloader.discover(start_dir=case_path, pattern='test*.py', top_level_dir=None)


time_str = datetime.now().strftime('%Y%m%d%H%M')
file_name = 'test_report_' + time_str + '.html'
file_path = os.path.join(Config.report_path, file_name, )

with open(file_path, 'wb+') as f:
    runner = HTMLTestReport(stream=f,
                            verbosity=2,
                            )
    runner.run(suite)