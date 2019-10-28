# -*-* coding:UTF-8
import re
import sys
import time
import requests
from conf import Setting
from lib.core.ClassObject import Extra
from lib.style.ColorPrint import ColorPrint
from concurrent.futures import ThreadPoolExecutor


class FindSystem(Extra):
    def __init__(self):
        super().__init__()
        self.start_up()

    def start_up(self):
        with ThreadPoolExecutor(max_workers=Setting.Options['threads']) as executor:
            for future in executor.map(self.thread_task, Setting.Information):
                char_set = ['\\', '|', '/', '-']
                sys.stdout.write('\r[{}]Found subdomains system {}'.format(char_set[int(time.time()) % 4], future))
        ColorPrint('Found {} subdomains system'
                   .format(sum(['system' in _ for _ in Setting.Information])), 'right')

    def thread_task(self, target_info):
        try:
            response = requests.get('http://' + target_info['domain'], headers=Setting.DEFAULT_HTTP_HEADERS,
                                    timeout=Setting.Options['timeout'])
            response.encoding = response.apparent_encoding
            target = target_info['domain'].split('.')
            result = re.findall('"(http://.*' + target[-2] + '.' + target[-1] + '/.*\..*)"', response.text)[0]
            response = requests.get(result.upper(), headers=Setting.DEFAULT_HTTP_HEADERS,
                                    timeout=Setting.Options['timeout'])
            if response.status_code == 200:
                target_info['system'] = 'Windows'
            else:
                target_info['system'] = 'Linux'
            return target_info['system']
        except:
            pass
