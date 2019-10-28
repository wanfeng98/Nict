# -*-* coding:UTF-8
import re
import sys
import time
import requests
from conf import Setting
from lib.core.ClassObject import Extra
from lib.style.ColorPrint import ColorPrint
from concurrent.futures import ThreadPoolExecutor


class FindTitle(Extra):
    def __init__(self):
        super().__init__()
        self.start_up()

    def start_up(self):
        with ThreadPoolExecutor(max_workers=Setting.Options['threads']) as executor:
            for future in executor.map(self.thread_task, Setting.Information):
                char_set = ['\\', '|', '/', '-']
                sys.stdout.write('\r[{}]Found subdomains title {}'.format(char_set[int(time.time()) % 4], future))
        ColorPrint('Found {} subdomains title'
                   .format(sum(['title' in _ for _ in Setting.Information])), 'right')

    def thread_task(self, target_info):
        try:
            response = requests.get('http://' + target_info['domain'], headers=Setting.DEFAULT_HTTP_HEADERS,
                                    timeout=Setting.Options['timeout'])
            response.encoding = response.apparent_encoding
            if response.status_code == 200:
                title = re.search('<title>(.*?)</title>', response.text, re.I).group(1)
            elif response.status_code == 302:
                title = '302 to %s' % response.url
            else:
                title = response.status_code
            target_info['title'] = title.strip()
            return title.strip()
        except:
            pass
