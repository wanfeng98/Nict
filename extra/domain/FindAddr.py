# -*-* coding:UTF-8
import re
import sys
import time
import requests
from conf import Setting
from lib.style.ColorPrint import ColorPrint
from concurrent.futures import ThreadPoolExecutor


class FindAddr(object):
    def __init__(self):
        self.start_up()

    def start_up(self):
        with ThreadPoolExecutor(max_workers=Setting.Options['threads']) as executor:
            for future in executor.map(self.thread_task, Setting.Information):
                char_set = ['\\', '|', '/', '-']
                sys.stdout.write('\r[{}]Found subdomains address {}'.format(char_set[int(time.time()) % 4], future))
        ColorPrint('Found {} subdomains address'
                   .format(sum(['address' in _ for _ in Setting.Information])), 'right')

    @staticmethod
    def thread_task(target_info):
        try:
            search_url = 'http://ip.cz88.net/data.php?ip={}'.format(target_info['ip'])
            response = requests.post(search_url, headers=Setting.DEFAULT_HTTP_HEADERS,
                                     timeout=Setting.Options['timeout'])
            address = re.findall("ShowIPAddr\('.*','(.*?)','.*'\);", response.text)[0]
            target_info['address'] = address
            return address
        except:
            pass
