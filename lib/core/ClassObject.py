# 输出写法模板
class Output(object):
    def __init__(self):
        """定义输出接口"""
        self.file_path = ''
        self.file_data = ''

    def write_file(self):
        """定义输出方法"""
        raise NotImplementedError


# 扩展写法模板
class Extra(object):
    def __init__(self):
        """定义扩展属性"""
        pass

    def start_up(self):
        """定义启动方法"""
        raise NotImplementedError

    def thread_task(self, args):
        """定义执行方法"""
        raise NotImplementedError
