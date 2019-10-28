# -*-* coding:UTF-8 -*-*
import time
import importlib
from conf import Setting
from extra.domain.FindIP import FindIP
from extra.domain.FindSub import FindSub
from extra.domain.FindCMS import FindCMS
from extra.domain.FindCDN import FindCDN
from extra.domain.FindPort import FindPort
from extra.domain.FindAddr import FindAddr
from lib.style.ColorPrint import ColorPrint
from lib.style.TablePrint import TablePrint
from extra.domain.FindTitle import FindTitle
from extra.domain.FindSystem import FindSystem


class CollectInfo(object):
    def __init__(self, options):
        self.init(options)
        self.start_up()

    @staticmethod
    def init(options):
        Setting.Options = options
        Setting.Information = []
        Setting.Options['target'] = [options['target']]

    def start_up(self):
        try:
            start = time.time()
            FindSub()  # to found subdomains
            if len(Setting.Information) != 0:
                FindIP()
                FindPort()
                self.filter_data()
                FindCDN()
                FindAddr()
                FindTitle()
                FindCMS()
                FindSystem()
                TablePrint(Setting.Information)
                stop = time.time()
                self.write_file()
                ColorPrint('Thanks for using this tool ..End/{}s'.format(round(stop - start, 2)), 'info')
            else:
                ColorPrint('Nothing found', 'error')
        except:
            ColorPrint('Run error', 'error')

    @staticmethod
    def write_file():
        try:
            output_object = importlib.import_module(
                'lib.output.' + Setting.Options['output'][-3:].title() + 'Output')
            output_object.OutputFile(Setting.Options['output'], Setting.Information)
        except:
            ColorPrint('Invalid save file type', 'error')

    @staticmethod
    def filter_data():
        filter_list = []
        for _dict in Setting.Information:
            if 'ip' in _dict.keys():
                filter_list.append(_dict)
        Setting.Information = filter_list
