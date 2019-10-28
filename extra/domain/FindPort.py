# -*-* coding:UTF-8 -*-*
import sys
import time
import socket
from conf import Setting
from multiprocessing.dummy import Pool
from lib.core.ClassObject import Extra
from lib.style.ColorPrint import ColorPrint
from concurrent.futures import ThreadPoolExecutor


class FindPort(Extra):
    def __init__(self):
        super().__init__()
        self.start_up()

    def start_up(self):
        with Pool(Setting.Options['process']) as p:
            p.map(self.process_task, Setting.Information)
        ColorPrint('Found {} subdomains port'
                   .format(sum(['port' in _ for _ in Setting.Information])), 'right')

    def process_task(self, target_info):
        target_info['port'] = []
        target_info['service'] = []
        with ThreadPoolExecutor(max_workers=Setting.Options['threads']) as executor:
            for future in executor.map(self.thread_task,
                                       [[target_info, port] for port in Setting.DEFAULT_PORT_SERVICES.keys()]):
                char_set = ['\\', '|', '/', '-']
                sys.stdout.write('\r[{}]Found subdomains port {}'.format(char_set[int(time.time()) % 4], future))

    def thread_task(self, args_list):
        try:
            socket.setdefaulttimeout(2)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = s.connect_ex((args_list[0]['ip'], int(args_list[1])))
            if result == 0:
                service = Setting.DEFAULT_PORT_SERVICES[args_list[1]]
                args_list[0]['port'].append(args_list[1])
                args_list[0]['service'].append(service)
            s.close()
            return args_list[1]
        except:
            pass
