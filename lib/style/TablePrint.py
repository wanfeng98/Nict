# -*-* coding:UTF-8 -*-*
from prettytable import PrettyTable


class TablePrint(object):
    def __init__(self, data):
        self.data = data
        self._print()

    def _print(self):
        table = PrettyTable(
            ['ID', 'DOMAIN', 'TITLE', 'IP', 'CDN', 'PORT', 'SERVICE', 'LANGUAGE', 'DATABASE', 'SERVER', 'SYSTEM', 'CMS',
             ])
        for _id, target_info in enumerate(self.data):
            table.add_row([_id+1, target_info['domain'] if 'domain' in target_info.keys() else '-',
                           'Found' if 'title' in target_info.keys() else '-',
                           'Found' if 'ip' in target_info.keys() else '-',
                           'Found' if 'cdn' in target_info.keys() else '-',
                           len(target_info['port']) if 'port' in target_info.keys() else '-',
                           'Found' if 'service' in target_info.keys() else '-',
                           'Found' if 'language' in target_info.keys() else '-',
                           'Found' if 'database' in target_info.keys() else '-',
                           'Found' if 'server' in target_info.keys() else '-',
                           'Found' if 'system' in target_info.keys() else '-',
                           'Found' if 'cms' in target_info.keys() else '-'])
        print(table)
