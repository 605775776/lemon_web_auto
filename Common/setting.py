import os


class Config:
    # 项目路径
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # common路径
    Common_path = os.path.join(root_path, 'common')

    # config路径
    config_path = os.path.join(root_path, 'config')

    # 日志配置路径
    yaml_config_path = os.path.join(config_path, 'config.yaml')

    # 输出文件路径
    Outputs_path = os.path.join(root_path, 'Outputs')

    # 失败截图路径
    screenshot_dir = os.path.join(Outputs_path, 'screenshots')
    if not os.path.exists(screenshot_dir):
        os.mkdir(screenshot_dir)
    # 测试数据路径
    data_path = os.path.join(root_path, 'data\\test_cases.xlsx')

    # 测试用例路径
    case_path = os.path.join(root_path, 'test_cases')

    # log日志路径
    log_path = os.path.join(root_path, 'log')
    if not os.path.exists(log_path):
        os.mkdir(log_path)

    # 测试报告路径
    report_path = os.path.join(root_path, 'report')
    if not os.path.exists(report_path):
        os.mkdir(report_path)


class DevConfig(Config):
    # 项目的域名
    host = 'http://120.78.128.27:8765/futureloan'


config = DevConfig()
if __name__ == '__main__':
    print(Config.root_path)
    print(Config.Outputs_path)
    print(Config.screenshot_dir)