# -*-* coding:UTF-8
import os
import sys
import click
import traceback
from lib.banner import Banner
from lib.style.ColorPrint import ColorPrint
from lib.core.CollectInfo import CollectInfo


@click.command()
@click.option('--target', help='Set target domain')
@click.option('--threads', help='Set number of threads(default 200).', type=click.IntRange(1, 999), default=200)
@click.option('--process', help='Set number of process(default 4).', type=click.IntRange(1, 60), default=4)
@click.option('--timeout', help='Set timeout connection(default 5).', default=5)
@click.option('--output', help='Save the results to the file.', default=os.path.join('output', 'result.txt'))
def cli(**kwargs):
    """Easy to use internet information collection tool"""
    os.system("")
    return main(kwargs)


def main(kwargs):
    # main function of nict
    Banner.show()
    check_environment()
    CollectInfo(kwargs)


def check_environment():
    # check the current environment,version
    ColorPrint('Check the current environment', 'info')
    if sys.version_info[0] < 3:
        ColorPrint("Must be using Python 3.X", 'error')
    try:
        # is install import packages?
        import click
        import requests
        import dns.resolver
    except:
        exec_msg = traceback.format_exc()
        if any(_ in exec_msg for _ in ("ImportError", "ModuleNotFoundError", "Can't find file for module")):
            ColorPrint("Invalid runtime environment : %s" % exec_msg.split("Error: ")[-1].strip(), 'error')
        raise SystemExit


if __name__ == '__main__':
    try:
        cli()
    except KeyboardInterrupt:
        pass
    except SystemExit:
        raise
