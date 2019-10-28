# -*-* coding:UTF-8
import re
import sys
import time
import requests
from conf import Setting
from lib.core.ClassObject import Extra
from lib.style.ColorPrint import ColorPrint
from concurrent.futures import ThreadPoolExecutor


class FindSub(Extra):
    def __init__(self):
        super().__init__()
        self.start_up()

    def start_up(self):
        with ThreadPoolExecutor(max_workers=Setting.Options['threads']) as executor:
            for future in executor.map(self.thread_task,
                                       [[Setting.Information, target] for target in Setting.Options['target']]):
                char_set = ['\\', '|', '/', '-']
                sys.stdout.write('\r[{}]Found subdomains {}'.format(char_set[int(time.time()) % 4], future))
        Setting.Information = [dict(t) for t in set([tuple(d.items()) for d in Setting.Information])]
        ColorPrint('Found {} subdomains'.format(len(Setting.Information)), 'right')

    def thread_task(self, args_list):
        try:
            search_url = 'https://www.baidu.com/s?ie=utf-8&wd=site:{}'.format(args_list[1])
            domain_filter = ''
            for n in range(1, 5):
                response = requests.get(search_url + domain_filter, headers=Setting.DEFAULT_HTTP_HEADERS,
                                        timeout=Setting.Options['timeout'])
                search_result = re.findall('<a.*?class="c-showurl".*?>(http://|https://)?(.*?)/.*?</a>', response.text)
                for domain in map(lambda x: x[1], list(set(search_result))):
                    if args_list[1] in domain:
                        args_list[0].append({'domain': domain})
                for domain in args_list[0]:
                    domain_filter = domain_filter + ' -site:{}'.format(domain)
        except:
            ColorPrint('Baidu search subdomains failure', 'warn')
        try:
            search_url = 'https://site.ip138.com/{}/domain.htm'.format(args_list[1])
            response = requests.get(search_url, headers=Setting.DEFAULT_HTTP_HEADERS,
                                    timeout=Setting.Options['timeout'])
            search_result = re.findall('<a.*target="_blank">(.*\.' + args_list[1] + ')</a>', response.text)
            for domain in search_result:
                args_list[0].append({'domain': domain})
        except:
            ColorPrint('IP138 search subdomains failure', 'warn')
        try:
            search_url = 'https://securitytrails.com/domain/{}/dns'.format(args_list[1])
            response = requests.get(search_url, headers=Setting.DEFAULT_HTTP_HEADERS,
                                    timeout=Setting.Options['timeout'])
            search_result = re.findall('"subdomains":(.*?),"stats"', response.text)[0]
            for domain in eval(search_result):
                args_list[0].append({'domain': domain + '.' + args_list[1]})
        except:
            ColorPrint('Securitytrails search subdomains failure', 'warn')
