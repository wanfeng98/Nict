# -*-* coding:UTF-8 -*-*
from prettytable import PrettyTable
from lib.core.ClassObject import Output


class OutputFile(Output):
    def __init__(self, path, data):
        super().__init__()
        self.file_path = path
        self.file_data = data
        self.write_file()

    def write_file(self):
        table = PrettyTable(
            ['ID', 'DOMAIN', 'TITLE', 'IP', 'CDN', 'PORT', 'SERVICE', 'LANGUAGE', 'DATABASE', 'SERVER', 'SYSTEM', 'CMS',
             ])
        for _id, target_info in enumerate(self.file_data):
            table.add_row([_id + 1, target_info['domain'] if 'domain' in target_info.keys() else '-',
                           target_info['title'] if 'title' in target_info.keys() else '-',
                           target_info['ip'] if 'ip' in target_info.keys() else '-',
                           target_info['cdn'] if 'cdn' in target_info.keys() else '-',
                           target_info['port'] if 'port' in target_info.keys() else '-',
                           target_info['service'] if 'service' in target_info.keys() else '-',
                           target_info['language'] if 'language' in target_info.keys() else '-',
                           target_info['database'] if 'database' in target_info.keys() else '-',
                           target_info['server'] if 'server' in target_info.keys() else '-',
                           target_info['system'] if 'system' in target_info.keys() else '-',
                           target_info['cms'] if 'cms' in target_info.keys() else '-'])
        with open(self.file_path, 'w', encoding='utf-8') as f:
            f.write(table.get_string())
