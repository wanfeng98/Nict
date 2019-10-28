# -*-* coding:UTF-8
import sys
import time
import dns.resolver
from conf import Setting
from lib.style.ColorPrint import ColorPrint
from concurrent.futures import ThreadPoolExecutor


class FindIP(object):
    def __init__(self):
        self.start_up()

    def start_up(self):
        with ThreadPoolExecutor(max_workers=Setting.Options['threads']) as executor:
            for future in executor.map(self.thread_task, Setting.Information):
                char_set = ['\\', '|', '/', '-']
                sys.stdout.write('\r[{}]Found subdomains ip {}'.format(char_set[int(time.time()) % 4], future))
        ColorPrint('Found {} subdomains ip'.format(sum(['ip' in _ for _ in Setting.Information])), 'right')

    @staticmethod
    def thread_task(target_info):
        try:
            Resolver = dns.resolver.Resolver()
            Resolver.nameservers = ['8.8.8.8', '114.114.114.114']
            ip = Resolver.query(target_info['domain'], 'A')[0].to_text()
            target_info['ip'] = ip
            return ip
        except:
            pass
