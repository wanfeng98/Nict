# -*-* coding:UTF-8
import sys
import time
import requests
from conf import Setting
from lib.style.ColorPrint import ColorPrint
from concurrent.futures import ThreadPoolExecutor


class FindCMS(object):
    def __init__(self):
        self.start_up()

    def start_up(self):
        with ThreadPoolExecutor(max_workers=Setting.Options['threads']) as executor:
            for future in executor.map(self.thread_task, Setting.Information):
                char_set = ['\\', '|', '/', '-']
                sys.stdout.write('\r[{}]Found subdomains cms {}'.format(char_set[int(time.time()) % 4], future))
        ColorPrint('Found {} subdomains cms'
                   .format(sum(['cms' in _ for _ in Setting.Information])), 'right')

    @staticmethod
    def thread_task(target_info):
        try:
            search_url = 'https://whatcms.org/APIEndpoint/Technology?key=4ac0c57c5f2ec2b1bf7e0bfaaef52e91f44eaecbd5' \
                         'a8e640cd69435bc95ab96b856aef&url={}'.format(target_info['domain'])
            response = requests.get(search_url, headers=Setting.DEFAULT_HTTP_HEADERS,
                                    timeout=Setting.Options['timeout'])
            result_dict = eval(response.text)['results']
            if result_dict[0]['name']:
                target_info['cms'] = result_dict[0]['name'] + '/' + result_dict[0]['version']
            if result_dict[1]['name']:
                target_info['language'] = result_dict[1]['name'] + '/' + result_dict[1]['version']
            if result_dict[2]['name']:
                target_info['database'] = result_dict[2]['name'] + '/' + result_dict[2]['version']
            if result_dict[3]['name']:
                target_info['server'] = result_dict[3]['name'] + '/' + result_dict[3]['version']
            return result_dict[0]['name']
        except:
            pass
