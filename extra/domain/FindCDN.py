# -*-* coding:UTF-8
import sys
import dns
import time
from conf import Setting
from lib.core.ClassObject import Extra
from lib.style.ColorPrint import ColorPrint
from concurrent.futures import ThreadPoolExecutor


class FindCDN(Extra):
    def __init__(self):
        super().__init__()
        self.start_up()

    def start_up(self):
        with ThreadPoolExecutor(max_workers=Setting.Options['threads']) as executor:
            for future in executor.map(self.thread_task, Setting.Information):
                char_set = ['\\', '|', '/', '-']
                sys.stdout.write('\r[{}]Found subdomains cdn {}'.format(char_set[int(time.time()) % 4], future))
        ColorPrint('Found {} subdomains cdn'
                   .format(sum(['cdn' in _ for _ in Setting.Information])), 'right')

    def thread_task(self, target_info):
        try:
            cname = dns.resolver.query(target_info['domain'], 'CNAME')[0].to_text()
            cdn = cname.split('.')[-2] + '.' + cname.split('.')[-1]
            target_info['cdn'] = cdn
            return cdn
        except:
            pass
