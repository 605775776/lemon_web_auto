import logging
from Common.setting import Config

class LoggerHandler(logging.Logger):

    def __init__(self,
                 name='admin',
                 level='DEBUG',
                 file=None,
                 format='%(filename)s-%(lineno)d-%(name)s-%(levelname)s-%(message)s'):
        # Logger(name) 实例化
        super().__init__(name)
        # logger = logging.getLogger(name)
        # 设置级别
        self.setLevel(level)

        # 初始化format
        fmt = logging.Formatter(format)

        # 初始化处理器filename
        if file:
            file_handler = logging.FileHandler(file)
            # 设置handler的级别
            file_handler.setLevel('DEBUG')
            # 设置日志格式
            file_handler.setFormatter(fmt)
            # 添加handler
            self.addHandler(file_handler)

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel('DEBUG')
        stream_handler.setFormatter(fmt)
        self.addHandler(stream_handler)


loggger = LoggerHandler(file=Config.log_path)

if __name__ == '__main__':
    logger = LoggerHandler(file=Config.log_path)
    a = "abc"
    logger.info("获取元素{}".format(a))
    logger.error("error")